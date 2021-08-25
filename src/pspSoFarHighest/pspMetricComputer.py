import datetime as dt
from typing import List
import pandas as pd
import numpy as np
from src.typeDefs.pspPoints import IlistPspPoint, IpspPoint
from src.typeDefs.newSoFarHighObj import InewSoFarHighObj
from src.fetchers.pspMetricDataFetcher import PspMetricDataFetcher
from src.soFarHighestRepo.soFarHighMetricFetcher import SoFarHighMetricFetch
from src.soFarHighestRepo.insNewSoFarHighData import NewSoFarHighInsertion
from src.pspSoFarHighest.pspMetricComparison import comparePspMetric


def computePspMetric(startDate:dt.datetime, endDate:dt.datetime, pspPointsConfig:IlistPspPoint, appConfig:dict)->bool:
    """fetch psp metric data from psp_db, and update so far highest table data

    Args:
        startDate (dt.datetime): startdate
        endDate (dt.datetime): enddate
        pspPointsConfig (IlistPspPoint): psp point config dictionary containing fetch SQL queries, metric name, and reasonabilty limit
        appConfig (dict): app config dictionary

    Returns:
        bool: return true if computations successfull
    """    
    dbConString = appConfig['con_string_mis_warehouse']
    pspDbConString = appConfig['con_string_server_db']
    countLoopIter = 0
    
    # creating instances of classes
    obj_pspMetricDataFetcher = PspMetricDataFetcher(pspDbConString)
    obj_pspSoFarHighMetricFetch = SoFarHighMetricFetch(dbConString)
    obj_newSoFarHighInsertion = NewSoFarHighInsertion(dbConString)
    
    # iterating through each day and each psp metric
    currDate = startDate
    while currDate <= endDate:
        for pspPoint in pspPointsConfig:
            try:
                # checking if sql corresponding to psp metric exist in config
                if not pd.isna(pspPoint['metricFetchSql']):
                    pspMetricData = obj_pspMetricDataFetcher.fetchPspMetricData(currDate, currDate, pspPoint)
                    
                    # fetch till now so far highest                 
                    pspMetricSoFarHighDf = obj_pspSoFarHighMetricFetch.fetchSoFarHighMeteric(pspPoint['metricName'])
                    
                    # comparison(algo implementation)
                    if not (pspMetricSoFarHighDf.empty or pspMetricData.empty) :
                            # return false if no changes in soFarhighest else return new sofarhighest object.
                            newSoFarHigheObj :InewSoFarHighObj = comparePspMetric(pspMetricData, pspMetricSoFarHighDf)
                            
                            if newSoFarHigheObj:
                                isnewSoFarHighUpdationSuccess = obj_newSoFarHighInsertion.insertNewSoFarHigh(newSoFarHigheObj)
            except Exception as err:
                print(err)
            finally:
                countLoopIter = countLoopIter +1
        currDate += dt.timedelta(days=1)

    numOfDays = (endDate-startDate).days

    #checking whether data is computed for each day or not
    if countLoopIter == (numOfDays+1)*len(pspPointsConfig):
        return True
    else:
        return False
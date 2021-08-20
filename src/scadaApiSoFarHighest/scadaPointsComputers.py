import datetime as dt
from typing import List
import pandas as pd
from src.fetchers.scadaApiFetcher import ScadaApiFetcher
from src.typeDefs.scadaPoints import IlistScadaPoint, IscadaPoint
from src.typeDefs.newSoFarHighObj import InewSoFarHighObj
from src.fetchers.scadaApiFetcher import ScadaApiFetcher
from src.soFarHighestRepo.soFarHighMetricFetcher import SoFarHighMetricFetch
from src.scadaApiSoFarHighest.scadaMetricComparison import compareScadaMetric
from src.soFarHighestRepo.insNewSoFarHighData import NewSoFarHighInsertion

def computeScadaPoints(startDate:dt.datetime, endDate:dt.datetime, scadaPointsConfig:dict, appConfig:dict)->bool:
    """fetch scada metric data from scada api, and update so far highest table data

    Args:
        startDate (dt.datetime): startdate
        endDate (dt.datetime): endDate
        scadaPointsConfig (dict):  scada point config dictionary containing scada points for scada api
        appConfig (dict): app config dictionary

    Returns:
        bool: return true if computations successfull
    """
    
    dbConString = appConfig['con_string_mis_warehouse']
    tokenUrl = appConfig['tokenUrl']
    apiBaseUrl = appConfig['apiBaseUrl']
    clientId = appConfig['clientId']
    clientSecret = appConfig['clientSecret']
    countLoopIter = 0
    
    # creating instances of classes
    obj_scadaApiFetcher = ScadaApiFetcher(tokenUrl, apiBaseUrl, clientId, clientSecret)
    obj_scadaMetricSoFarHighFetch= SoFarHighMetricFetch(dbConString)
    obj_newSoFarHighInsertion = NewSoFarHighInsertion(dbConString)
    
    # making list of scada points from dictionary
    scadaPoints:IlistScadaPoint= []
    listScadaPoints = scadaPointsConfig.items()
    for points in listScadaPoints:
        tempDict:IscadaPoint = {'metricName': points[0], 'metricScadaId':points[1]}
        scadaPoints.append(tempDict)
    
    # iterating through each day and each scada metric
    currDate = startDate
    while currDate <= endDate:
        for scadaPoint in scadaPoints:
            try:
                # fetch scada points via scada api
                resData = obj_scadaApiFetcher.fetchData(scadaPoint['metricScadaId'], currDate, currDate)

                if len(resData)>0:
                    respDf= pd.DataFrame(resData, columns =['timestamp','values'])
                    maxRespDf = respDf[respDf['values']== respDf['values'].max()].rename(columns = {'values':'maxValue'})
                    maxRespDf.insert(0, "metricName", scadaPoint['metricName'])    
                    maxRespDf.reset_index(drop=True, inplace=True)
                    
                    # fetch till now so far highest                 
                    scadametricSoFarHighDf = obj_scadaMetricSoFarHighFetch.fetchSoFarHighMeteric(scadaPoint['metricName'])
                    
                    #comparison(algo implementation)
                    if not scadametricSoFarHighDf.empty:
                        # return false if no changes in soFarhighest else return new sofarhighest object.
                        newSoFarHigheObj :InewSoFarHighObj = compareScadaMetric(maxRespDf, scadametricSoFarHighDf)

                        if newSoFarHigheObj:
                            isnewSoFarHighUpdationSuccess = obj_newSoFarHighInsertion.insertNewSoFarHigh(newSoFarHigheObj)
                            
            except Exception as err:
                print("error while fetching from scada api", err)
            finally:
                countLoopIter = countLoopIter +1
        currDate += dt.timedelta(days=1)

    numOfDays = (endDate-startDate).days

    #checking whether data is computed for each day or not
    if countLoopIter == (numOfDays+1)*len(scadaPoints):
        return True
    else:
        return False
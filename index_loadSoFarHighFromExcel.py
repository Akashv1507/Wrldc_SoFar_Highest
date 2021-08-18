import argparse
from datetime import datetime as dt, timedelta
from src.appConfig import getAppConfigDict
from src.loadSoFarHighFromExcel import LoadSoFarHighestExcel

appConfig = getAppConfigDict(sheetName='appConfig')

excelFilePath = appConfig['file_path'] + '\\So_Far_Highest.xlsx'
dbConStr = appConfig['con_string_mis_warehouse']

obj_loadSofarHigh = LoadSoFarHighestExcel(dbConStr, excelFilePath)
isLoadingSuccess = obj_loadSofarHigh.insertSoFarHigh()

if isLoadingSuccess:
    print("so far highest table loading successfull from excel file")
else:
    print("something went wrong !! please try again ")
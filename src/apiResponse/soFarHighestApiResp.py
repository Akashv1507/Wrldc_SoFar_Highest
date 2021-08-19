import cx_Oracle
import pandas as pd
import datetime as dt
from typing import List, Tuple, Union
from src.typeDefs.apiResponse import IapiResponse


class SoFarHighestApiResp():
    

    def __init__(self, con_string):
        """initialize connection string
        Args:
            con_string ([type]): connection string 
        """
        self.connString = con_string

    def toDesiredFormat(self, apiRespDf:pd.core.frame.DataFrame, dataSource:str)-> IapiResponse:

        if dataSource == 'SCADA_API':
            respObj:IapiResponse = {'soFarHighest': apiRespDf['SOFAR_HIGHEST'][0], 'soFarHighestTimestamp':str(apiRespDf['SOFAR_HIGHEST_TIMESTAMP'][0]), 'prevSoFarHighest': apiRespDf['PREV_SOFAR_HIGHEST'][0], 'prevSoFarHighestTimestamp':str(apiRespDf['PREV_SOFAR_HIGHEST_TIMESTAMP'][0])}
        elif dataSource == 'PSP_DB' :
            respObj:IapiResponse = {'soFarHighest': apiRespDf['SOFAR_HIGHEST'][0], 'soFarHighestTimestamp':str(apiRespDf['SOFAR_HIGHEST_TIMESTAMP'][0].date()), 'prevSoFarHighest': apiRespDf['PREV_SOFAR_HIGHEST'][0], 'prevSoFarHighestTimestamp':str(apiRespDf['PREV_SOFAR_HIGHEST_TIMESTAMP'][0].date())}
        # print(respObj)
        return respObj

    def fetchSoFarHighest(self, dataSource:str, metricName:str)->IapiResponse : 
        """api response

        Args:
            dataSource (str): SCADA_API/PSP_DB
            metricName (str): metric name like ['WR_DEM_MW', 'MAH_WIND_MW' etc]

        Returns:
            IapiResponse: IapiResponse
        """        

        try:
            connection = cx_Oracle.connect(self.connString)
        except Exception as err:
            print('error while creating a connection', err)
        else:
            try:
                cur = connection.cursor()
                cur.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS' ")

                fetch_sql = "select sofar_highest, sofar_highest_timestamp, prev_sofar_highest, prev_sofar_highest_timestamp from SoFar_Highest where metric_name =:metricName and datasource = :datasource"
                soFarHighApiRespDf = pd.read_sql(fetch_sql, params={'datasource':dataSource, 'metricName': metricName}, con=connection)               
                
            except Exception as err:
                print('error while creating a cursor', err)
            else:
                connection.commit()
        finally:
            cur.close()
            connection.close()

        respData:IapiResponse = self.toDesiredFormat(soFarHighApiRespDf, dataSource)
        return respData
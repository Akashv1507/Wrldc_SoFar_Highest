import pandas as pd
import datetime as dt
import cx_Oracle
from src.typeDefs.pspPoints import  IpspPoint

class PspMetricDataFetcher():

    def __init__(self, connStr:str ) -> None:
        """constructor

        Args:
            connStr (str): psp db connection string
        """        
        self.connString = connStr

    def todesiredFormat(self, pspMetricDataDf:pd.DataFrame, metricName:str )-> pd.DataFrame:
        """convert fetched data to desired format and rename columns

        Args:
            pspMetricDataDf (pd.DataFrame): fetched dataframe
            metricName (str): metric name (WR_DEM_MU, MAH_SOLAR_MU etc)

        Returns:
            pd.DataFrame: return df with columns ['METRIC_NAME', 'DATE_KEY', 'VALUE']
        """   
        # converting date to no 2021-08-18 to 20210818     
        pspMetricDataDf['DATE_KEY']= pd.to_datetime(pspMetricDataDf['DATE_KEY'], format="%Y%m%d")

        # inserting METRIC_NAME column with value metricName
        pspMetricDataDf.insert(0, "METRIC_NAME", metricName)

        #renaming column for consistency    
        pspMetricDataDf.rename(columns={pspMetricDataDf.columns[1]: 'DATE_KEY', pspMetricDataDf.columns[2]: 'VALUE'}, inplace=True)

        # finding maximum (done to handle case where data fetched for more than one date.)
        pspMetricDataDf = pspMetricDataDf[pspMetricDataDf['VALUE']== pspMetricDataDf['VALUE'].max()]
        # resetting index, so that 0th index will be desired value
        pspMetricDataDf.reset_index(drop=True, inplace=True)
        
        return pspMetricDataDf

    def fetchPspMetricData(self, start_date:dt.datetime, end_date:dt.datetime , pspPoint:IpspPoint)->pd.DataFrame:
        """fetch psp metric data from psp database

        Args:
            start_date (dt.datetime): startdat
            end_date (dt.datetime): enddaye
            pspPoint (IpspPoint): IpspPoint {metricName:str, strmetricFetchSql:str}

        Returns:
            pd.DataFrame: return df with columns ['METRIC_NAME', 'DATE_KEY', 'VALUE']
        """        
        
        # converting datetime obj to string and then integer, 2021-08-16-> 20210816
        numbStartDate = int(start_date.strftime('%Y%m%d'))
        numbEndDate = int(end_date.strftime('%Y%m%d'))
       
        try:   
            connection = cx_Oracle.connect(self.connString)
        except Exception as err:
            print('error while creating a connection', err)
        else:
            try:
                cur = connection.cursor()
                fetch_sql = pspPoint['metricFetchSql']
                pspMetricDataDf = pd.read_sql(fetch_sql, params={'start_date': numbStartDate, 'end_date': numbEndDate}, con=connection)
            except Exception as err:
                print('error while creating a cursor', err)
            else:
                connection.commit()
        finally:
            cur.close()
            connection.close()
        pspMetricData = self.todesiredFormat(pspMetricDataDf, pspPoint['metricName'])
        return pspMetricData
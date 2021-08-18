import pandas as pd
import datetime as dt
import cx_Oracle

class SoFarHighMetricFetch():

    def __init__(self, connStr:str ) -> None:
        """constructor

        Args:
            connStr (str): application db conn string
        """        
        self.connString = connStr

    def fetchSoFarHighMeteric(self, metricName: str)->pd.DataFrame:

        """fetch so far highest value corresponding to metric name

        Returns:
            pd.DataFrame: Dataframe with columns ['metric_name', 'sofar_highest_timestamp', 'sofar_highest']
        """        
        try:   
            connection = cx_Oracle.connect(self.connString)
        except Exception as err:
            print('error while creating a connection', err)
        else:
            try:
                cur = connection.cursor()
                cur.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS' ")
                fetch_sql = "select metric_name, sofar_highest_timestamp, sofar_highest from SoFar_Highest where metric_name =:metricName"
                soFarHighScadaMetricDf = pd.read_sql(fetch_sql, params={'metricName': metricName}, con=connection)
            except Exception as err:
                print('error while creating a cursor', err)
            else:
                connection.commit()
        finally:
            cur.close()
            connection.close()
        return soFarHighScadaMetricDf
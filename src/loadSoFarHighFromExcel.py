import pandas as pd
import cx_Oracle
import datetime as dt
from typing import List, Tuple, Dict


class LoadSoFarHighestExcel():
    

    def __init__(self, con_string: str, filePath:str) -> None:
        """initialize connection string
        Args:
            con_string ([type]): connection string 
            filePath(str):  so far highest excel file path
        """
        self.connString = con_string
        self.excelPath = filePath

    
    def toListOfTuple(self,df:pd.core.frame.DataFrame) ->Dict:
        """convert df to list of tuple

        Args:
            df (pd.core.frame.DataFrame): excel dataframe

        Returns:
        Dict(List[Tuple]): dictionary [(datasource:str, metricName: str, sofarHighest: float, soFarHighestTimestamp: str, prevSoFarHighest: float, prevSoFarHighestTimestamp: str)]
        """        
        soFarHighData:List[Tuple]= []
        soFarHighDataHistory:List[Tuple]= []
        for ind in df.index:
            tempTuple = (df['Datasource'][ind], df['Metric_Name'][ind], float(df['Sofar_Highest'][ind]), str(df['Sofar_Highest_Timestamp'][ind]), float(df['Prev_Sofar_Highest'][ind]), str(df['Prev_Sofar_Highest_Timestamp'][ind]) )
            soFarHighData.append(tempTuple)
            tempHistryTuple = (df['Datasource'][ind], df['Metric_Name'][ind], float(df['Sofar_Highest'][ind]), str(df['Sofar_Highest_Timestamp'][ind]))
            soFarHighDataHistory.append(tempHistryTuple)
        return {'soFarHighData':soFarHighData, 'soFarHighDataHistory':soFarHighDataHistory}

    def insertSoFarHigh(self) -> bool:
        """insert so far highest from excel

        Returns:
            bool: [description]
        """        
        soFarHighExcelDf = pd.read_excel(self.excelPath, parse_dates=['Sofar_Highest_Timestamp', 'Prev_Sofar_Highest_Timestamp'])

        #converting dataframe to list of tuples.
        soFarHighData = self.toListOfTuple(soFarHighExcelDf)

        
        # making list of tuple of parameter and entity_tag based on which deletion takes place before insertion of duplicate
        existingRows = [(x[0],x[1]) for x in soFarHighData['soFarHighData']]
        existingRowsHistory = [(x[0],x[1], x[3]) for x in soFarHighData['soFarHighDataHistory']]
        
        try:
            
            connection = cx_Oracle.connect(self.connString)
            isInsertionSuccess = True

        except Exception as err:
            print('error while creating a connection', err)
        else:

            try:
                cur = connection.cursor()
                try:
                    cur.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS' ")

                    del_sql = "DELETE FROM SoFar_Highest WHERE datasource = :1 and metric_name=:2"
                    cur.executemany(del_sql,existingRows)

                    del_sql = "DELETE FROM SoFar_Highest_History WHERE datasource = :1 and metric_name=:2 and sofar_highest_timestamp=:3"
                    cur.executemany(del_sql,existingRowsHistory)

                    insert_sql = "INSERT INTO SoFar_Highest(datasource,metric_name, sofar_highest, sofar_highest_timestamp, prev_sofar_highest, prev_sofar_highest_timestamp) VALUES(:1, :2, :3, :4, :5, :6)"
                    cur.executemany(insert_sql, soFarHighData['soFarHighData'])

                    insert_sql = "INSERT INTO SoFar_Highest_History(datasource, metric_name, sofar_highest, sofar_highest_timestamp) VALUES(:1, :2, :3, :4)"
                    cur.executemany(insert_sql, soFarHighData['soFarHighDataHistory'])

                except Exception as e:
                    print("error while insertion/deletion->", e)
                    isInsertionSuccess = False
            except Exception as err:
                print('error while creating a cursor', err)
                isInsertionSuccess = False
            else:
                connection.commit()
        finally:
            cur.close()
            connection.close()
        return isInsertionSuccess
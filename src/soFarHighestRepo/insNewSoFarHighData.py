import pandas as pd
import cx_Oracle
import datetime as dt
from typing import List, Tuple
from src.typeDefs.newSoFarHighObj import InewSoFarHighObj


class NewSoFarHighInsertion():
    

    def __init__(self, con_string: str) -> None:
        """initialize connection string
        Args:
            con_string ([str]): application db connection string 
        """
        self.connString = con_string 

    def insertNewSoFarHigh(self, newSoFarHighObj: InewSoFarHighObj) -> bool:
        """insert new so far high obj data

        Args:
            newSoFarHighObj (InewSoFarHighObj):InewSoFarHighObj-> {'newSoFarHighdata': newSoFarHighdata, 'newSoFarHighHistory': newSoFarHighHistory}

        Returns:
            bool: return true if insertion successfull else false
        """        
        
        # making list of tuple of datesource and metricName based on which deletion takes place before insertion of duplicate
        existingRows = [(x[0],x[1]) for x in newSoFarHighObj['newSoFarHighdata']]
        existingRowsHistory = [(x[0],x[1], x[3]) for x in newSoFarHighObj['newSoFarHighHistory']]
        
        try:
            
            connection = cx_Oracle.connect(self.connString)
            isInsertionSuccess = True

        except Exception as err:
            print('error while creating a connection', err)
        else:

            try:
                cur = connection.cursor()
               
                cur.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS' ")

                del_sql = "DELETE FROM SoFar_Highest WHERE datasource = :1 and metric_name=:2"
                cur.executemany(del_sql,existingRows)

                del_sql = "DELETE FROM SoFar_Highest_History WHERE datasource = :1 and metric_name=:2 and sofar_highest_timestamp=:3"
                cur.executemany(del_sql,existingRowsHistory)

                insert_sql = "INSERT INTO SoFar_Highest(datasource,metric_name, sofar_highest, sofar_highest_timestamp, prev_sofar_highest, prev_sofar_highest_timestamp) VALUES(:1, :2, :3, :4, :5, :6)"
                cur.executemany(insert_sql, newSoFarHighObj['newSoFarHighdata'])

                insert_sql = "INSERT INTO SoFar_Highest_History(datasource, metric_name, sofar_highest, sofar_highest_timestamp) VALUES(:1, :2, :3, :4)"
                cur.executemany(insert_sql, newSoFarHighObj['newSoFarHighHistory'])

            except Exception as err:
                print('error while creating a cursor', err)
                isInsertionSuccess = False
            else:
                connection.commit()
        finally:
            cur.close()
            connection.close()
        return isInsertionSuccess
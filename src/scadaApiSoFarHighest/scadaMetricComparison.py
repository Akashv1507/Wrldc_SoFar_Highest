import pandas as pd
import pandas as pd 
from src.typeDefs.newSoFarHighObj import InewSoFarHighObj

def compareScadaMetric(maxRespDf: pd.DataFrame, scadametricSoFarHighDf: pd.DataFrame )-> (InewSoFarHighObj or bool):    
    """ compare fetch metric data to availabe so far highest data, if fetched data greater than available so far highest return newSoFarHigh obj else false

    Args:
        maxRespDf (pd.DataFrame): max value from scada api
        scadametricSoFarHighDf (pd.DataFrame): so far high value for a metri name

    Returns:
        InewSoFarHighObj: InewSoFarHighObj
    """  
    
    if round(maxRespDf['maxValue'][0], 2)>scadametricSoFarHighDf['SOFAR_HIGHEST'][0]:
        # if sofar highest changed,  making new list of tuple for updating sofarhighest table 
        # (datasource, metricName, sofarHighest, sofarHighestTimestamp, prevSofarHighest, prevSofarHighestTimestamp)
        newSoFarHighdata = [('SCADA_API', scadametricSoFarHighDf['METRIC_NAME'][0], float(maxRespDf['maxValue'][0]), str(maxRespDf['timestamp'][0]), float(scadametricSoFarHighDf['SOFAR_HIGHEST'][0]), str(scadametricSoFarHighDf['SOFAR_HIGHEST_TIMESTAMP'][0]))]
        newSoFarHighHistory = [('SCADA_API', scadametricSoFarHighDf['METRIC_NAME'][0], float(maxRespDf['maxValue'][0]), str(maxRespDf['timestamp'][0]))]
        return {'newSoFarHighdata': newSoFarHighdata, 'newSoFarHighHistory': newSoFarHighHistory}
    else:
        return False
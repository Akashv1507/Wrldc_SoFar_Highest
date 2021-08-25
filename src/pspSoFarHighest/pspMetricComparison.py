import pandas as pd
import pandas as pd 
from src.typeDefs.newSoFarHighObj import InewSoFarHighObj

def comparePspMetric(pspMetricData: pd.DataFrame, pspMetricSoFarHighDf: pd.DataFrame )->(InewSoFarHighObj or bool):
    """compare fetch metric data to availabe so far highest data, if fetched data greater than available so far highest return newSoFarHigh obj else false
    Args:
        pspMetricData (pd.DataFrame): fetched psp df
        pspMetricSoFarHighDf (pd.DataFrame): fetched so dar high df

    Returns:
        InewSoFarHighObj/bool: InewSoFarHighObj/bool
    """

    if round(pspMetricData['VALUE'][0], 2)>pspMetricSoFarHighDf['SOFAR_HIGHEST'][0]:
        # if sofar highest changed,  making new list of tuple for updating sofarhighest table 
        # (datasource, metricName, sofarHighest, sofarHighestTimestamp, prevSofarHighest, prevSofarHighestTimestamp)
        newSoFarHighdata = [('PSP_DB', pspMetricSoFarHighDf['METRIC_NAME'][0], float(pspMetricData['VALUE'][0]), str(pspMetricData['DATE_KEY'][0]), float(pspMetricSoFarHighDf['SOFAR_HIGHEST'][0]), str(pspMetricSoFarHighDf['SOFAR_HIGHEST_TIMESTAMP'][0]))]
        newSoFarHighHistory = [('PSP_DB', pspMetricSoFarHighDf['METRIC_NAME'][0], float(pspMetricData['VALUE'][0]), str(pspMetricData['DATE_KEY'][0]))]
        return {'newSoFarHighdata': newSoFarHighdata, 'newSoFarHighHistory': newSoFarHighHistory}
    else:
        return False
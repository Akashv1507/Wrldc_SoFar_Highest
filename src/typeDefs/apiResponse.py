from typing import List, Tuple, TypedDict
import pandas as pd


class IapiResponse(TypedDict):
    metricName: str
    soFarHighest:float
    soFarHighestTimestamp:str
    prevSoFarHighest:float
    prevSoFarHighestTimestamp:str



from typing import List, Tuple, TypedDict
import pandas as pd


class IscadaPoint(TypedDict):
    metricName: str
    metricScadaId:str
    maxReasonabiltyLimit:float

class IlistScadaPoint():
    listScadaPoint: List[IscadaPoint]

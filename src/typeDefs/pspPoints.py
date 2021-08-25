from typing import List, Tuple, TypedDict
import pandas as pd


class IpspPoint(TypedDict):
    metricName: str
    metricFetchSql:str
    maxReasonabiltyLimit: float

class IlistPspPoint():
    listPspPoint: List[IpspPoint]

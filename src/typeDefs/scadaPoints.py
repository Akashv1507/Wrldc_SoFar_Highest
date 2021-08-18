from typing import List, Tuple, TypedDict
import pandas as pd


class IscadaPoint(TypedDict):
    metricName: str
    metricScadaId:str

class IlistScadaPoint():
    listScadaPoint: List[IscadaPoint]

##
# @file dataset.py
# @author Marián Tarageľ (xtarag01)
# @brief Wrapper for benchmark data

import pandas as pd

class Dataset:

    df: pd.DataFrame
    images: list
    labels: list
    name: str

    def __init__(self, name, df=None, images=None, labels=None) -> None:
        self.name = name
        self.df = df
        self.images = images
        self.labels = labels

    def __repr__(self) -> str:
        return self.name
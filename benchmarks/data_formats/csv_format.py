##
# @file csv_format.py
# @author Marián Tarageľ (xtarag01)

from .data_format import DataFormat
import dask.dataframe as dd
import pandas as pd

class Csv(DataFormat):

    format_name = "CSV"
    filetype = "csv"

    def __init__(self) -> None:
        self.filename = f"test.{self.filetype}"
        self.pathname = f"{self.filename}/*.part"

    def save(self, data_set, compression=None, complevel=None):
        data_set.to_csv(self.filename, index=False, compression={"method": compression, "level": complevel})

    def parallel_save(self, data_set, n):
        dask_df = dd.from_pandas(data_set, npartitions=n)
        dd.to_csv(dask_df, self.filename, index=False)

    def read(self, compression="infer") -> pd.DataFrame:
        return pd.read_csv(self.filename, compression=compression)

    def parallel_read(self) -> pd.DataFrame:
        return dd.read_csv(self.pathname).compute()
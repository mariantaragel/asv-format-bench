##
# @file parquet_format.py
# @author Marián Tarageľ (xtarag01)

from .data_format import DataFormat
import dask.dataframe as dd
import pandas as pd

class Parquet(DataFormat):

    format_name = "Parquet"
    filetype = "parquet"
    
    def __init__(self) -> None:
        self.filename = f"test.{self.filetype}"
        self.pathname = f"{self.filename}/part.*.{self.filetype}"

    def save(self, data_set, compression=None, complevel=None):
        data_set.to_parquet(self.filename, index=False, engine="pyarrow", compression=compression)

    def parallel_save(self, data_set, n):
        dask_df = dd.from_pandas(data_set, npartitions=n)
        dd.to_parquet(dask_df, self.filename, write_index=False, engine="pyarrow")

    def read(self) -> pd.DataFrame:
        return pd.read_parquet(self.filename)

    def parallel_read(self) -> pd.DataFrame:
        return dd.read_parquet(self.pathname).compute()

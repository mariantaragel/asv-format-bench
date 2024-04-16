##
# @file hdf5table_format.py
# @author Marián Tarageľ (xtarag01)

from .data_format import DataFormat
import dask.dataframe as dd
import pandas as pd
import dask

class Hdf5Table(DataFormat):

    format_name = "HDF5.table"
    filetype = "h5"

    def __init__(self) -> None:
        self.filename = f"test.{self.filetype}"
        self.pathname = f"{self.filename}.*.{self.filetype}"

    def save(self, data_set, compression="zlib", complevel=None):
        data_set.to_hdf(
            self.filename,
            index=False,
            key="data",
            format="table",
            complib=f"blosc:{compression}",
            complevel=complevel
        )

    def parallel_save(self, data_set, n):
        dask.config.set({"dataframe.convert-string": False})
        dask_df = dd.from_pandas(data_set, npartitions=n)
        dd.to_hdf(
            dask_df,
            f"{self.filename}.*.{self.filetype}",
            index=False,
            key="data",
            format="table",
            compute=True
        )

    def read(self) -> pd.DataFrame:
        return pd.read_hdf(self.filename, key="data")

    def parallel_read(self) -> pd.DataFrame:
        return dd.read_hdf(self.pathname, key="data").compute()
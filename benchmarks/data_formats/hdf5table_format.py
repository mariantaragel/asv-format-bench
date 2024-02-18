from .data_format import DataFormat
import pandas as pd
import dask.dataframe as dd

class Hdf5Table(DataFormat):

    format_name = "HDF5.table"
    filetype = "h5"
    
    complevel: int

    def __init__(self, data_set, compression="zlib", complevel=None) -> None:
        super().__init__(data_set, compression)
        self.filename = f"test.{self.filetype}"
        self.pathname = f"{self.filename}.*.{self.filetype}"
        self.complevel = complevel

    def save(self):
        self.data_set.to_hdf(
            self.filename,
            index=False,
            key="data",
            format="table",
            complib=self.compression,
            complevel=self.complevel
        )

    def parallel_save(self):
        dask_df = dd.from_pandas(self.data_set, npartitions=4)
        dd.to_hdf(
            dask_df,
            f"{self.filename}.*.{self.filetype}",
            index=False,
            key="data",
            format="table",
            compute=True
        )

    def read(self):
        pd.read_hdf(self.filename, key="data")

    def parallel_read(self):
        dd.read_hdf(self.pathname, key="data").compute()
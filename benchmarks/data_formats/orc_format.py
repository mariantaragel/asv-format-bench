from .data_format import DataFormat
import pandas as pd
import dask.dataframe as dd

class Orc(DataFormat):

    format_name = "ORC"
    filetype = "orc"
    
    def __init__(self) -> None:
        self.filename = f"test.{self.filetype}"
        self.pathname = f"{self.filename}/part.*.{self.filetype}"

    def save(self, data_set, compression="uncompressed"):
        data_set.to_orc(self.filename, index=False, engine_kwargs={"compression": compression})

    def parallel_save(self, data_set, n):
        dask_df = dd.from_pandas(data_set, npartitions=n)
        dd.to_orc(dask_df, self.filename, write_index=False, compute=True)

    def read(self):
        pd.read_orc(self.filename)

    def parallel_read(self):
        dd.read_orc(self.pathname).compute()
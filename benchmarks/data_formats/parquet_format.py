from .data_format import DataFormat
import pandas as pd
import dask.dataframe as dd

class Parquet(DataFormat):

    format_name = "Parquet"
    filetype = "parquet"
    
    def __init__(self, data_set, compression=None) -> None:
        super().__init__(data_set, compression)
        self.filename = f"test.{self.filetype}"
        self.pathname = f"{self.filename}/part.*.{self.filetype}"

    def save(self):
        self.data_set.to_parquet(self.filename, index=False, compression=self.compression)

    def parallel_save(self):
        dask_df = dd.from_pandas(self.data_set, npartitions=4)
        dd.to_parquet(dask_df, self.filename, write_index=False)

    def read(self):
        pd.read_parquet(self.filename)

    def parallel_read(self):
        dd.read_parquet(self.pathname).compute()
from .data_format import DataFormat
import pandas as pd
import dask.dataframe as dd

class Csv(DataFormat):

    format_name = "CSV"
    filetype = "csv"

    def __init__(self, data_set, compression=None) -> None:
        super().__init__(data_set, compression)
        self.filename = f'test.{self.filetype}'

    def save(self):
        self.data_set.to_csv(self.filename, index=False, compression=self.compression)

    def parallel_save(self):
        dask_df = dd.from_pandas(self.data_set, npartitions=4)
        dd.to_csv(dask_df, self.filename)

    def read(self):
        pd.read_csv(self.filename, compression=self.compression)

    def parallel_read(self):
        dd.read_csv(f"{self.filename}/*.part").compute()
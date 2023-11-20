from .data_format import DataFormat
import pandas as pd

class Parquet(DataFormat):

    format_name = "parquet"
    filetype = "parquet"
    save_params = {"index": False}
    read_params = {}

    def __init__(self, data_set) -> None:
        super().__init__(data_set)
        self.filename = f'test.{self.filetype}'

    def save(self):
        self.data_set.to_parquet(self.filename, **self.save_params)

    def read(self):
        pd.read_parquet(self.filename, **self.read_params)
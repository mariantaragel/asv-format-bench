from .data_format import DataFormat
import pandas as pd

class Csv(DataFormat):

    format_name = "csv"
    filetype = "csv"
    save_params = {"index": False}
    read_params = {}

    def __init__(self, data_set) -> None:
        super().__init__(data_set)
        self.filename = f'test.{self.filetype}'

    def save(self):
        self.data_set.to_csv(self.filename, **self.save_params)

    def read(self):
        pd.read_csv(self.filename, **self.read_params)
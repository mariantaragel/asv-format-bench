from .data_format import DataFormat
import pandas as pd

class Feather(DataFormat):

    format_name = "feather"
    filetype = "feather"
    save_params = {}
    read_params = {}

    def __init__(self, data_set) -> None:
        super().__init__(data_set)
        self.filename = f'test.{self.filetype}'

    def save(self):
        self.data_set.to_feather(self.filename, **self.save_params)

    def read(self):
        pd.read_feather(self.filename, **self.read_params)
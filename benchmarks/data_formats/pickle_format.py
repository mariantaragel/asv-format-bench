from .data_format import DataFormat
import pandas as pd

class Pickle(DataFormat):

    format_name = "pickle"
    filetype = "pkl"
    save_params = {}
    read_params = {}

    def __init__(self, data_set) -> None:
        super().__init__(data_set)
        self.filename = f'test.{self.filetype}'

    def save(self):
        self.data_set.to_pickle(self.filename, **self.save_params)

    def read(self):
        pd.read_pickle(self.filename, **self.read_params)
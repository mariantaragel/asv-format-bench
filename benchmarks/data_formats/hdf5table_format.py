from .data_format import DataFormat
import pandas as pd

class Hdf5Table(DataFormat):

    format_name = "hdf5.table"
    filetype = "h5"
    
    save_params: dict
    read_params: dict

    def __init__(self, data_set, save_params = {"index": False, "key": "data", "format": "table"}, read_params = {}) -> None:
        super().__init__(data_set)
        self.filename = f'test.{self.filetype}'
        self.save_params = save_params
        self.read_params = read_params

    def save(self):
        self.data_set.to_hdf(self.filename, **self.save_params)

    def read(self):
        pd.read_hdf(self.filename, **self.read_params)
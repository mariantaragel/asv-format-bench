from .data_format import DataFormat
import pandas as pd

class Feather(DataFormat):

    format_name = "Feather"
    filetype = "feather"

    compression_level: int

    def __init__(self, data_set, compression="uncompressed", compression_level=None) -> None:
        super().__init__(data_set, compression)
        self.filename = f"test.{self.filetype}"
        self.compression_level = compression_level

    def save(self):
        self.data_set.to_feather(self.filename, compression=self.compression, compression_level=self.compression_level)

    def read(self):
        pd.read_feather(self.filename, use_threads=False)
from .data_format import DataFormat
import pandas as pd

class Feather(DataFormat):

    format_name = "Feather"
    filetype = "feather"

    def __init__(self) -> None:
        self.filename = f"test.{self.filetype}"

    def save(self, data_set, compression="uncompressed"):
        if compression == "uncompressed":
            complevel = None
        else:
            complevel = 9
        data_set.to_feather(self.filename, compression=compression, compression_level=complevel)

    def read(self):
        pd.read_feather(self.filename, use_threads=False)
from .data_format import DataFormat
import pandas as pd

class Xml(DataFormat):

    format_name = "XML"
    filetype = "xml"

    complevel: int

    def __init__(self, data_set, compression=None, complevel=None) -> None:
        super().__init__(data_set, compression)
        self.filename = f"test.{self.filetype}"
        self.complevel = complevel

    def save(self):
        self.data_set.to_xml(self.filename, index=False, compression={"method": self.compression, "level": self.complevel})

    def read(self):
        pd.read_xml(self.filename, compression=self.compression)
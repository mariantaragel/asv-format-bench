from .data_format import DataFormat
import pandas as pd

class Xml(DataFormat):

    format_name = "XML"
    filetype = "xml"

    complevel: int

    def __init__(self, compression=None, complevel=None) -> None:
        super().__init__(compression)
        self.filename = f"test.{self.filetype}"
        self.complevel = complevel

    def save(self, data_set):
        data_set.to_xml(self.filename, index=False, compression={"method": self.compression, "level": self.complevel})

    def read(self):
        pd.read_xml(self.filename, compression=self.compression)
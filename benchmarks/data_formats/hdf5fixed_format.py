##
# @file hdf5fixed_format.py
# @author Marián Tarageľ (xtarag01)

from .data_format import DataFormat
import pandas as pd

class Hdf5Fixed(DataFormat):

    format_name = "HDF5.fixed"
    filetype = "h5"

    def __init__(self) -> None:
        self.filename = f"test.{self.filetype}"

    def save(self, data_set, compression="zlib", complevel=None):
        data_set.to_hdf(
            self.filename,
            index=False,
            key="data",
            format="fixed",
            complib=f"blosc:{compression}",
            complevel=complevel
        )

    def read(self) -> pd.DataFrame:
        return pd.read_hdf(self.filename)
from .data_format import DataFormat
import pyarrow.dataset as pyds
import pyarrow as pa
import pandas as pd
import shutil
import lance
import os

class Lance(DataFormat):

    format_name = "Lance"
    filetype = "lance"

    def __init__(self, compression=None) -> None:
        super().__init__(compression)
        self.filename = f"test.{self.filetype}"

    def save(self, data_set: pd.DataFrame):
        uri = "data.parquet"
        if os.path.exists(uri):
            shutil.rmtree(uri)
        if os.path.exists(self.filename):
            shutil.rmtree(self.filename)

        tbl = pa.Table.from_pandas(data_set)

        pyds.write_dataset(tbl, uri, format="parquet")

        parquet = pyds.dataset(uri, format="parquet")
        lance.write_dataset(parquet, self.filename)

    def read(self) -> pd.DataFrame:
        return lance.dataset(self.filename).to_table().to_pandas()

    def remove(self):
        shutil.rmtree(self.filename)
        shutil.rmtree("tmp/data.parquet")
    
    def size(self):
        size = 0
        for path, dirs, files in os.walk(self.filename):
            for f in files:
                fp = os.path.join(path, f)
                size += os.path.getsize(fp)
        return size
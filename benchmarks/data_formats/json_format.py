from .data_format import DataFormat
import dask.dataframe as dd
import pandas as pd

class Json(DataFormat):

    format_name = "JSON"
    filetype = "jsonl"

    complevel: int

    def __init__(self, compression=None, complevel=None) -> None:
        super().__init__(compression)
        self.filename = f"test.{self.filetype}"
        self.pathname = f"{self.filename}/*.part"
        self.complevel = complevel

    def save(self, data_set):
        data_set.to_json(
            self.filename,
            orient="records",
            lines=True,
            index=False,
            compression={"method": self.compression, "level": self.complevel}
        )

    def parallel_save(self, data_set, n):
        dask_df = dd.from_pandas(data_set, npartitions=n)
        dd.to_json(dask_df, self.filename, orient="records", lines=True, index=False)

    def read(self):
        pd.read_json(self.filename, lines=True, compression=self.compression)

    def parallel_read(self):
        dd.read_json(self.pathname).compute()
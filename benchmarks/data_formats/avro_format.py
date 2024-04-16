##
# @file avro_format.py
# @author Marián Tarageľ (xtarag01)

from fastavro import writer, reader, parse_schema
from .data_format import DataFormat
import pandas as pd

class Avro(DataFormat):

    format_name = "Avro"
    filetype = "avro"

    def __init__(self) -> None:
        self.filename = f"test.{self.filetype}"

    def save(self, data_set: pd.DataFrame, compression=None):
        schema = self.build_schema(data_set, False)
        records = data_set.to_dict(orient="records")

        parsed_schema = parse_schema(schema)

        with open(self.filename, "wb") as out:
            writer(out, parsed_schema, records)

    def read(self) -> pd.DataFrame:
        with open(self.filename, "rb") as fo:
            records = [record for record in reader(fo)]
        return pd.DataFrame.from_records(records)

    @staticmethod
    def build_schema(df: pd.DataFrame, index: bool) -> dict[str, any]:
        fields = []
        
        if index:
            index_field = {"name": df.index.name, "type": Avro.pandas_dtype_to_avro_dtype(df.index.dtype)}
            fields.append(index_field)

        for type, col in zip(df.dtypes, df.columns):
            new_field = {"name": col, "type": Avro.pandas_dtype_to_avro_dtype(type)}
            fields.append(new_field)

        schema = {
            'name': 'data',
            'type': 'record',
            'fields': fields
        }

        return schema
    
    @staticmethod
    def pandas_dtype_to_avro_dtype(dtype: str) -> (str | None):
        if dtype == "object":
            return "string"
        elif dtype == "int64":
            return "long"
        elif dtype == "float64":
            return "double"
        elif dtype == "bool":
            return "boolean"
        else:
            return None
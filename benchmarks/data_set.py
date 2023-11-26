import pandas as pd
from .gen_dtype import GenDtype
from .data_formats import Csv, Json, Xml, Hdf5Fixed, Hdf5Table, Parquet, Feather, Orc, Pickle, Excel


class DataSet:

    def gen_data_set(
            entries: int,
            int_cols: int,
            float_cols: int,
            bool_cols: int,
            str_cols: int,
            nan_ratio: float,
            str_fixed: int
        ) -> pd.DataFrame:
        gd = GenDtype()

        num_of_cols = int_cols + float_cols + bool_cols + str_cols
        cols = [f"col{i}" for i in range(num_of_cols)]

        int_params = {"low": 0, "high": 100}
        data_int = gd.gen_cols(int_cols, entries, "int", nan_ratio, int_params)

        float_params = {"low": 0, "high": 100}
        data_float = gd.gen_cols(float_cols, entries, "float", nan_ratio, float_params)

        bool_params = {}
        data_bool = gd.gen_cols(bool_cols, entries, "bool", nan_ratio, bool_params)

        data_str = []
        if str_fixed:
            str_fix_params = {"length": 10}
            data_str = gd.gen_cols(str_cols, entries, "str_fix", nan_ratio, str_fix_params)
        else:
            str_var_params = {"low": 0, "high": 10}
            data_str = gd.gen_cols(str_cols, entries, "str_var", nan_ratio, str_var_params)

        data = dict(zip(cols, data_int + data_float + data_bool + data_str))
        return pd.DataFrame(data)

    def get_data_formats(ds):
        return [
            Csv(ds),
            Json(ds),
            Xml(ds),
            Hdf5Fixed(ds),
            Hdf5Table(ds),
            Parquet(ds),
            Feather(ds),
            Orc(ds),
            Pickle(ds),
            Excel(ds),
        ]
    
    data_set_1 = gen_data_set(10_000, 1, 1, 0, 0, 0, True)
    data_set_2 = gen_data_set(10_000, 1, 0, 0, 1, 0, True)
    data_set_3 = gen_data_set(10_000, 0, 0, 1, 1, 0, True)

import pandas as pd
from .gen_dtype import GenDtype


class DataSet:

    def __repr__(self) -> str:
        return "Data set"

    def __str__(self) -> str:
        return "DS"

    def gen_data_set(
            entries: int,
            int_cols: int,
            float_cols: int,
            bool_cols: int,
            str_cols: int,
            nan_ratio: float,
            str_fixed: bool
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
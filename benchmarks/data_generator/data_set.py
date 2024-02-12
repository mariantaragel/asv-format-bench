import pandas as pd
from .gen_dtype import GenDtype


class DataSet:

    def gen_data_set(
            entries: int,
            int_cols: int,
            float_cols: int,
            bool_cols: int,
            str_fixed_cols: int,
            str_var_cols: int
        ) -> pd.DataFrame:
        gd = GenDtype()

        num_of_cols = int_cols + float_cols + bool_cols + str_fixed_cols + str_var_cols
        cols = [f"col{i}" for i in range(num_of_cols)]

        data_int = [gd.gen_int_col(0, 100, entries) for i in range(int_cols)]
        data_float = [gd.gen_float_col(0, 100, entries) for i in range(float_cols)]
        data_bool = [gd.gen_bool_col(entries) for i in range(bool_cols)]
        data_str_fixed = [gd.gen_fixed_str_col(10, entries) for i in range(str_fixed_cols)]
        data_str_var = [gd.gen_var_str_col(0, 10, entries) for i in range(str_var_cols)]

        data = dict(zip(cols, data_int + data_float + data_bool + data_str_fixed + data_str_var))
        
        return pd.DataFrame(data)
import pandas as pd
from .gen_dtype import GenDtype as gd
from .data_formats import Csv, Json, Xml, Hdf5Fixed, Hdf5Table, Parquet, Feather, Orc, Pickle, Excel

class Common:

    def gen_data_set(entries: int, int_cols: int, float_cols: int, str_cols: int, bool_cols: int, str_len: any) -> pd.DataFrame:
        num_of_cols = int_cols + float_cols + str_cols + bool_cols
        cols = [f"col{i}" for i in range(num_of_cols)]

        data_int = [gd.gen_int(0, 100, entries) for i in range(int_cols)]
        data_float = [gd.gen_float(0, 100, entries) for i in range(float_cols)]
        data_bool = [gd.gen_bool(entries) for i in range(bool_cols)]
        if str_len == gd.RAND_STR_LEN:
            data_str = [gd.gen_str_v(1, 10, entries) for i in range(str_cols)]
        elif str_len == gd.FIX_STR_LEN:
            data_str = [gd.gen_str_f(str_len, entries) for i in range(str_cols)]
        else:
            data_str = []

        data = dict(zip(cols, data_int + data_float + data_str + data_bool))
        
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
            Excel(ds)
        ]
    
    data_set_1 = gen_data_set(10_000, 1, 0, 0, 0, gd.NO_STR_COLS)
    data_set_2 = gen_data_set(10_000, 0, 1, 0, 0, gd.NO_STR_COLS)
    data_set_3 = gen_data_set(10_000, 0, 0, 1, 0, gd.RAND_STR_LEN)
    data_set_4 = gen_data_set(10_000, 0, 0, 0, 1, gd.NO_STR_COLS)

from .data_generator import DataSet
from .data_formats import Csv, Json, Xml, Hdf5Fixed, Hdf5Table, Parquet, Feather, Orc, Pickle, Excel
from .base import BaseBenchmark

class Uncompressed(BaseBenchmark):

    def __init__(self) -> None: 
        ds = DataSet.gen_data_set(
            entries=10_000,
            int_cols=1,
            float_cols=1,
            bool_cols=1,
            str_fixed_cols=1,
            str_var_cols=1
        )
        self.params = [
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

    def setup(self, format):
        format.save()

    def time_save(self, format):
        format.save()

    def track_size(self, format):
        return format.size()
    
    def time_read(self, format):
        format.read()

    def peakmem_save(self, format):
        format.save()

    def peakmem_read(self, format):
        format.read()

    time_save.pretty_name = "Saving time"
    time_read.pretty_name = "Reading time"

    track_size.pretty_name = "Total size"
    peakmem_save.pretty_name = "Peak Memory Saving"
    peakmem_read.pretty_name = "Peak Memory Reading"

    time_save.benchmark_name = "Uncompressed.time_save"
    time_read.benchmark_name = "Uncompressed.time_read"

    track_size.benchmark_name = "Uncompressed.track_size"
    peakmem_save.benchmark_name = "Uncompressed.peakmem_save"
    peakmem_read.benchmark_name = "Uncompressed.peakmem_read"
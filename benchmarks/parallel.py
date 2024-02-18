from .data_generator import DataSet
from .data_formats import Csv, Json, Hdf5Table, Parquet, Orc
from .base import BaseBenchmark
import dask

class Parallel(BaseBenchmark):
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
            Hdf5Table(ds),
            Parquet(ds),
            Orc(ds)
        ]

    def setup(self, format):
        dask.config.set({"dataframe.convert-string": False})
        format.parallel_save()

    def time_save(self, format):
        format.parallel_save()

    def track_size(self, format):
        return format.size_all_files()
    
    def time_read(self, format):
        format.parallel_read()

    def peakmem_save(self, format):
        format.parallel_save()

    def peakmem_read(self, format):
        format.parallel_read()

    time_save.pretty_name = "Saving time"
    time_read.pretty_name = "Reading time"

    track_size.pretty_name = "Total size"
    peakmem_save.pretty_name = "Peak Memory Saving"
    peakmem_read.pretty_name = "Peak Memory Reading"

    time_save.benchmark_name = "Parallel.time_save"
    time_read.benchmark_name = "Parallel.time_read"

    track_size.benchmark_name = "Parallel.track_size"
    peakmem_save.benchmark_name = "Parallel.peakmem_save"
    peakmem_read.benchmark_name = "Parallel.peakmem_read"
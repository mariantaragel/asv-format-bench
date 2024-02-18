from .data_generator import DataSet
from .data_formats import Hdf5Fixed, Hdf5Table, Parquet, Feather, Orc
from .base import BaseBenchmark

class Compressed(BaseBenchmark):

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
            Hdf5Fixed(ds, "blosc:lz4", 9),  # blosc:{lz4, lz4hc, zstd, snappy, zlib, blosclz}, zlib, lzo, bzip2
            Hdf5Table(ds, "blosc:lz4", 9),  # blosc:{lz4, lz4hc, zstd, snappy, zlib, blosclz}, zlib, lzo, bzip2
            Parquet(ds, "lz4"),             # lz4, zstd, snappy, gzip, brotli
            Feather(ds, "lz4", 9),          # lz4, zstd
            Orc(ds, "lz4"),                 # lz4, sztd, snappy, zlib
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

    time_save.benchmark_name = "Compressed.time_save"
    time_read.benchmark_name = "Compressed.time_read"

    track_size.benchmark_name = "Compressed.track_size"
    peakmem_save.benchmark_name = "Compressed.peakmem_save"
    peakmem_read.benchmark_name = "Compressed.peakmem_read"
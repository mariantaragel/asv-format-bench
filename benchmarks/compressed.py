from .data_generator import DataSet
from .data_formats import Csv, Json, Xml, Hdf5Fixed, Hdf5Table, Parquet, Feather, Orc, Pickle, Excel
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
            Csv(ds, {"method": "gzip", "compresslevel": 9}), # zip, gzip, bz2, zstd, xz, tar
            Json(ds, {"method": "gzip", "compresslevel": 9}), # zip, gzip, bz2, zstd, xz, tar
            Xml(ds, {"method": "gzip", "compresslevel": 9}), # zip, gzip, bz2, zstd, xz, tar
            Hdf5Fixed(ds, "zlib", 9), # zlib, lzo, bzip2, blosc:{blosclz, lz4, lz4hc, snappy, zlib, zstd}
            Hdf5Table(ds, "zlib", 9), # zlib, lzo, bzip2, blosc:{blosclz, lz4, lz4hc, snappy, zlib, zstd}
            Parquet(ds, "gzip") # snappy, gzip, brotli, lz4, zstd
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
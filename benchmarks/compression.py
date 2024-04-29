##
# @file compression.py
# @author Marián Tarageľ (xtarag01)

from .data_formats import Hdf5Table, Parquet, Feather, Orc
from .data_generator import Generator
from .base import BaseBenchmark

class Compression(BaseBenchmark):
    """Compression benchmark suite"""

    param_names = ["Data format", "Dataset", "Compression", "Compression level"]
    timeout = 140

    ds = Generator.gen_dataset("eq", 1_000_000, 2, 2, 2, 2, 0, 0)

    def __init__(self) -> None:
        self.params = ([
            Hdf5Table(), # blosc:{lz4, lz4hc, zstd, snappy, zlib, blosclz}, zlib, lzo, bzip2
            Parquet(),   # lz4, zstd, snappy, gzip, brotli
            Feather(),   # lz4, zstd
            Orc(),       # lz4, sztd, snappy, zlib
        ], [self.ds], ["lz4", "zstd"], [1])

    def setup(self, format, ds, compression, complevel):
        """Benchmark setup"""
        format.save(ds.df, compression, complevel)

    def time_save(self, format, ds, compression, complevel):
        """Run compression benchmark save time"""
        format.save(ds.df, compression, complevel)

    def track_size(self, format, ds, compression, complevel):
        """Run compression benchmark total size"""
        return format.size()
    
    def time_read(self, format, ds, compression, complevel):
        """Run compression benchmark read time"""
        format.read()

    time_save.pretty_name = "Saving time"
    time_read.pretty_name = "Reading time"
    track_size.pretty_name = "Total size"

    time_save.benchmark_name = "Compression.time_save"
    time_read.benchmark_name = "Compression.time_read"
    track_size.benchmark_name = "Compression.track_size"
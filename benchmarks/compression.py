from .data_formats import Hdf5Fixed, Hdf5Table, Parquet, Feather, Orc
from .data_generator import Generator
from .base import BaseBenchmark

class Compression(BaseBenchmark):

    param_names = ["Data format", "Compression"]

    ds = Generator.gen_data_set("ds", 1000, 1, 1, 0, 1, 0, 0)

    def __init__(self) -> None:
        self.params = ([
            Hdf5Fixed(), # blosc:{lz4, lz4hc, zstd, snappy, zlib, blosclz}, zlib, lzo, bzip2
            Hdf5Table(), # blosc:{lz4, lz4hc, zstd, snappy, zlib, blosclz}, zlib, lzo, bzip2
            Parquet(),   # lz4, zstd, snappy, gzip, brotli
            Feather(),   # lz4, zstd
            Orc(),       # lz4, sztd, snappy, zlib
        ], ["lz4", "zstd"])

    def setup(self, format, compression):
        format.save(self.ds.df, compression)

    def time_save(self, format, compression):
        format.save(self.ds.df, compression)

    def track_size(self, format, compression):
        return format.size()
    
    def time_read(self, format, compression):
        format.read()

    def peakmem_save(self, format, compression):
        format.save(self.ds.df, compression)

    def peakmem_read(self, format, compression):
        format.read()

    time_save.pretty_name = "Saving time"
    time_read.pretty_name = "Reading time"

    track_size.pretty_name = "Total size"
    peakmem_save.pretty_name = "Peak Memory Saving"
    peakmem_read.pretty_name = "Peak Memory Reading"

    time_save.benchmark_name = "Compression.time_save"
    time_read.benchmark_name = "Compression.time_read"

    track_size.benchmark_name = "Compression.track_size"
    peakmem_save.benchmark_name = "Compression.peakmem_save"
    peakmem_read.benchmark_name = "Compression.peakmem_read"
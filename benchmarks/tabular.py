##
# @file tabular.py
# @author Marián Tarageľ (xtarag01)

from .data_formats import Csv, Json, Xml, Hdf5Fixed, Hdf5Table, Parquet, Feather, Orc, Pickle, Excel, Lance, Avro
from .data_generator import Generator
from .base import BaseBenchmark

class Tabular(BaseBenchmark):
    """Tabular benchmark suite"""

    param_names = ["Data format", "Dataset"]
    timeout = 500

    ds1 = Generator.gen_dataset("eq", 1_000_000, 2, 2, 2, 2, 0, 0)
    ds2 = Generator.gen_dataset("int", 1_000_000, 5, 1, 1, 1, 0, 0)
    ds3 = Generator.gen_dataset("float", 1_000_000, 1, 5, 1, 1, 0, 0)
    ds4 = Generator.gen_dataset("bool", 1_000_000, 1, 1, 5, 1, 0, 0)
    ds5 = Generator.gen_dataset("str", 1_000_000, 1, 1, 1, 5, 0, 0)

    def __init__(self) -> None: 
        self.params = ([Csv(), Json(), Xml(), Hdf5Fixed(), Hdf5Table(), Parquet(),
                        Feather(), Orc(), Pickle(), Excel(), Lance(), Avro()],
                       [self.ds1, self.ds2, self.ds3, self.ds4, self.ds5])

    def setup(self, format, ds):
        """Benchmark setup"""
        format.save(ds.df)

    def time_save(self, format, ds):
        """Run tabular benchmark save time"""
        format.save(ds.df)

    def track_size(self, format, ds):
        """Run tabular benchmark total size"""
        return format.size()
    
    def time_read(self, format, ds):
        """Run tabular benchmark read time"""
        format.read()

    time_save.pretty_name = "Saving time"
    time_read.pretty_name = "Reading time"
    track_size.pretty_name = "Total size"

    time_save.benchmark_name = "Tabular.time_save"
    time_read.benchmark_name = "Tabular.time_read"
    track_size.benchmark_name = "Tabular.track_size"
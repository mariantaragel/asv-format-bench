from .data_formats import Csv, Json, Xml, Hdf5Fixed, Hdf5Table, Parquet, Feather, Orc, Pickle, Excel, Lance, Avro
from .data_generator import Generator
from .base import BaseBenchmark

class Tabular(BaseBenchmark):

    param_names = ["Data format", "Dataset"]

    ds1 = Generator.gen_dataset("int", 1000, 1, 0, 0, 0, 0, 0)
    ds2 = Generator.gen_dataset("float", 1000, 0, 1, 0, 0, 0, 0)

    def __init__(self) -> None: 
        self.params = ([Csv(), Json(), Xml(), Hdf5Fixed(), Hdf5Table(), Parquet(),
                       Feather(), Orc(), Pickle(), Excel(), Lance(), Avro()],
                       [self.ds1, self.ds2])

    def setup(self, format, ds):
        format.save(ds.df)

    def time_save(self, format, ds):
        format.save(ds.df)

    def track_size(self, format, ds):
        return format.size()
    
    def time_read(self, format, ds):
        format.read()

    def peakmem_save(self, format, ds):
        format.save(ds.df)

    def peakmem_read(self, format, ds):
        format.read()

    time_save.pretty_name = "Saving time"
    time_read.pretty_name = "Reading time"

    track_size.pretty_name = "Total size"
    peakmem_save.pretty_name = "Peak Memory Saving"
    peakmem_read.pretty_name = "Peak Memory Reading"

    time_save.benchmark_name = "Tabular.time_save"
    time_read.benchmark_name = "Tabular.time_read"

    track_size.benchmark_name = "Tabular.track_size"
    peakmem_save.benchmark_name = "Tabular.peakmem_save"
    peakmem_read.benchmark_name = "Tabular.peakmem_read"
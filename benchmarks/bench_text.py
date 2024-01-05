from .data_generator import DataSet
from .data_formats import Csv, Json, Xml
from .base import BaseBenchmark


class SimpleDs(BaseBenchmark):

    def __init__(self) -> None: 
        ds = DataSet.gen_data_set(10_000, 1, 0, 0, 1, 0, True)
        self.params = [Csv(ds), Json(ds), Xml(ds)]

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

    time_save.benchmark_name = "Timing.time_save"
    time_read.benchmark_name = "Timing.time_read"

    track_size.benchmark_name = "Memory usage.track_size"
    peakmem_save.benchmark_name = "Memory usage.peakmem_save"
    peakmem_read.benchmark_name = "Memory usage.peakmem_read"


class Compression(BaseBenchmark):

    def __init__(self) -> None:
        ds = DataSet.gen_data_set(10_000, 1, 1, 1, 1, 0, False)
        self.params = [Csv(ds), Csv(ds, {"index": False, "compression": "gzip"}, {"compression": "gzip"}),
                       Json(ds), Json(ds, {"orient": "values", "compression": "gzip"}, {"compression": "gzip"}),
                       Xml(ds), Xml(ds, {"index": False, "compression": "gzip"}, {"compression": "gzip"})]

    def setup(self, format):
        format.save()

    def time_save(self, format):
        format.save()

    def track_size(self, format):
        return format.size()
    
    def time_read(self, format):
        format.read()

    time_save.pretty_name = "Saving time"
    track_size.pretty_name = "Total size"
    time_read.pretty_name = "Reading time"

    time_save.benchmark_name = "Compression.time_save"
    track_size.benchmark_name = "Compression.track_size"
    time_read.benchmark_name = "Compression.time_read"
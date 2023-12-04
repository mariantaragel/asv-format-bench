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


class ComplexDs(BaseBenchmark):

    def __init__(self) -> None: 
        ds = DataSet.gen_data_set(10_000, 2, 2, 2, 2, 0, False)
        self.params = [Csv(ds), Json(ds), Xml(ds)]

    def setup(self, format):
        format.save()

    def time_save(self, format):
        format.save()

    def track_size(self, format):
        return format.size()
    
    def time_read(self, format):
        format.read()


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
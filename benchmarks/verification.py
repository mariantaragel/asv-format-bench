from .common import Common
from .base import BaseBenchmark

class Save(BaseBenchmark):

    def __init__(self) -> None:
        self.params = Common.get_data_formats(Common.data_set_3)
        
    def time_save(self, format):
        format.save()
        

class Read(BaseBenchmark):

    def __init__(self) -> None:
        self.params = Common.get_data_formats(Common.data_set_3)

    def setup(self, format) -> None:
        format.save()
        
    def time_read(self, format):
        format.read()
        

class Size(BaseBenchmark):

    def __init__(self) -> None:
        self.params = Common.get_data_formats(Common.data_set_3)

    def setup(self, format):
        format.save()
        
    def track_size(self, format):
        return format.size()
        
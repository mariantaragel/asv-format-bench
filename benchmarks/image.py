from .image_storages import PngImage, Base64String, Hdf5Image, ParquetImage, Sqlite, LmdbImage
from .data_generator import Generator
from .base import BaseBenchmark

class Image(BaseBenchmark):

    param_names = ["Data format", "Dataset"]
    timeout = 2200

    cifar = Generator.load_cifar_10(50_000)

    def __init__(self) -> None:
        self.params = ([PngImage(), Base64String(), Hdf5Image(),
                       ParquetImage(), Sqlite(), LmdbImage()],
                       [self.cifar])

    def setup(self, format, ds):
        format.save(ds.images, ds.labels)

    def time_save(self, format, ds):
        format.save(ds.images, ds.labels)

    def time_read(self, format, ds):
        format.read()

    def track_size(self, format, ds):
        return format.size()

    time_save.pretty_name = "Saving time"
    time_read.pretty_name = "Reading time"
    track_size.pretty_name = "Total size"

    time_save.benchmark_name = "Image.time_save"
    time_read.benchmark_name = "Image.time_read"
    track_size.benchmark_name = "Image.track_size"
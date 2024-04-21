# from .data_formats import Csv, Json, Hdf5Table, Parquet, Orc
# from .data_generator import Generator
# from .base import BaseBenchmark

# class Parallel(BaseBenchmark):

#     param_names = ["Data format", "Partitions"]

#     ds = Generator.gen_dataset("ds", 1000, 1, 1, 0, 1, 0, 0)

#     def __init__(self) -> None:
#         self.params = ([Csv(), Json(), Hdf5Table(), Parquet(), Orc()], [1, 2, 4])

#     def setup(self, format, n):
#         format.parallel_save(self.ds.df, n)

#     def time_save(self, format, n):
#         format.parallel_save(self.ds.df, n)

#     def track_size(self, format, n):
#         return format.size_all_files()
    
#     def time_read(self, format, n):
#         format.parallel_read()

#     def peakmem_save(self, format, n):
#         format.parallel_save(self.ds.df, n)

#     def peakmem_read(self, format, n):
#         format.parallel_read()

#     time_save.pretty_name = "Saving time"
#     time_read.pretty_name = "Reading time"

#     track_size.pretty_name = "Total size"
#     peakmem_save.pretty_name = "Peak Memory Saving"
#     peakmem_read.pretty_name = "Peak Memory Reading"

#     time_save.benchmark_name = "Parallel.time_save"
#     time_read.benchmark_name = "Parallel.time_read"

#     track_size.benchmark_name = "Parallel.track_size"
#     peakmem_save.benchmark_name = "Parallel.peakmem_save"
#     peakmem_read.benchmark_name = "Parallel.peakmem_read"
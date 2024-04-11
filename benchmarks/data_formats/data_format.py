from .benchmark_utils import remove_file, size_of_file, size_all_files, remove_all_files

class DataFormat:

    filename: str
    pathname: str
    compression: any

    def __init__(self, compression) -> None:
        self.compression = compression
        self.pathname = None

    def __repr__(self) -> str:
        return self.format_name

    def save(self):
        pass

    def parallel_save(self):
        pass

    def read(self):
        pass

    def parallel_read(self):
        pass

    def remove(self):
        remove_file(self.filename)

    def remove_all_files(self):
        remove_all_files(self.pathname, self.filename)

    def size(self):
        return size_of_file(self.filename)
    
    def size_all_files(self):
        return size_all_files(self.pathname)
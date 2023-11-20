from .benchmark_utils import remove_file, size_of_file

class DataFormat:

    data_set: any
    filename: str

    def __init__(self, data_set) -> None:
        self.data_set = data_set

    def save(self):
        pass

    def read(self):
        pass

    def remove(self):
        remove_file(self.filename)

    def size(self):
        return size_of_file(self.filename)

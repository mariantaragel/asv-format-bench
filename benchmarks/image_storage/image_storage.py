from .benchmark_utils import remove_file, size_of_file

class ImageStorage:

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return self.format_name

    def save(self):
        pass

    def read(self):
        pass

    def size(self):
        return size_of_file(self.filename)

    def remove(self):
        remove_file(self.filename)
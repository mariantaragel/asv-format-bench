##
# @file data_format.py
# @author Marián Tarageľ (xtarag01)
# @brief Base class for all data formats

from .file_utils import FileUtils

class DataFormat:

    filename: str
    pathname: str

    def __init__(self) -> None:
        self.pathname = None

    def __repr__(self) -> str:
        return self.format_name

    def save(self, data_set, compression=None):
        """
        Save dataset to a data format

        data_set : dataset to save
        compression : compression code to use
        """
        pass

    def parallel_save(self, data_set, n):
        """
        Save dataset with more workers

        data_set : dataset to save
        n : number of partitions
        """
        pass

    def read(self):
        """Read tabular data back from data format to pandas.DataFrame"""
        pass

    def parallel_read(self):
        """Read tabular data back from data format to pandas.DataFrame"""
        pass

    def remove(self):
        """Remove created file"""
        FileUtils.remove_file(self.filename)

    def remove_all_files(self):
        """Remove more created files"""
        FileUtils.remove_all_files(self.pathname, self.filename)

    def size(self):
        """Get the total size of a file"""
        return FileUtils.size_of_file(self.filename)
    
    def size_all_files(self):
        """Get the total size of more files"""
        return FileUtils.size_all_files(self.pathname)
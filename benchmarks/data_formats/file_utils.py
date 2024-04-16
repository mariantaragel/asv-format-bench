##
# @file file_utils.py
# @author Marián Tarageľ (xtarag01)
# @brief Class with utilities to manipulate with files

import glob
import os

class FileUtils:

    @staticmethod
    def size_of_file(filename: str) -> int:
        return os.path.getsize(filename)

    @staticmethod
    def size_all_files(pathname: str) -> int:
        files = glob.glob(pathname)
        
        total_size = 0
        for filename in files:
            total_size += os.path.getsize(filename)
        
        return total_size

    @staticmethod
    def remove_file(filename: str):
        if os.path.exists(filename):
            os.remove(filename)

    @staticmethod
    def remove_all_files(pathname: str, directory: str):
        files = glob.glob(pathname)

        for filename in files:
            if os.path.exists(filename):
                os.remove(filename)

        os.rmdir(directory)
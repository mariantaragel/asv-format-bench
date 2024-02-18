import os
import glob

def size_of_file(filename: str) -> int:
    return os.path.getsize(filename)

def size_all_files(pathname: str) -> int:
    files = glob.glob(pathname)
    
    total_size = 0
    for filename in files:
        total_size += size_of_file(filename)
    
    return total_size

def remove_file(filename: str):
    if os.path.exists(filename):
        os.remove(filename)
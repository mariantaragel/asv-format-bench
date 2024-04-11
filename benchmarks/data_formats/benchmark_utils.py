from pathlib import Path
import glob
import os

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

def remove_all_files(pathname: str, directory=None):
    files = glob.glob(pathname)

    for filename in files:
        remove_file(filename)

    if directory:
        os.rmdir(directory)

def setup():
    Path("./tmp").mkdir(exist_ok=True)

def teardown():
    Path("./tmp").rmdir()
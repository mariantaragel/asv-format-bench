from pathlib import Path
import resource
import timeit
import glob
import os

def setup():
    Path("./tmp").mkdir(exist_ok=True)

def teardown():
    Path("./tmp").rmdir()

def measure_time(code: callable) -> float:
    return timeit.timeit(code, number=1)

def get_peak_memory() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

def size_of_file(filename: str) -> int:
    return os.path.getsize(filename)

def size_all_files(pathname: str) -> int:
    files = glob.glob(pathname)
    
    total_size = 0
    for filename in files:
        total_size += size_of_file(filename)
    
    return total_size

def remove_all_files(pathname: str, directory=None):
    files = glob.glob(pathname)

    for filename in files:
        remove_file(filename)

    if directory:
        os.rmdir(directory)

def remove_file(filename: str):
    if os.path.exists(filename):
        os.remove(filename)
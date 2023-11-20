import os
import timeit


def size_of_file(filename: str) -> int:
    return int(os.path.getsize(filename))


def measure_time(code: callable, unit: int):
    return timeit.timeit(code, number=1) * unit


def remove_file(filename: str):
    if os.path.exists(filename):
        os.remove(filename)
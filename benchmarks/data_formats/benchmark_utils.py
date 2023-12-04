import os


def size_of_file(filename: str) -> int:
    return int(os.path.getsize(filename))


def remove_file(filename: str):
    if os.path.exists(filename):
        os.remove(filename)
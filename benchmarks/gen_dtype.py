from enum import Enum, auto
import numpy as np
import random
import string

class GenDtype(Enum):

    NO_STR_COLS = auto()
    RAND_STR_LEN = auto()
    FIX_STR_LEN = auto()

    @classmethod
    def gen_int(cls, low: int, high: int, count: int) -> list[int]:
        return [np.random.randint(low, high) for i in range(count)]

    @classmethod
    def gen_float(cls, low: int, high: int, count: int) -> list[float]:
        return [np.random.uniform(low, high) for i in range(count)]

    @classmethod
    def gen_str(cls, length: int) -> str:
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    @classmethod
    def gen_str_f(cls, length: int, count: int) -> list[str]:
        return [cls.gen_str(length) for i in range(count)]

    @classmethod
    def gen_str_v(cls, low: int, high: int, count: int) -> list[str]:
        letters = string.ascii_letters
        return [''.join(random.choice(letters) for i in range(np.random.randint(low, high))) for i in range(count)]

    @classmethod
    def gen_bool(cls, count: int) -> list[bool]:
        return [random.choice([True, False]) for i in range(count)]
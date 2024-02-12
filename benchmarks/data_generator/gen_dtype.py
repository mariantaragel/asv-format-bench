import numpy as np
import random
import string


class GenDtype:

    def gen_fixed_str(self, length: int) -> str:
        letters = string.ascii_letters
        return "".join(random.choices(letters, k=length))

    def gen_rand_str(self, low: int, high: int) -> str:
        length = np.random.randint(low, high)
        return self.gen_fixed_str(length)

    def gen_int_col(self, low: int, high: int, count: int) -> list[int]:
        return np.random.randint(low, high, count).tolist()

    def gen_float_col(self, low: int, high: int, count: int) -> list[float]:
        return np.random.uniform(low, high, count).tolist()

    def gen_fixed_str_col(self, length: int, count: int) -> list[str]:
        return [self.gen_fixed_str(length) for i in range(count)]

    def gen_var_str_col(self, low: int, high: int, count: int) -> list[str]:
        return [self.gen_rand_str(low, high) for i in range(count)]

    def gen_bool_col(self, count: int) -> list[bool]:
        return random.choices([True, False], k=count)

    def gen_list_col(self, count: int) -> list[list]:
        return [
            [
                np.random.randint(0, 15),
                np.random.randint(0, 15),
                np.random.uniform(-np.pi, np.pi),
                random.choice([0, 1]),
            ]
            for i in range(count)
        ]

    def gen_dict_col(self, count: int) -> list[dict[str, int]]:
        return [
            {self.gen_fixed_str(10): 0, self.gen_fixed_str(10): 1} for i in range(count)
        ]
import numpy as np
import random
import string


class GenDtype:

    def gen_cols(self, cols: int, entries: int, dtype: str, nan_ratio: float, params: dict) -> list[list]:
        return [self.gen(entries, dtype, nan_ratio, params) for i in range(cols)]

    def gen(self, entris: int, dtype: str, nan_ratio: float, params: dict) -> list:
        if dtype == "int":
            func = np.random.randint
        elif dtype == "float":
            func = np.random.uniform
        elif dtype == "str_var":
            func = self.gen_rand_str
        elif dtype == "str_fix":
            func = self.gen_fixed_str
        elif dtype == "bool":
            func = self.gen_bool
        else:
            return

        result = []
        num_of_nan = round(entris * nan_ratio)
        num_of_vals = entris - num_of_nan

        for i in range(entris):
            if num_of_nan != 0 and num_of_vals != 0:
                if np.random.uniform(0, 1) <= nan_ratio:
                    result.append(np.nan)
                    num_of_nan -= 1
                else:
                    result.append(func(**params))
                    num_of_vals -= 1
            else:
                if num_of_nan == 0:
                    result += [func(**params) for j in range(entris - i)]
                else:
                    result += [np.nan for j in range(entris - i)]
                break

        return result

    def gen_fixed_str(self, length: int) -> str:
        letters = string.ascii_letters
        return "".join(random.choice(letters) for i in range(length))

    def gen_rand_str(self, low: int, high: int) -> str:
        length = np.random.randint(low, high)
        return self.gen_fixed_str(length)

    def gen_bool(self) -> bool:
        return random.choice([True, False])

    def gen_int_col(self, low: int, high: int, count: int) -> list[int]:
        return [np.random.randint(low, high) for i in range(count)]

    def gen_float_col(self, low: int, high: int, count: int) -> list[float]:
        return [np.random.uniform(low, high) for i in range(count)]

    def gen_fixed_str_col(self, length: int, count: int) -> list[str]:
        return [self.gen_fixed_str(length) for i in range(count)]

    def gen_var_str_col(self, low: int, high: int, count: int) -> list[str]:
        return [self.gen_rand_str(low, high) for i in range(count)]

    def gen_bool_col(self, count: int) -> list[bool]:
        return [self.gen_bool() for i in range(count)]

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
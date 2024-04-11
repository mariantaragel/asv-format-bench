import numpy as np
import random
import string

class GenDtype:

    words = [
        "Abjure", "Future", "Picnic", "Agonistic", "Garland", "Protect", "Airline",
        "Gigantic", "Publish", "Bandit", "Goofy", "Quadrangle", "Banquet",
        "Government", "Recount", "Binoculars", "Grandnieces", "Redoubtable",
        "Biologist", "Handbook", "Reflection", "Blackboard", "Himself", "Reporter",
        "Board", "Indulge", "Ring", "Bookworm", "Inflatable", "Salesclerk",
        "Butterscotch", "Inimical", "Snapshot", "Camera", "Interim", "Shellfish",
        "Campus", "Invest", "Ship", "Catfish", "Jackpot", "Significance", "Carsick",
        "Kitchenette", "Sometimes", "Celebrate", "Law", "Sublime", "Celery", "Life",
        "Tabletop", "Citizen", "Lifeline", "Teamwork", "Coloring", "Love", "Tennis",
        "Compact", "Magnificent", "Timesaving", "Dark", "Malevolence", "Tree",
        "Damage", "Man", "Termination", "Dangerous", "Mascot", "Underestimate",
        "Decorum", "Marshmallow", "Vineyard", "Endorse", "Mine", "War", "Engender",
        "Moonwalk", "Way", "Erratic", "Near", "Wealth", "Envelope", "Nephogram",
        "Wednesday", "Etymology", "Newborn", "World", "Eyewitness", "Noisome", "Xerox",
        "Eulogy", "Owl", "You", "Fish", "Parenthesis", "Zestful", "Food",
        "Perpetrator", "Foreclose", "Phone"
    ]

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
        chars = np.array(list(string.ascii_letters + string.digits), dtype=(np.str_, 1))
        retval = (
            np.random.default_rng(2)
            .choice(chars, size=length * np.prod(count), replace=True)
            .view((np.str_, length))
            .reshape(count)
        )
        return retval.astype("O").tolist()

    def gen_var_str_col(self, low: int, high: int, count: int) -> list[str]:
        return [self.gen_rand_str(low, high) for i in range(count)]
    
    def gen_str_words(self, count: int) -> list[str]:
        return random.choices(self.words, k=count)

    def gen_bool_col(self, count: int) -> list[bool]:
        return random.choices([True, False], k=count)
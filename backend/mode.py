from collections import Counter
from functools import lru_cache
from numbers import Number
from .pattern import Pattern


class Mode(Pattern):
    def __init__(self, lst: list[Number]):
        self._lst = lst
        super().__init__()

    @lru_cache(None)
    def _count(self):
        counter = Counter(self._lst)
        max_value = max(counter.values())
        if all(max_value == i for i in counter.values()):
            return []
        counter = {key: value for key, value in counter.items() if value == max_value}
        return list(counter.keys())


if __name__ == '__main__':
    # assert Mode([1, 2, 3, 4, 5]).answer == []
    # assert Mode([1, 2, 2, 3, 4]).answer == [2]
    # assert Mode([1, 2, 2, 3, 3, 4]).answer == [2, 3]
    # assert Mode([1, 2, 2, 3, 3, 3]).answer == [3]
    print(*Mode([*([1] * 11), 111, 11, 222, 22, 333, 33, 444, 44, 555, *([55] * 111)]).answer, sep='\n')

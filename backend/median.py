from functools import lru_cache
from numbers import Number
from backend.pattern import Pattern


class Median(Pattern):
    def __init__(self, lst: list[Number]):
        self._lst = lst
        super().__init__()

    @lru_cache(None)
    def _count(self):
        lst = sorted(self._lst)
        if len(lst) % 2 == 0:
            return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
        else:
            return lst[len(lst) // 2]


if __name__ == '__main__':
    # assert Mode([1, 2, 3, 4, 5]).answer == []
    # assert Mode([1, 2, 2, 3, 4]).answer == [2]
    # assert Mode([1, 2, 2, 3, 3, 4]).answer == [2, 3]
    # assert Mode([1, 2, 2, 3, 3, 3]).answer == [3]
    print(Median([1, 2, 3, 4]).answer, sep='\n')

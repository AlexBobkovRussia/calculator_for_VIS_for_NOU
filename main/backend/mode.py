from pattern import Pattern
from numbers import Number
from functools import lru_cache
from collections import Counter


class Mode(Pattern):
    def __init__(self, lst: list[Number]):
        self._lst = lst
        super().__init__()

    @lru_cache(None)
    def _make_step_by_step_response(self):
        output = f'{', '.join(self._lst)} = {', '.join(sorted(self._lst))}\n'
        first_line, second_line, third_line = '', '', ''
        counter = Counter(self._lst)
        for i, j in counter.items():
            length_i = len(str(i))
            length_j = len(str(j))
            if length_i > length_j:
                pass
            elif length_i > length_j:
                pass
            else:
                pass

    @lru_cache(None)
    def _count(self):
        counter = Counter(self._lst)
        max_value = max(counter.values())
        if all(max_value == i for i in counter.values()):
            return []
        counter = {key: value for key, value in counter.items() if value == max_value}
        return list(counter.keys())


if __name__ == '__main__':
    assert Mode([1, 2, 3, 4, 5]).answer == []
    assert Mode([1, 2, 2, 3, 4]).answer == [2]
    assert Mode([1, 2, 2, 3, 3, 4]).answer == [2, 3]
    assert Mode([1, 2, 2, 3, 3, 3]).answer == [3]

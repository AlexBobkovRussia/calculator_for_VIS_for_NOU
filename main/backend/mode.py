from collections import Counter
from functools import lru_cache
from numbers import Number

from pattern import Pattern


class Mode(Pattern):
    def __init__(self, lst: list[Number]):
        self._lst = lst
        super().__init__()

    @lru_cache(None)
    def _make_step_by_step_response(self):
        output = f'{', '.join(map(str, self._lst))} = {', '.join(sorted(map(str, self._lst)))}\n'
        first_line, second_line, third_line, fourth_line, fifth_line = '+', '|', '+', '|', '+'
        counter = Counter(self._lst)
        for i, j in counter.items():
            length_i = len(str(i))
            length_j = len(str(j))
            if length_i > length_j:
                first_line += f' +'
                second_line += f''
                third_line += f' +'
                fourth_line += f''
                fifth_line += f' +'
            elif length_i < length_j:
                first_line += f' +'
                second_line += f''
                third_line += f' +'
                fourth_line += f''
                fifth_line += f' +'
            else:
                first_line += f'{"-" * (length_i + 2)}+'
                second_line += f' {i} |'
                third_line += f'{"-" * (length_i + 2)}+'
                fourth_line += f' {j} |'
                fifth_line += f'{"-" * (length_i + 2)}+'
        first_line += '\n'
        second_line += '\n'
        third_line += '\n'
        fourth_line += '\n'
        fifth_line += '\n'
        output += first_line + second_line + third_line + fourth_line + fifth_line
        return output

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
    print(Mode([1, 2, 3, 4, 5]).step_by_step_answer)

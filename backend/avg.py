from functools import lru_cache
from numbers import Number
from backend.pattern import Pattern


class Avg(Pattern):
    def __init__(self, lst: list[Number]):
        self._lst = lst
        self.step_by_step_answer = self.counting_step_by_step_answer()
        super().__init__()

    @lru_cache(None)
    def _count(self):
        return max(self._lst) - min(self._lst)

    @lru_cache(None)
    def counting_step_by_step_answer(self):
        # first_line = second_line = third_line = ''
        # first_line += ' + '.join(map(str, self._lst))
        # second_line += '-' * (len(self._lst) + 3 * (len(self._lst) - 1)) + ' = ' + str(self._count())
        # third_line += ' ' * (len(first_line) // 2) + str(len(self._lst))
        return f'({" + ".join(map(str, self._lst))}) / {len(self._lst)} = {self._count()}'


if __name__ == '__main__':
    # assert Mode([1, 2, 3, 4, 5]).answer == []
    # assert Mode([1, 2, 2, 3, 4]).answer == [2]
    # assert Mode([1, 2, 2, 3, 3, 4]).answer == [2, 3]
    # assert Mode([1, 2, 2, 3, 3, 3]).answer == [3]
    print(Avg([1, 2, 3, 4]).answer, sep='\n')
    print(Avg([1, 2, 3]).step_by_step_answer, sep='\n')

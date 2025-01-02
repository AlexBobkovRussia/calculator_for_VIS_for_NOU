from numbers import Number
from functools import lru_cache
from back.statistical_inducators.collection import Collection
from Errors import LengthError
import sys

sys.path.append('.')


class Avg(Collection):
    @lru_cache
    def make_course_of_the_decision(self) -> str:
        return f'({' + '.join(map(str, self._lst))}) / {len(self._lst)} -> '

    @lru_cache
    def _count_the_answer(self) -> Number | None:
        if not self._lst:
            raise LengthError('Длина списка должна быть больше нуля!')
        return self.returning('Среднее арифметическое', sum(self._lst) / len(self._lst))


if __name__ == '__main__':
    assert Avg([1]).answer == 1
    assert Avg([1, 2]).answer == 1.5
    assert Avg([1, 2, 3]).answer == 2
    assert Avg([1, 2, 3, 4]).answer == 2.5
    assert Avg([1, 2, 3, 4, 5]).answer == 3
    try:
        assert Avg([]) == LengthError
    except LengthError:
        print('Ошибка LengthError ОТРАБОТАЛА')
    else:
        print('Ошибка LengthError НЕ ОТРАБОТАЛА')

    try:
        assert Avg(['a']) == TypeError
    except TypeError:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')

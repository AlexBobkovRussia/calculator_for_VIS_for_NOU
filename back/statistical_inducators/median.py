from numbers import Number
from functools import lru_cache
from back.statistical_inducators.collection import Collection
from Errors import LengthError


class Median(Collection):
    @lru_cache
    def _count_the_answer(self) -> Number | None:
        if not self._lst:
            raise LengthError('Длина списка должна быть больше нуля!')
        self._lst.sort()
        if len(self._lst) % 2 != 0:
            return self._lst[len(self._lst) // 2]
        else:
            return (self._lst[len(self._lst) // 2 - 1] + self._lst[len(self._lst) // 2]) / 2


if __name__ == '__main__':
    assert Median([1, 2, 3]).answer == 2
    assert Median([1, 2, 3, 4]).answer == 2.5
    assert Median([1, 2, 3, 4, 5]).answer == 3
    assert Median([6, 5, 3, 4, 2, 1]).answer == 3.5

    try:
        assert Median([]) == LengthError
    except LengthError:
        print('Ошибка LengthError ОТРАБОТАЛА')
    else:
        print('Ошибка LengthError НЕ ОТРАБОТАЛА')

    try:
        assert Median(['a']) == TypeError
    except TypeError:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')


import sys
sys.path.append('.')

from numbers import Number
from functools import lru_cache
from back.collection import Collection
from Errors import LengthError


class Scope(Collection):
    @lru_cache
    def _count_the_answer(self) -> Number | None:
        if not len(self._lst) >= 2:
            raise LengthError('Длина списка должна быть больше нуля!')
        return max(self._lst) - min(self._lst)


if __name__ == '__main__':
    assert Scope([1, 2, 3]).answer == 2
    assert Scope([1, 2, 3, 4]).answer == 3
    assert Scope([1, 2, 3, 4, 5]).answer == 4
    try:
        assert Scope([]) == LengthError
    except:
        print('Ошибка LengthError ОТРАБОТАЛА')
    else:
        print('Ошибка LengthError НЕ ОТРАБОТАЛА')
    
    try:
        assert Scope(['a']) == TypeError
    except:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')
    
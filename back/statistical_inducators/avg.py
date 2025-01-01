import sys
sys.path.append('.')

from numbers import Number
from functools import lru_cache
from back.abstract_classes import Abstraction
from Errors import LengthError


class Avg(Abstraction):
    def __init__(self, lst: list[Number]):
        if not all(isinstance(i, Number) for i in lst):
            raise TypeError('Все элементы списка должны быть числами!')
        self._lst = lst
        self.answer = self._count_the_answer()
    
    def __call__(self, element: Number):
        if not isinstance(element, Number):
            raise TypeError('Новый элемент должен  быть числом!')
        self._lst.append(element)
    
    @lru_cache(None)
    def _count_the_answer(self) -> Number | None:
        if not self._lst:
            raise LengthError('Длина списка должна быть больше нуля!')
        return sum(self._lst) / len(self._lst)
    
    
if __name__ == '__main__':
    assert Avg([1]).answer == 1
    assert Avg([1, 2]).answer == 1.5
    assert Avg([1, 2, 3]).answer == 2
    assert Avg([1, 2, 3, 4]).answer == 2.5
    assert Avg([1, 2, 3, 4, 5]).answer == 3
    try:
        assert Avg([]) == LengthError
    except:
        print('Ошибка LengthError ОТРАБОТАЛА')
    else:
        print('Ошибка LengthError НЕ ОТРАБОТАЛА')
    
    try:
        assert Avg(['a']) == TypeError
    except:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')
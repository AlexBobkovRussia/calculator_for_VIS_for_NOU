import sys
sys.path.append('.')

from numbers import Number
from back.cache import Cache
from back.abstract_classes import Abstraction
from Errors import LengthError

class Mediana(Cache, Abstraction):
    def __init__(self, lst: Number) -> None:
        if not all(isinstance(i, Number) for i in lst):
            raise TypeError('Все элементы списка должны быть целыми числами!')
        self._lst = lst
        self.answer = self.count_the_answer()
        
    def __call__(self, number: Number) -> None:
        if not isinstance(number, Number):
            raise TypeError('Все элементы списка должны быть целыми числами!')
        self._lst.append(number)
        
        
    # @Cache._cache
    def count_the_answer(self) -> Number:
        if not self._lst:
            raise LengthError('Длина списка должна быть больше нуля!')
        self._lst.sort()
        if len(self._lst) % 2 != 0:
            return self._lst[len(self._lst) // 2]
        else:
            return self._lst[len(self._lst) // 2 - 1] + self._lst[len(self._lst) // 2]
        

    

if __name__ == '__main__':
    assert Mediana([1, 2, 3]).answer == 2
    assert Mediana([1, 2, 3, 4]).answer == 5
    assert Mediana([1, 2, 3, 4, 5]).answer == 3
    assert Mediana([]).answer == LengthError
    assert Mediana(['a', 'b', 'c']).answer == TypeError
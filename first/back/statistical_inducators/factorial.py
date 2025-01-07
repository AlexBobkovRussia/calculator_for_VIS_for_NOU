import sys
from functools import lru_cache
from math import factorial
from numbers import Number

sys.path.append('')


class Factorial:
    def __init__(self, number: Number):
        self._number = number
        self.answer = self._count_the_answer()

    def __call__(self, number: Number):
        self._number = number

    @lru_cache
    def _count_the_answer(self):
        if not self._number >= 0:
            raise ValueError('number должно быть больше или равно нулю!')
        if not isinstance(self._number, Number):
            raise TypeError('number должно быть числом!')
        return factorial(self._number)


if __name__ == '__main__':
    assert Factorial(1).answer == 1
    assert Factorial(2).answer == 2
    assert Factorial(3).answer == 6
    assert Factorial(4).answer == 24
    assert Factorial(4).answer == 24

    try:
        assert Factorial(-1) == ValueError
    except ValueError:
        print('Ошибка ValueError ОТРАБОТАЛА')
    else:
        print('Ошибка ValueError НЕ ОТРАБОТАЛА')

    try:
        assert Factorial('a') == TypeError
    except TypeError:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')

    try:
        assert Factorial([]) == TypeError
    except TypeError:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')

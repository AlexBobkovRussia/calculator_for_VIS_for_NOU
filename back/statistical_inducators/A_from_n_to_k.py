from functools import lru_cache
from numbers import Number
from math import factorial
import sys

sys.path.append('.')


class AFromNToK:
    def __init__(self, *, n: Number, k: Number):
        self._n = n
        self._k = k
        self.answer = self._count_the_answer()

    def __call__(self, *, n: Number, k: Number):
        self._n = n
        self._k = k

    @lru_cache
    def _count_the_answer(self):
        if not isinstance(self._n, Number):
            raise TypeError('n должно быть числом!')
        if not isinstance(self._k, Number):
            raise TypeError('k должно быть числом!')
        if self._n < 0:
            raise ValueError('n должно быть неотрицательным числом!')
        if self._k < 0:
            raise ValueError('k должно быть неотрицательным числом!')
        if self._n < self._k:
            raise ValueError('n должно быть не меньше k!')
        return factorial(self._n) / factorial(self._n - self._k)


if __name__ == '__main__':
    assert AFromNToK(n=10, k=5).answer == 30240
    assert AFromNToK(n=5, k=5).answer == 120

    try:
        assert AFromNToK(n=-1, k=30)
    except ValueError:
        print('Ошибка ValueError ОТРАБОТАЛА')
    else:
        print('Ошибка ValueError НЕ ОТРАБОТАЛА')

    try:
        assert AFromNToK(n=1, k=-2)
    except ValueError:
        print('Ошибка ValueError ОТРАБОТАЛА')
    else:
        print('Ошибка ValueError НЕ ОТРАБОТАЛА')

    try:
        assert AFromNToK(n=5, k=15)
    except ValueError:
        print('Ошибка ValueError ОТРАБОТАЛА')
    else:
        print('Ошибка ValueError НЕ ОТРАБОТАЛА')

    try:
        assert AFromNToK(n=-5, k=-15)
    except ValueError:
        print('Ошибка ValueError ОТРАБОТАЛА')
    else:
        print('Ошибка ValueError НЕ ОТРАБОТАЛА')

    try:
        assert AFromNToK(n='l', k=-15)
    except TypeError:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')

    try:
        assert AFromNToK(n=5, k='o')
    except TypeError:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')

    try:
        assert AFromNToK(n='l', k='o')
    except TypeError:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')

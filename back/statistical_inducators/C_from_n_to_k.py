from math import factorial
from back.statistical_inducators.A_from_n_to_k import AFromNToK
from functools import lru_cache
import sys

sys.path.append('.')


class CFromNToK(AFromNToK):

    @lru_cache
    def _count_the_answer(self):
        return super()._count_the_answer() / factorial(self._k)


if __name__ == '__main__':
    assert CFromNToK(n=10, k=0).answer == 1
    assert CFromNToK(n=10, k=1).answer == 10
    assert CFromNToK(n=10, k=2).answer == 45

    assert CFromNToK(n=10, k=5).answer == 252
    assert CFromNToK(n=20, k=8).answer == 125970

    try:
        assert CFromNToK(n=-1, k=30)
    except ValueError:
        print('Ошибка ValueError ОТРАБОТАЛА')
    else:
        print('Ошибка ValueError НЕ ОТРАБОТАЛА')

    try:
        assert CFromNToK(n=1, k=-2)
    except ValueError:
        print('Ошибка ValueError ОТРАБОТАЛА')
    else:
        print('Ошибка ValueError НЕ ОТРАБОТАЛА')

    try:
        assert CFromNToK(n=5, k=15)
    except ValueError:
        print('Ошибка ValueError ОТРАБОТАЛА')
    else:
        print('Ошибка ValueError НЕ ОТРАБОТАЛА')

    try:
        assert CFromNToK(n=-5, k=-15)
    except ValueError:
        print('Ошибка ValueError ОТРАБОТАЛА')
    else:
        print('Ошибка ValueError НЕ ОТРАБОТАЛА')

    try:
        assert CFromNToK(n='l', k=-15)
    except TypeError:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')

    try:
        assert CFromNToK(n=5, k='o')
    except TypeError:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')

    try:
        assert CFromNToK(n='l', k='o')
    except TypeError:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')

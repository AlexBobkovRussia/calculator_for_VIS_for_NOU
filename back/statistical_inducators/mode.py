import sys
sys.path.append('.')


from numbers import Number
from functools import lru_cache
from back.collection import Collection
from Errors import LengthError
from collections import Counter

class Mode(Collection):
    @lru_cache
    def _count_the_answer(self) -> Number | None:
        if not self._lst:
            raise LengthError('Длина списка должна быть больше нуля!')
        counter = Counter(self._lst)
        max_elem = max(counter.values())
        counter = dict(list(filter(lambda x: x[1] == max_elem, counter.items())))
        counter = dict(sorted(counter.items(), key=lambda x: x[0]))
        return list(counter.keys())


if __name__ == '__main__':
    assert Mode([1]).answer == [1]
    assert Mode([1, 2]).answer == [1, 2]
    assert Mode([1, 2, 3]).answer == [1, 2, 3]
    assert Mode([1, 2, 3, 4]).answer == [1, 2, 3, 4]
    assert Mode([1, 2, 3, 4, 5]).answer == [1, 2, 3, 4, 5]
    assert Mode([1, 2, 2]) == [2]
    assert Mode([1, 2, 2, 3, 3]) == [2, 3]
    assert Mode([1, 2, 2, 3]) == [2]
    assert Mode([1, 1, 1, 2, 2, 2, 3, 3, 3]) == [1, 2, 3]
    try:
        assert Mode([]) == LengthError
    except:
        print('Ошибка LengthError ОТРАБОТАЛА')
    else:
        print('Ошибка LengthError НЕ ОТРАБОТАЛА')
    
    try:
        assert Mode(['a']) == TypeError
    except:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')
from numbers import Number
from functools import lru_cache
from first.back.statistical_inducators.collection import Collection
from first.Errors import LengthError, ModeError
from collections import Counter
import sys

sys.path.append('')


class Mode(Collection):
    @lru_cache
    def make_course_of_the_decision(self) -> str:
        output = f'{', '.join(map(str, self._lst))} -> '
        return output

    @lru_cache
    def _count_the_answer(self) -> Number | None:
        if not self._lst:
            raise LengthError('Длина списка должна быть больше нуля!')
        counter = Counter(self._lst)
        max_elem = max(counter.values())
        if all(i == max_elem for i in counter.values()):
            raise ModeError('Моды нет!')
        counter = dict(list(filter(lambda x: x[1] == max_elem, counter.items())))
        counter = dict(sorted(counter.items(), key=lambda x: x[0]))
        self.counted_answer = list(counter.keys())
        return self.returning('Мода', self.counted_answer)


if __name__ == '__main__':
    assert Mode([1, 2, 2]).answer == [2]
    assert Mode([1, 2, 2, 3, 3]).answer == [2, 3]
    assert Mode([1, 2, 2, 3]).answer == [2]

    try:
        assert Mode([1]).answer
    except ModeError:
        print('Ошибка ModeError ОТРАБОТАЛА')
    else:
        print('Ошибка ModeError НЕ ОТРАБОТАЛА')

    try:
        assert Mode([]).answer
    except LengthError:
        print('Ошибка LengthError ОТРАБОТАЛА')
    else:
        print('Ошибка LengthError НЕ ОТРАБОТАЛА')

    try:
        assert Mode(['a']).answer
    except TypeError:
        print('Ошибка TypeError ОТРАБОТАЛА')
    else:
        print('Ошибка TypeError НЕ ОТРАБОТАЛА')

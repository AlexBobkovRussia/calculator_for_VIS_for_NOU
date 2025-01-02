from abc import ABC, abstractmethod
from numbers import Number
import sys

sys.path.append('..')


class Collection(ABC):
    def __init__(self, lst: list[Number], add_name=False):
        if not all(isinstance(i, Number) for i in lst):
            raise TypeError('Все элементы списка должны быть числами!')
        self._lst = lst
        self.add_name = add_name
        self.answer = self._count_the_answer()

    def __call__(self, element: Number):
        if not isinstance(element, Number):
            raise TypeError('Новый элемент должен  быть числом!')
        self._lst.append(element)

    @abstractmethod
    def _count_the_answer(self):
        pass

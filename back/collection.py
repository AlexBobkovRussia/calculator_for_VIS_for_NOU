import sys
sys.path.append('.')

from abc import ABC, abstractmethod
from numbers import Number

class Collection(ABC):
    def __init__(self, lst: list[Number]):
        if not all(isinstance(i, Number) for i in lst):
            raise TypeError('Все элементы списка должны быть числами!')
        self._lst = lst
        self.answer = self._count_the_answer()
    
    def __call__(self, element: Number):
        if not isinstance(element, Number):
            raise TypeError('Новый элемент должен  быть числом!')
        self._lst.append(element)
    
    @abstractmethod
    def _count_the_answer(self): pass
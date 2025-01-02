from abc import ABC, abstractmethod
from numbers import Number
import sys

sys.path.append('.')


class Collection(ABC):
    def __init__(self, lst: list[Number], add_name=False, course_of_the_decision=False) -> None:
        if not all(isinstance(i, Number) for i in lst):
            raise TypeError('Все элементы списка должны быть числами!')
        self._lst = lst
        self.add_name = add_name
        self.course_of_the_decision = course_of_the_decision
        self.answer = self._count_the_answer()

    def __call__(self, element: Number) -> None:
        if not isinstance(element, Number):
            raise TypeError('Новый элемент должен  быть числом!')
        self._lst.append(element)

    @abstractmethod
    def _count_the_answer(self) -> Number:
        pass

    @abstractmethod
    def make_course_of_the_decision(self) -> str:
        pass

    def returning(self, name, counted_answer) -> tuple[str, str, int]:
        if self.add_name and self.course_of_the_decision:
            return name, self.make_course_of_the_decision(), counted_answer
        if self.add_name and not self.course_of_the_decision:
            return name, counted_answer
        if not self.add_name and self.course_of_the_decision:
            return self.course_of_the_decision, counted_answer
        if not self.add_name and not self.course_of_the_decision:
            return counted_answer

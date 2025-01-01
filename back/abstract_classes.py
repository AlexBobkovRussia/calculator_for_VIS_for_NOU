import sys
sys.path.append('.')

from abc import ABC, abstractmethod
from numbers import Number


class Abstraction(ABC):           
    @abstractmethod 
    def count_the_answer(self) -> Number:
        pass
from abc import ABC, abstractmethod


class Pattern(ABC):
    def __init__(self):
        self.answer = self._count()

    @abstractmethod
    def _count(self):
        pass


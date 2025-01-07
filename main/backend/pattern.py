from abc import ABC, abstractmethod


class Pattern(ABC):
    def __init__(self):
        self.answer = self._count()
        self.step_by_step_answer = self._make_step_by_step_response()

    @abstractmethod
    def _count(self):
        pass

    @abstractmethod
    def _make_step_by_step_response(self):
        pass

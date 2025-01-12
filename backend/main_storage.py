from numbers import Number


class Storage:
    def __init__(self, lst: list[Number] | None):
        self._lst = lst

    @property
    def lst(self):
        if self._lst is None:
            raise ValueError('Список не инициализирован!')
        return self._lst

    def __call__(self, lst: list[Number]):
        self._lst = lst


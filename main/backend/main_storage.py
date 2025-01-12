class Storage:
    def __init__(self, lst):
        self._lst = lst

    @property
    def lst(self):
        return self._lst

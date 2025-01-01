import sys
sys.path.append('.')

from frozendict import frozendict

class Cache():
    @classmethod
    def _cache(self, func):
        def wrapper(*args, **kwargs):
            dct = {}
            if (args, frozendict(kwargs)) in dct:
                return dct[(args, frozendict(kwargs))]
            else:
                dct[(args, frozendict(kwargs))] = func(self, *args, **kwargs)
        return wrapper
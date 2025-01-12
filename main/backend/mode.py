from collections import Counter
from functools import lru_cache
from numbers import Number
from prettytable import PrettyTable

from pattern import Pattern


class Mode(Pattern):
    def __init__(self, lst: list[Number]):
        self._lst = lst
        super().__init__()

    def _make_table(self):
        counter = Counter(self._lst)
        th, td = list(counter.keys()), list(counter.values())
        columns = len(th)  # Подсчитаем кол-во столбцов на будущее.

        table = PrettyTable(th)  # Определяем таблицу.

        # Cкопируем список td, на случай если он будет использоваться в коде дальше.
        td_data = td[:]
        # Входим в цикл который заполняет нашу таблицу.
        # Цикл будет выполняться до тех пор пока у нас не кончатся данные
        # для заполнения строк таблицы (список td_data).
        while td_data:
            # Используя срез добавляем первые пять элементов в строку.
            # (columns = 5).
            table.add_row(td_data[:columns])
            # Используя срез переопределяем td_data так, чтобы он
            # больше не содержал первых 5 элементов.
            td_data = td_data[columns:]
        return table

    @lru_cache(None)
    def _make_step_by_step_response(self):
        output = f'{', '.join(map(str, self._lst))} = {', '.join(sorted(map(str, self._lst)))}\n'
        return output, self._make_table()

    @lru_cache(None)
    def _count(self):
        counter = Counter(self._lst)
        max_value = max(counter.values())
        if all(max_value == i for i in counter.values()):
            return []
        counter = {key: value for key, value in counter.items() if value == max_value}
        return list(counter.keys())


if __name__ == '__main__':
    # assert Mode([1, 2, 3, 4, 5]).answer == []
    # assert Mode([1, 2, 2, 3, 4]).answer == [2]
    # assert Mode([1, 2, 2, 3, 3, 4]).answer == [2, 3]
    # assert Mode([1, 2, 2, 3, 3, 3]).answer == [3]
    print(*Mode([*([1] * 11), 111, 11, 222, 22, 333, 33, 444, 44, 555, *([55] * 111)]).step_by_step_answer, sep='\n')

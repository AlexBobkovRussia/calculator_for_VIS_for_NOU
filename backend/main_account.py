from collections import Counter
from prettytable import PrettyTable
from .main_storage import Storage


class MainAccount:
    def __init__(self, storage: Storage):
        self._lst = storage.lst
        output = self.output()

    def _sorted_list(self):
        return sorted(self._lst)

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

    def output(self):
        return f"Список чисел: {', '.join(map(str, self._lst))}\nОтсортированный список: {', '.join(map(str, self._sorted_list()))}\nТаблица частот: \n{self._make_table()}\n"


if __name__ == '__main__':
    print(MainAccount(Storage([5, 1, 2, 3, 4, 5])).output())

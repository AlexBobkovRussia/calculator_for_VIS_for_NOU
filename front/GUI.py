from customtkinter import *
from back import *
from Errors import LengthError, ModeError


class Answers:
    def __init__(self, what_count: list[str, ...], data):
        self.__what_count = what_count
        self.__output = []
        if len(data) == 0:
            raise LengthError('Не указаны данные!')
        try:
            self.__data = list(map(lambda x: int(x.strip()), data.split(',')))
        except (TypeError, ValueError):
            raise ValueError('Неверный формат данных')

    def output(self):
        if 'Мода' in self.__what_count:
            try:
                self.__output.append(Mode(self.__data).answer)
            except ModeError:
                self.__output.append('Моды нет!')
        if 'Медиана' in self.__what_count:
            self.__output.append(Median(self.__data).answer)
        if 'Размах' in self.__what_count:
            self.__output.append(Scope(self.__data).answer)
        if 'Среднее арифметическое' in self.__what_count:
            self.__output.append(Avg(self.__data).answer)
        print(self.__output)


class Root:
    def __init__(self, *, title: str, resizable: list[bool, bool], bg: str, geometry: str):
        self._root = CTk()
        self._root.title(title)
        self._root.resizable(*resizable)
        self._root.config(bg=bg)
        self._root.geometry(geometry)
        self.__what_count: list[str, ...] = []

    def input_field(self):
        entry = CTkEntry(master=self._root, placeholder_text='Введите список чисел через запятую', font=('Arial', 25), width=800)
        entry.grid(row=0, column=0)
        entry.bind('<Return>', lambda x: (answer := Answers(self.__what_count, entry.get()).output()))

    def _what_count(self, value):
        if value not in self.__what_count:
            self.__what_count.append(value)
        else:
            self.__what_count.remove(value)
        print(self.__what_count)

    def check_boxes(self):
        CTkCheckBox(master=self._root, text='Мода', font=('Arial', 25), width=800, bg_color='#E0F2F7', command=lambda: self._what_count('Мода')).grid(row=1, column=0)
        CTkCheckBox(master=self._root, text='Медиана', font=('Arial', 25), width=800, bg_color='#E0F2F7', command=lambda: self._what_count('Медиана')).grid(row=2, column=0)
        CTkCheckBox(master=self._root, text='Размах', font=('Arial', 25), width=800, bg_color='#E0F2F7', command=lambda: self._what_count('Размах')).grid(row=3, column=0)
        CTkCheckBox(master=self._root, text='Среднее арифметическое', font=('Arial', 25), width=800, bg_color='#E0F2F7', command=lambda: self._what_count('Среднее арифметическое')).grid(row=4, column=0)

    def answer(self):
        answer = CTkLabel(master=self._root, text='', font=('Arial', 25), width=800, bg_color='#E0F2F7')
        answer.grid(row=6, column=0)
        answer = CTkLabel(master=self._root, text='Ответ:', font=('Arial', 25), width=200, bg_color='#E0F2F7')
        answer.grid(row=7, column=0)

    def output(self):
        box = CTkTextbox(master=self._root, font=('Arial', 25), width=800, height=370, bg_color='#E0F2F7', fg_color='white', wrap='none')
        box.grid(row=8, column=0)

    def count_the_answer(self):
        counting = CTkButton(master=self._root, text='Посчитать', font=('Arial', 25), width=200, bg_color='#E0F2F7', fg_color='darkblue', hover_color='#0089FF', command=lambda: (answer := Answers(self.__what_count, entry.get()).output())))
        counting.grid(row=5, column=0)

    def mainloop(self):
        self._root.mainloop()


root = Root(title='Калькулятор для ВиС', resizable=[False, False], bg='#E0F2F7', geometry='800x600')
root.input_field()
root.check_boxes()
root.count_the_answer()
root.answer()
root.output()
root.mainloop()

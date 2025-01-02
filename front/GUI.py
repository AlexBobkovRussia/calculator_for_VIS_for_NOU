from customtkinter import *
from back import *
from Errors import LengthError, ModeError, SelectError
from numbers import Number


class Answers:
    def __init__(self, what_count: list[str, ...], data, add_name=False, course_of_the_decision=False):
        self.__what_count = what_count
        self.__output = {}
        self.add_name = add_name
        self.course_of_the_decision = course_of_the_decision
        if len(data) == 0:
            raise LengthError('Не указаны данные!')
        try:
            self.__data = list(map(lambda x: int(x.strip()), data.split(',')))
        except (TypeError, ValueError):
            raise ValueError('Неверный формат данных')

    def output(self):
        if 'Мода' in self.__what_count:
            try:
                data = Mode(self.__data, add_name=self.add_name,
                            course_of_the_decision=self.course_of_the_decision).answer
                self.__output[data[0]] = data[1:]
            except ModeError:
                self.__output['Мода'] = 'Моды нет!'
        if 'Медиана' in self.__what_count:
            data = Median(self.__data, add_name=self.add_name,
                          course_of_the_decision=self.course_of_the_decision).answer
            self.__output[data[0]] = data[1:]
        if 'Размах' in self.__what_count:
            data = Scope(self.__data, add_name=self.add_name, course_of_the_decision=self.course_of_the_decision).answer
            self.__output[data[0]] = data[1:]
        if 'Среднее арифметическое' in self.__what_count:
            data = Avg(self.__data, add_name=self.add_name, course_of_the_decision=self.course_of_the_decision).answer
            self.__output[data[0]] = data[1:]
        return self.__output


class Root:
    def __init__(self, *, title: str, resizable: list[bool, bool], bg: str, geometry: str):
        self._root = CTk()
        self._root.title(title)
        self._root.resizable(*resizable)
        self._root.config(bg=bg)
        self._root.geometry(geometry)
        self.__what_count: list[str, ...] = []
        self.answers: list[Number, ...] = []
        self.entry = CTkEntry(master=self._root, placeholder_text='Введите список чисел через запятую',
                              font=('Arial', 25), width=800)
        self.checkbox1 = CTkCheckBox(master=self._root, text='Мода', font=('Arial', 25), width=800, bg_color='#E0F2F7',
                                     command=lambda: self._what_count('Мода'))
        self.checkbox2 = CTkCheckBox(master=self._root, text='Медиана', font=('Arial', 25), width=800,
                                     bg_color='#E0F2F7', command=lambda: self._what_count('Медиана'))
        self.checkbox3 = CTkCheckBox(master=self._root, text='Размах', font=('Arial', 25), width=800,
                                     bg_color='#E0F2F7', command=lambda: self._what_count('Размах'))
        self.checkbox4 = CTkCheckBox(master=self._root, text='Среднее арифметическое', font=('Arial', 25), width=800,
                                     bg_color='#E0F2F7', command=lambda: self._what_count('Среднее арифметическое'))
        self.answer = CTkLabel(master=self._root, text='Ответ:', font=('Arial', 25), width=200, bg_color='#E0F2F7')
        self.box = CTkTextbox(master=self._root, font=('Arial', 25), width=800, height=370, bg_color='#E0F2F7',
                              fg_color='white', wrap='none', state='disabled')
        self.counting = CTkButton(master=self._root, text='Посчитать', font=('Arial', 25), width=200,
                                  bg_color='#E0F2F7', fg_color='darkblue', hover_color='#0089FF',
                                  command=lambda: self.__get_and_insert_data_from_entry())

    def __get_and_insert_data_from_entry(self):
        data = self.entry.get()
        self.answers = Answers(self.__what_count, data, add_name=True, course_of_the_decision=True).output()
        if len(self.__what_count) == 0:
            raise SelectError('Не выбрано ни одного варианта!')
        else:
            self.answer_name()
            self.output()
            self.entry.delete(0, END)
        return data

    def input_field(self):
        self.entry.grid(row=0, column=0)
        self.entry.bind('<Return>', lambda x: self.__get_and_insert_data_from_entry())

    def _what_count(self, value):
        if value not in self.__what_count:
            self.__what_count.append(value)
        else:
            self.__what_count.remove(value)

    def check_boxes(self):
        self.checkbox1.grid(row=1, column=0)
        self.checkbox2.grid(row=2, column=0)
        self.checkbox3.grid(row=3, column=0)
        self.checkbox4.grid(row=4, column=0)

    def answer_name(self):
        passer = CTkLabel(master=self._root, text='', font=('Arial', 25), width=800, bg_color='#E0F2F7')
        passer.grid(row=6, column=0)
        self.answer.grid(row=7, column=0)

    def output(self):
        self.box.grid(row=8, column=0)
        for i in self.answers:
            self.box.configure(state='normal')
            if i == 'Мода':
                if isinstance(self.answers[i], tuple) and len(self.answers[i]) == 2:
                    if len(self.answers[i][-1]) > 1:
                        self.box.insert(END, f'{i}: {self.answers[i][0]}{', '.join(map(str, self.answers[i][1]))}\n')
                    elif len(self.answers[i][-1]) == 1:
                        self.box.insert(END, f'{i}: {self.answers[i][0]}{self.answers[i][1][0]}\n')
                    else:
                        self.box.insert(END, f'{i}: {self.answers[i][0]}\n')
            elif i in ['Медиана', 'Размах', 'Среднее арифметическое']:
                if isinstance(self.answers[i], tuple) and len(self.answers[i]) == 2:
                    self.box.insert(END, f'{i}: {self.answers[i][0]}{self.answers[i][1]}\n')
            self.box.see(END)
            self.box.configure(state='disabled')

    def count_the_answer(self):
        self.counting.grid(row=5, column=0)

    def mainloop(self):
        self._root.mainloop()


root = Root(title='Калькулятор для ВиС', resizable=[False, False], bg='#E0F2F7', geometry='800x600')
root.input_field()
root.check_boxes()
root.count_the_answer()
root.mainloop()

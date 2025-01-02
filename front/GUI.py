from customtkinter import *


class Root:
    def __init__(self, *, title: str, resizable: list[bool, bool], bg: str, geometry: str):
        self._root = CTk()
        self._root.title(title)
        self._root.resizable(*resizable)
        self._root.config(bg=bg)
        self._root.geometry(geometry)

    def input_field(self):
        entry = CTkEntry(master=self._root, placeholder_text='Введите список чисел через запятую', font=('Arial', 25),
                         width=800)
        entry.grid(row=0, column=0)
        entry.bind('<Return>', lambda x: print(1))

    def check_boxes(self):
        CTkCheckBox(master=self._root, text='Мода', font=('Arial', 25), width=800, bg_color='#E0F2F7').grid(row=1,
                                                                                                            column=0)
        CTkCheckBox(master=self._root, text='Медиана', font=('Arial', 25), width=800, bg_color='#E0F2F7').grid(
            row=2, column=0)
        CTkCheckBox(master=self._root, text='Размах', font=('Arial', 25), width=800,
                    bg_color='#E0F2F7').grid(row=3,
                                             column=0)
        CTkCheckBox(master=self._root, text='Среднее арифметическое', font=('Arial', 25), width=800,
                    bg_color='#E0F2F7').grid(row=4,
                                             column=0)

    def count_the_answer(self):
        counting = CTkButton(master=self._root, text='Посчитать', font=('Arial', 25), width=200, bg_color='#E0F2F7',
                             fg_color='darkblue', hover_color='#0089FF')
        counting.grid(row=5, column=0)

    def mainloop(self):
        self._root.mainloop()


root = Root(title='Калькулятор для ВиС', resizable=[False, False], bg='#E0F2F7', geometry='800x600')
root.input_field()
root.check_boxes()
root.count_the_answer()
root.mainloop()

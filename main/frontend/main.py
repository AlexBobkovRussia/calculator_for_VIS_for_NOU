from customtkinter import CTk, CTkTextbox, CTkButton, CTkEntry
from collections import Counter
import statistics
from numbers import Number


class Root:
    def __init__(self, *, title: str, resizable: list[bool, bool], bg: str, geometry: str):
        self._root = CTk()
        self._root.title(title)
        self._root.resizable(*resizable)
        self._root.config(bg=bg)
        self._root.geometry(geometry)
        self.box = CTkTextbox(master=self._root, font=('Arial', 20), width=800, height=370, bg_color='#E0F2F7',
                              fg_color='red', wrap='none', state='disabled')
        self.moda = CTkButton(master=self._root, text='Мода', font=('Arial', 25), height=50, command=None)
        self.median = CTkButton(master=self._root, text='Медиана', font=('Arial', 20), height=50, command=None)
        self.avg = CTkButton(master=self._root, text='Среднее арифметическое', font=('Arial', 20), height=50, command=None)
        self.scope = CTkButton(master=self._root, text='Размах', font=('Arial', 20), height=50, command=None)
        self.entry = CTkEntry(master=self._root, placeholder_text='Введите числа через запятую', font=('Arial', 20), width=800, height=50)
        self.count = CTkButton(master=self._root, text='Сделать базовый расчет', font=('Arial', 20), height=50, command=None)

    def buttons(self):
        self.moda.grid(row=0, column=0, sticky='we', padx=(1, 1))
        self.median.grid(row=0, column=1, sticky='we', padx=(1, 1))
        self.avg.grid(row=0, column=2, sticky='we', padx=(1, 1))
        self.scope.grid(row=0, column=3, sticky='we', padx=(1, 1))
        self.count.grid(row=2, column=0, columnspan=4)

    def textbox(self):
        self.box.grid(row=3, column=0, columnspan=4)

    def place_entry(self):
        self.entry.grid(row=1, column=0, columnspan=4)

    def mainloop(self):
        self._root.mainloop()


root: Root = Root(title='Калькулятор для ВиС', resizable=[False, False], bg='#E0F2F7', geometry='800x520+300+170')
root.buttons()
root.place_entry()
root.textbox()
root.mainloop()

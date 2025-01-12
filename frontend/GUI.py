import tkinter.messagebox as messagebox

from customtkinter import CTk, CTkTextbox, CTkButton, CTkEntry, END

from backend import Mode, MainAccount, Storage, Median, Scope, Avg


class Root:
    def __init__(self, *, title: str, resizable: list[bool, bool], bg: str, geometry: str):
        self._root = CTk()
        self._root.title(title)
        self._root.resizable(*resizable)
        self._root.config(bg=bg)
        self._root.geometry(geometry)
        self._main_storage = Storage(None)
        self._mode_count = False
        self._median_count = False
        self._avg_count = False
        self._scope_count = False
        self.box = CTkTextbox(master=self._root, font=('Arial', 20), width=800, height=420, fg_color='#49B8DA',
                              wrap='none', state='disabled')
        self.moda = CTkButton(master=self._root, text='Мода', font=('Arial', 25), height=50, command=self.mode,
                              state='disabled')
        self.median = CTkButton(master=self._root, text='Медиана', font=('Arial', 20), height=50, command=self.median,
                                state='disabled')
        self.avg = CTkButton(master=self._root, text='Среднее арифметическое', font=('Arial', 20), height=50,
                             command=self.avg, state='disabled')
        self.scope = CTkButton(master=self._root, text='Размах', font=('Arial', 20), height=50, command=self.scope,
                               state='disabled')
        self.entry = CTkEntry(master=self._root, placeholder_text='Введите числа через запятую', font=('Arial', 20),
                              width=800, height=50)
        self.count = CTkButton(master=self._root, text='Сделать базовый расчет', font=('Arial', 20), height=50,
                               command=self.count_pressed, fg_color='#7300F6')
        self.cleaner = CTkButton(master=self._root, text='Очистить все', font=('Arial', 20), height=50,
                                 command=self.clean, fg_color='#7300F6')

    def clean(self):
        self._main_storage = Storage(None)
        self._mode_count = False
        self._median_count = False
        self._avg_count = False
        self._scope_count = False
        self.moda.configure(state='disabled')
        self.median.configure(state='disabled')
        self.avg.configure(state='disabled')
        self.scope.configure(state='disabled')
        self.entry.delete(0, END)
        self.box.configure(state='normal')
        self.box.delete('1.0', END)
        self.box.configure(state='disabled')

    def count_pressed(self):
        try:
            self._main_storage(self.input_data())
            data = self._main_storage
            self.box.configure(state='normal')
            self.box.insert(END, MainAccount(data).output() + '\n')
            self.box.configure(state='disabled')
            self.moda.configure(state='normal')
            self.median.configure(state='normal')
            self.avg.configure(state='normal')
            self.scope.configure(state='normal')
        except ValueError:
            messagebox.showerror("Ошибка", "Проверьте правильность ввода чисел")

    def mode(self):
        if not self._median_count:
            self.box.configure(state='normal')
            answer = Mode(self._main_storage.lst).answer
            if not answer:
                self.box.insert(END, f'Мода: МОДЫ НЕТ!\n')
            else:
                self.box.insert(END, f'\nМода: {', '.join(map(str, answer))}\n')
            self.box.configure(state='disabled')
            self._median_count = True

    def median(self):
        if not self._mode_count:
            self.box.configure(state='normal')
            answer = Median(self._main_storage.lst).answer
            self.box.insert(END, f'Медиана: {answer}\n')
            self.box.configure(state='disabled')
            self._mode_count = True

    def avg(self):
        if not self._avg_count:
            self.box.configure(state='normal')
            answer = Avg(self._main_storage.lst).step_by_step_answer
            self.box.insert(END, f'Среднее арифметическое: \n{answer}\n')
            self.box.configure(state='disabled')
            self._avg_count = True

    def scope(self):
        if not self._scope_count:
            self.box.configure(state='normal')
            answer = Scope(self._main_storage.lst).answer
            self.box.insert(END, f'Размах: {answer}\n')
            self.box.configure(state='disabled')
            self._scope_count = True

    def input_data(self):
        data = self.entry.get().split(', ')
        try:
            data = list(map(int, data))
        except ValueError:
            raise ValueError
        return list(map(int, data))

    def buttons(self):
        self.moda.grid(row=0, column=0, sticky='we', padx=(1, 1))
        self.median.grid(row=0, column=1, sticky='we', padx=(1, 1))
        self.avg.grid(row=0, column=2, sticky='we', padx=(1, 1))
        self.scope.grid(row=0, column=3, sticky='we', padx=(1, 1))
        self.count.grid(row=2, column=0, columnspan=2)
        self.cleaner.grid(row=2, column=2, columnspan=2)

    def textbox(self):
        self.box.grid(row=3, column=0, columnspan=4)

    def place_entry(self):
        self.entry.grid(row=1, column=0, columnspan=4)

    def mainloop(self):
        self._root.mainloop()


root: Root = Root(title='Калькулятор для ВиС', resizable=[False, False], bg='#58D0F5', geometry='800x570+300+170')
root.buttons()
root.place_entry()
root.textbox()
root.mainloop()


import customtkinter

def calculate():
    global history_text
    expression = "10 + 5"  # Или получение выражения из ввода
    result = 15
    history_text += f"{expression} = {result}\n"
    output_textbox.insert("end", f"{expression} = {result}\n")
    output_textbox.see("end") # Перемещаем скролл в конец

def main():
    window = customtkinter.CTk()
    window.geometry("400x300")
    global output_textbox
    global history_text
    history_text = ""

    calculate_button = customtkinter.CTkButton(window, text="Посчитать", command=calculate)
    calculate_button.pack(pady=20)

    output_textbox = customtkinter.CTkTextbox(window, width=350, height = 200)
    output_textbox.pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    main()

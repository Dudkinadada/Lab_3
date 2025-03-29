import tkinter as tk
from tkinter import messagebox
import math


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Научный калькулятор")
        self.root.geometry("400x600")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)

        entry = tk.Entry(entry_frame, textvariable=self.input_text, font=("Arial", 18), width=25, bd=5,
                         relief=tk.GROOVE)
        entry.grid(row=0, column=0)

        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('sin', 'cos', 'tan', 'sqrt'),
            ('log', 'ln', 'pi', 'C')
        ]

        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                button = tk.Button(button_frame, text=btn_text, font=("Arial", 14), width=5, height=2,
                                   command=lambda b=btn_text: self.on_button_click(b))
                button.grid(row=row_idx, column=col_idx, padx=5, pady=5)

    def on_button_click(self, button_text):
        try:
            if button_text == "=":
                self.expression = str(eval(self.expression))
            elif button_text == "C":
                self.expression = ""
            elif button_text == "sqrt":
                self.expression = str(math.sqrt(float(self.expression)))
            elif button_text == "sin":
                self.expression = str(math.sin(math.radians(float(self.expression))))
            elif button_text == "cos":
                self.expression = str(math.cos(math.radians(float(self.expression))))
            elif button_text == "tan":
                self.expression = str(math.tan(math.radians(float(self.expression))))
            elif button_text == "log":
                self.expression = str(math.log10(float(self.expression)))
            elif button_text == "ln":
                self.expression = str(math.log(float(self.expression)))
            elif button_text == "pi":
                self.expression += str(math.pi)
            else:
                self.expression += button_text

            self.input_text.set(self.expression)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Неверный ввод: {e}")
            self.expression = ""
            self.input_text.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()

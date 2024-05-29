import tkinter as tk
from PIL import Image, ImageTk, ImageGrab


def create_widgets(self):
    entry = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
    entry.grid(row=0, column=0, columnspan=4)

def create_button(self, value, row, col):
        button = tk.Button(self.root, text=value, font=('Arial', 18), command=lambda: self.on_button_click(value))
        button.grid(row=row, column=col, sticky="nsew")

def on_button_click(self, value):
    current_text = self.result_var.get()
    
    if value == 'DEL':
        self.result_var.set(current_text[:-1])
    elif value == 'AC':
        self.result_var.set("")
    elif value == ':-)':
        self.flip_window()
    elif value == 'ANS':
        self.result_var.set(current_text + self.previous_answer)
    elif value == '=':
        try:
            result = str(eval(current_text))
            self.previous_answer = result
            self.result_var.set(result)
        except:
            self.result_var.set("Error")
    else:
        new_text = current_text + value
        self.result_var.set(new_text)

def flip_window(self):
    
    width = self.root.winfo_width()
    height = self.root.winfo_height()

    x = self.root.winfo_rootx()
    y = self.root.winfo_rooty()
    x1 = x + width
    y1 = y + height
    image = ImageGrab.grab().crop((x, y, x1, y1))

    flipped_image = image.rotate(180)

    tk_image = ImageTk.PhotoImage(flipped_image)

    flipped_window = tk.Toplevel()
    flipped_window.geometry(f"{width}x{height}")
    tk.Label(flipped_window, image=tk_image).pack()
    flipped_window.mainloop()



class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        
        self.root.geometry("320x420")
        self.root.resizable(False, False)
        
        self.result_var = tk.StringVar()
        self.previous_answer = ''
        
        self.create_widgets()
    
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'AC', 'DEL', 'ANS', ':-)',
        ]
        
        row_val = 1
        col_val = 0
        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1, uniform="button")
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1, uniform="button")


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

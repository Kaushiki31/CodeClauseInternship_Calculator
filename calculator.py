import tkinter as tk
from math import *

def evaluate_expression(expression, degree_mode):
    try:
        if degree_mode:
            result = str(eval(expression, {'sin': lambda x: sin(radians(x)),
                                           'cos': lambda x: cos(radians(x)),
                                           'tan': lambda x: tan(radians(x)),
                                           'sqrt': lambda x: sqrt(x)}))
        else:
            result = str(eval(expression, {'sqrt': lambda x: sqrt(x)}))
        return result
    except Exception as e:
        return "Error"

def on_button_click(value):
    current_expression = entry_var.get()
    if value == 'C':
        entry_var.set("")
    elif value == 'DEL':
        entry_var.set(current_expression[:-1])
    elif value == '=':
        result = evaluate_expression(current_expression, degree_mode.get())
        entry_var.set(result)
    else:
        entry_var.set(current_expression + str(value))

# Create the main window
calculator_window = tk.Tk()
calculator_window.title("Scientific Calculator")

# Entry widget to display the expression
entry_var = tk.StringVar()
entry = tk.Entry(calculator_window, textvariable=entry_var, font=('Arial', 18), bd=10, insertwidth=4, width=15, justify='right')
entry.grid(row=0, column=0, columnspan=7)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]

# Function to create and configure buttons
def create_button(value, row, col):
    return tk.Button(calculator_window, text=value, command=lambda: on_button_click(value),
                     font=('Arial', 14), padx=20, pady=20).grid(row=row, column=col)

# Create and configure buttons
row_val = 1
col_val = 0
for button_value in buttons:
    create_button(button_value, row_val, col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Trigonometric functions
sin_button = tk.Button(calculator_window, text='sin', command=lambda: on_button_click('sin('),
                       font=('Arial', 14), padx=20, pady=20).grid(row=4, column=4)
cos_button = tk.Button(calculator_window, text='cos', command=lambda: on_button_click('cos('),
                       font=('Arial', 14), padx=20, pady=20).grid(row=4, column=5)
tan_button = tk.Button(calculator_window, text='tan', command=lambda: on_button_click('tan('),
                       font=('Arial', 14), padx=20, pady=20).grid(row=4, column=6)

# Additional buttons
sqrt_button = tk.Button(calculator_window, text='sqrt', command=lambda: on_button_click('sqrt('),
                       font=('Arial', 14), padx=20, pady=20).grid(row=2, column=6)
open_parenthesis_button = tk.Button(calculator_window, text='(', command=lambda: on_button_click('('),
                                    font=('Arial', 14), padx=20, pady=20).grid(row=3, column=4)
close_parenthesis_button = tk.Button(calculator_window, text=')', command=lambda: on_button_click(')'),
                                     font=('Arial', 14), padx=20, pady=20).grid(row=3, column=5)

# Clear buttons
clear_button = tk.Button(calculator_window, text='C', command=lambda: on_button_click('C'),
                         font=('Arial', 14), padx=20, pady=20).grid(row=1, column=4)
del_button = tk.Button(calculator_window, text='DEL', command=lambda: on_button_click('DEL'),
                       font=('Arial', 14), padx=20, pady=20).grid(row=1, column=5)

# Degree/Radian mode
degree_mode = tk.BooleanVar()
degree_mode.set(True)  # Default: Degree mode
degree_button = tk.Radiobutton(calculator_window, text='Degree', variable=degree_mode, value=True,
                               font=('Arial', 14)).grid(row=2, column=4)
radian_button = tk.Radiobutton(calculator_window, text='Radian', variable=degree_mode, value=False,
                                font=('Arial', 14)).grid(row=2, column=5)

# Start the main loop
calculator_window.mainloop()

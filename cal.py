import tkinter as tk
from tkinter import messagebox

def clear_display():
    display_var.set("")

def button_click(value):
    current_text = display_var.get()
    display_var.set(current_text + str(value))

def calculate():
    try:
        # Extract numbers and operation from the display
        expression = display_var.get()
        result = eval(expression)
        display_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        display_var.set("")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Display for showing input and result
display_var = tk.StringVar()
entry = tk.Entry(root, textvariable=display_var, font=("Arial", 20), justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=("Arial", 18), command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, font=("Arial", 18), command=clear_display)
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5)

# Run the application
root.mainloop()

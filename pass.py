import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a strong password
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 6:
            messagebox.showerror("Error", "Password length must be at least 6.")
            return
        char_pool = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(char_pool) for _ in range(length))
        entry_password.delete(0, tk.END)  # Clear previous password
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")

# Function to copy the password to the clipboard
def copy_password():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Keeps clipboard data available even after the program closes
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)

# Title Label
label_title = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# Input for password length
frame_length = tk.Frame(root)
frame_length.pack(pady=10)
label_length = tk.Label(frame_length, text="Number of characters:")
label_length.pack(side=tk.LEFT, padx=5)
entry_length = tk.Entry(frame_length, width=10)
entry_length.pack(side=tk.LEFT)

# Button to generate a strong password
button_generate = tk.Button(root, text="Generate Strong Password", command=generate_password)
button_generate.pack(pady=10)

# Entry to display the generated password
entry_password = tk.Entry(root, width=40, font=("Arial", 12), justify="center")
entry_password.pack(pady=10)

# Button to copy the password to the clipboard
button_copy = tk.Button(root, text="Copy Password", command=copy_password)
button_copy.pack(pady=10)

# Run the application
root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import time

# Initialize the main application window
app = tk.Tk()
app.title("To-Do List Application")
app.geometry("500x600")

# Global list to store tasks and their reminders
tasks = []  # List of tuples (serial_number, task, reminder_time)

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        serial_number = len(tasks) + 1
        tasks.append((serial_number, task, None))  # None indicates no reminder yet
        update_task_list()
        task_entry.delete(0, tk.END)

# Function to delete a selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        removed_task = tasks.pop(selected_task_index[0])
        update_task_list()
        messagebox.showinfo("Task Deleted", f"Task '{removed_task[1]}' deleted successfully!")
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to set a reminder for a task
def set_reminder():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        reminder_time = simpledialog.askinteger("Set Reminder", "Enter reminder time in seconds:")
        if reminder_time:
            task = tasks[selected_task_index[0]]
            tasks[selected_task_index[0]] = (task[0], task[1], reminder_time)
            messagebox.showinfo("Reminder Set", f"Reminder set for '{task[1]}' in {reminder_time} seconds.")
            threading.Thread(target=start_reminder, args=(task[1], reminder_time)).start()
    else:
        messagebox.showwarning("Warning", "Please select a task to set a reminder!")

# Function to start a reminder
def start_reminder(task, reminder_time):
    time.sleep(reminder_time)
    messagebox.showinfo("Reminder", f"Time's up for your task: {task}")

# Function to update the task listbox with current tasks
def update_task_list():
    task_listbox.delete(0, tk.END)  # Clear the listbox
    for task in tasks:
        serial_number, task_text, reminder = task
        reminder_info = f" (Reminder in {reminder}s)" if reminder else ""
        task_listbox.insert(tk.END, f"{serial_number}. {task_text}{reminder_info}")

# GUI Layout
# Input field and Add button
task_entry = tk.Entry(app, font=("Arial", 14))
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task, bg="green", fg="white", font=("Arial", 12))
add_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(app, font=("Arial", 14), width=50, height=15)
task_listbox.pack(pady=10)

# Buttons for delete and reminder
delete_button = tk.Button(app, text="Delete Task", command=delete_task, bg="red", fg="white", font=("Arial", 12))
delete_button.pack(pady=5)

reminder_button = tk.Button(app, text="Set Reminder", command=set_reminder, bg="blue", fg="white", font=("Arial", 12))
reminder_button.pack(pady=5)


app.mainloop()

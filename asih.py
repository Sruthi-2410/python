import tkinter as tk
from tkinter import messagebox


def save_data():
    routine = routine_text.get("1.0", "end-1c")
    todo = todo_entry.get()
    reminder = reminder_entry.get()

    # Here you could write to a file or database
    print("Routine:", routine)
    print("To-Do:", todo)
    print("Reminder:", reminder)

    messagebox.showinfo("Saved", "Your daily schedule has been saved!")


# Setup main window
root = tk.Tk()
root.title("Daily Planner")
root.geometry("400x400")

# Routine
tk.Label(root, text="Daily Routine:").pack()
routine_text = tk.Text(root, height=5, width=40)
routine_text.pack()

# To-do list
tk.Label(root, text="To-Do Item:").pack()
todo_entry = tk.Entry(root, width=40)
todo_entry.pack()

# Reminder
tk.Label(root, text="Reminder:").pack()
reminder_entry = tk.Entry(root, width=40)
reminder_entry.pack()

# Save Button
save_button = tk.Button(root, text="Save", command=save_data)
save_button.pack(pady=10)

root.mainloop()
import tkinter as tk
from tkinter import messagebox
import sqlite3

# --- Database setup ---
conn = sqlite3.connect('plants.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS plants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    count INTEGER
)''')
conn.commit()

# --- Main Application ---
def add_plant():
    name = name_entry.get()
    type_ = type_entry.get()
    count = count_entry.get()
    if name and type_ and count.isdigit():
        c.execute("INSERT INTO plants (name, type, count) VALUES (?, ?, ?)",
                  (name, type_, int(count)))
        conn.commit()
        messagebox.showinfo("Success", "Plant added")
        show_plants()
    else:
        messagebox.showerror("Error", "Invalid input")

def update_plant():
    try:
        pid = int(id_entry.get())
        new_count = count_entry.get()
        if new_count.isdigit():
            c.execute("UPDATE plants SET count=? WHERE id=?", (int(new_count), pid))
            conn.commit()
            messagebox.showinfo("Success", "Plant updated")
            show_plants()
        else:
            messagebox.showerror("Error", "Enter valid count")
    except ValueError:
        messagebox.showerror("Error", "Enter valid ID")

def delete_plant():
    try:
        pid = int(id_entry.get())
        c.execute("DELETE FROM plants WHERE id=?", (pid,))
        conn.commit()
        messagebox.showinfo("Success", "Plant deleted")
        show_plants()
    except ValueError:
        messagebox.showerror("Error", "Enter valid ID")

def show_plants():
    listbox.delete(0, tk.END)
    for row in c.execute("SELECT * FROM plants"):
        listbox.insert(tk.END, f"ID: {row[0]} | Name: {row[1]} | Type: {row[2]} | Count: {row[3]}")

# --- GUI ---
root = tk.Tk()
root.title("Plant Management System")

tk.Label(root, text="Plant Name").grid(row=0, column=0)
tk.Label(root, text="Plant Type").grid(row=1, column=0)
tk.Label(root, text="Count").grid(row=2, column=0)
tk.Label(root, text="Plant ID (for Update/Delete)").grid(row=3, column=0)

name_entry = tk.Entry(root)
type_entry = tk.Entry(root)
count_entry = tk.Entry(root)
id_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
type_entry.grid(row=1, column=1)
count_entry.grid(row=2, column=1)
id_entry.grid(row=3, column=1)

tk.Button(root, text="Add Plant", command=add_plant).grid(row=0, column=2)
tk.Button(root, text="Update Count", command=update_plant).grid(row=1, column=2)
tk.Button(root, text="Delete Plant", command=delete_plant).grid(row=2, column=2)
tk.Button(root, text="Show Plants", command=show_plants).grid(row=3, column=2)

listbox = tk.Listbox(root, width=50)
listbox.grid(row=4, column=0, columnspan=3)

show_plants()
root.mainloop()
conn.close()

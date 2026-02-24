import tkinter as tk
from tkinter import messagebox
import sqlite3

# Initialize DB
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        email TEXT,
        mobile TEXT,
        username TEXT UNIQUE,
        password TEXT
    )
''')
conn.commit()
conn.close()

# Signup function
def signup():
    name = entry_name.get()
    email = entry_email.get()
    mobile = entry_mobile.get()
    username = entry_username.get()
    password = entry_password.get()

    if not (name and email and mobile and username and password):
        messagebox.showerror("Error", "All fields are required")
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, mobile, username, password) VALUES (?, ?, ?, ?, ?)",
                       (name, email, mobile, username, password))
        conn.commit()
        messagebox.showinfo("Success", "Signup successful")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")
    conn.close()

# Login function
def login():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Success", "Login successful")
    else:
        messagebox.showerror("Error", "Invalid credentials")

# GUI
root = tk.Tk()
root.title("Signup and Login")
root.geometry("300x400")

# Signup Fields
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Mobile Number").pack()
entry_mobile = tk.Entry(root)
entry_mobile.pack()

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Buttons
tk.Button(root, text="Signup", command=signup).pack(pady=5)
tk.Button(root, text="Login", command=login).pack()

root.mainloop()

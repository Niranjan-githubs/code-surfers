import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_table():
    conn = sqlite3.connect('userdetails.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS details (
                        ID INTEGER PRIMARY KEY,
                        NAME TEXT NOT NULL,
                        PASSWORD TEXT NOT NULL,
                        PRIVILEGE TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_user_details(username, password, privilege):
    conn = sqlite3.connect('userdetails.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO details (NAME, PASSWORD, PRIVILEGE) VALUES (?, ?, ?)", (username, password, privilege))
    conn.commit()
    conn.close()

def check_credentials(username, password):
    conn = sqlite3.connect('userdetails.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM details WHERE NAME= ? AND PASSWORD= ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

def add_new_user():
    username = entry_username.get()
    password = entry_password.get()
    user = check_credentials(username, password)
    print("User:", user)
    if user and len(user) >= 4:  # Check if user exists and tuple has enough elements
        privilege = user[3]
        if privilege == "admin":
            new_username = entry_new_username.get()
            new_password = entry_new_password.get()
            if new_username and new_password:
                add_user_details(new_username, new_password, "user")
                messagebox.showinfo("Success", "User details added successfully!")
            else:
                messagebox.showerror("Error", "New username and password cannot be empty.")
        else:
            messagebox.showerror("Error", "You do not have the privilege to add new users.")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

def login():
    username = entry_username.get()
    password = entry_password.get()
    user = check_credentials(username, password)
    if user:
        messagebox.showinfo("Success", f"Welcome {username}! You are logged in as {user[3]}.")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

create_table()
root = tk.Tk()
root.title("User Authentication")

label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=5, pady=5)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

button_login = tk.Button(root, text="Login", command=login)
button_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

label_new_username = tk.Label(root, text="New Username:")
label_new_username.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_new_username = tk.Entry(root)
entry_new_username.grid(row=3, column=1, padx=5, pady=5)

label_new_password = tk.Label(root, text="New Password:")
label_new_password.grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry_new_password = tk.Entry(root, show="*")
entry_new_password.grid(row=4, column=1, padx=5, pady=5)

button_add_user = tk.Button(root, text="Add User", command=add_new_user)
button_add_user.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

root.mainloop()

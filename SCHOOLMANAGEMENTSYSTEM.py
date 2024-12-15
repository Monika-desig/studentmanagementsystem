import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create/connect to the database
def create_db():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no INTEGER NOT NULL,
            class TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a student to the database
def add_student():
    name = name_entry.get()
    roll_no = roll_no_entry.get()
    class_name = class_entry.get()

    if not name or not roll_no or not class_name:
        messagebox.showerror("Input Error", "Please fill all fields")
        return
    
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('INSERT INTO students (name, roll_no, class) VALUES (?, ?, ?)', 
              (name, roll_no, class_name))
    conn.commit()
    conn.close()

    # Clear the fields
    name_entry.delete(0, tk.END)
    roll_no_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Student added successfully")

# Function to search for a student by roll number
def search_student():
    roll_no = roll_no_entry.get()

    if not roll_no:
        messagebox.showerror("Input Error", "Please enter a roll number")
        return
    
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students WHERE roll_no=?', (roll_no,))
    student = c.fetchone()
    conn.close()

    if student:
        name_entry.delete(0, tk.END)
        roll_no_entry.delete(0, tk.END)
        class_entry.delete(0, tk.END)

        name_entry.insert(0, student[1])
        roll_no_entry.insert(0, student[2])
        class_entry.insert(0, student[3])
    else:
        messagebox.showerror("Student Not Found", "No student found with this roll number")

# Function to update student data
def update_student():
    name = name_entry.get()
    roll_no = roll_no_entry.get()
    class_name = class_entry.get()

    if not name or not roll_no or not class_name:
        messagebox.showerror("Input Error", "Please fill all fields")
        return

    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('UPDATE students SET name=?, class=? WHERE roll_no=?', 
              (name, class_name, roll_no))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student data updated successfully")

# Function to delete student data
def delete_student():
    roll_no = roll_no_entry.get()

    if not roll_no:
        messagebox.showerror("Input Error", "Please enter a roll number")
        return

    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('DELETE FROM students WHERE roll_no=?', (roll_no,))
    conn.commit()
    conn.close()

    name_entry.delete(0, tk.END)
    roll_no_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Student data deleted successfully")

# GUI Setup
root = tk.Tk()
root.title("School Management System")
root.geometry("400x300")

# Create the database if not exists
create_db()

# Create widgets
tk.Label(root, text="Name:", font=("Arial", 12)).pack(pady=10)
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

tk.Label(root, text="Roll Number:", font=("Arial", 12)).pack(pady=10)
roll_no_entry = tk.Entry(root, font=("Arial", 12))
roll_no_entry.pack(pady=5)

tk.Label(root, text="Class:", font=("Arial", 12)).pack(pady=10)
class_entry = tk.Entry(root, font=("Arial", 12))
class_entry.pack(pady=5)

# Buttons
add_button = tk.Button(root, text="Add Student", command=add_student, font=("Arial", 12))
add_button.pack(pady=5)

search_button = tk.Button(root, text="Search Student", command=search_student, font=("Arial", 12))
search_button.pack(pady=5)

update_button = tk.Button(root, text="Update Student", command=update_student, font=("Arial", 12))
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Student", command=delete_student, font=("Arial", 12))
delete_button.pack(pady=5)

root.mainloop()

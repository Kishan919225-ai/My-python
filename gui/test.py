import tkinter as tk
from tkinter import messagebox

def submit():
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()

    # Basic validation
    if not name or not age or not email:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    # You can process/store the data here
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    messagebox.showinfo("Success", "Data submitted successfully!")

# Create main window
root = tk.Tk()
root.title("User Info Form")
root.geometry("300x250")

# Name
tk.Label(root, text="Name").pack(pady=(10, 0))
entry_name = tk.Entry(root, width=30)
entry_name.pack()

# Age
tk.Label(root, text="Age").pack(pady=(10, 0))
entry_age = tk.Entry(root, width=30)
entry_age.pack()

# Email
tk.Label(root, text="Email").pack(pady=(10, 0))
entry_email = tk.Entry(root, width=30)
entry_email.pack()

# Submit Button
tk.Button(root, text="Submit", command=submit).pack(pady=20)

# Start the GUI loop
root.mainloop()

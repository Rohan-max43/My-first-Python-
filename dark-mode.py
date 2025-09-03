# hello I'm dark-mode
import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Dark Theme Example")
root.geometry("400x200")
root.configure(bg="#000000")  # Dark background

# Style for ttk widgets
style = ttk.Style()
style.theme_use('clam')  # Use clam theme to allow custom colors
style.configure('TButton', background='#444444', foreground='white')
style.configure('TLabel', background='#2e2e2e', foreground='white')

# Add a label
label = ttk.Label(root, text="Welcome to Dark Theme!", font=("Arial", 16))
label.pack(pady=20)

# Add a button
button = ttk.Button(root, text="Click Me")
button.pack(pady=10)

# Run the GUI
root.mainloop()

# I hope it's help you.
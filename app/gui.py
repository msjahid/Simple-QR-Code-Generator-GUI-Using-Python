import tkinter as tk

class GUI:
    def __init__(self, root, entry_callback, button_callback):
        self.root = root
        self.entry_callback = entry_callback
        self.button_callback = button_callback
        self.root.title("Bar Code Generator")
        self.root.geometry("495x565")
        self.entry = self.create_entry()
        self.create_button()

    def create_entry(self):
        entry = tk.Entry(self.root, bd=1)
        entry.insert(0, 'Enter your Link')
        entry.bind('<FocusIn>', self.entry_callback)
        entry.bind('<FocusOut>', self.entry_callback)
        entry.config(fg='grey')
        entry.pack()
        return entry

    def create_button(self):
        button = tk.Button(self.root, text="Generate", command=self.button_callback)
        button.pack()
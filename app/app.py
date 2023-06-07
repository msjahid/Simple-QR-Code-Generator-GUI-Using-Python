from gui import GUI
from qr_code import QRCode
import tkinter as tk

class QRCodeApp:
    def __init__(self, root):
        self.qr_code = QRCode()
        self.gui = GUI(root, self.on_entry_click, self.generate_qr_code)
        self.photo = None

    def on_entry_click(self, event):
        if self.gui.entry.get() == 'Enter your Link':
            self.gui.entry.delete(0, "end")
            self.gui.entry.insert(0, '')
            self.gui.entry.config(fg='black')

    def on_focusout(self, event):
        if self.gui.entry.get() == '':
            self.gui.entry.insert(0, 'Enter your Link')
            self.gui.entry.config(fg='grey')

    def generate_qr_code(self):
        data = self.gui.entry.get()
        if self.qr_code.generate_qr_code(data):
            self.display_qr_code()

    def display_qr_code(self):
        cv = tk.Canvas(self.gui.root,  width=200, height=100)
        cv.pack(side='top', fill='both', expand=1)
        self.photo = tk.PhotoImage(file="qcode.png")
        cv.create_image(0, 0, image=self.photo, anchor="nw")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
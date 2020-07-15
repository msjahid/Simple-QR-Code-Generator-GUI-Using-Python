from tkinter import *
from PIL import ImageTk, Image, ImageDraw
import qrcode


def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if entry.get() == 'Enter your Link':
        entry.delete(0, "end")  # delete all the text in the entry
        entry.insert(0, '')  # Insert blank for user input
        entry.config(fg='black')


def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Enter your Link')
        entry.config(fg='grey')


root = Tk()
root.title("Bar Code Generator")
root.geometry("495x565")

label = Label(root, text="Link: ")
label.pack()

entry = Entry(root, bd=1)
entry.insert(0, 'Enter your Link')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.config(fg='grey')
entry.pack()


def myClick():
    data = entry.get()
    img = qrcode.make(data)
    img = img.resize((490, 490), Image.ANTIALIAS)
    img.save('qcode.png')
    # photo = PhotoImage(file="qcode.png")
    # imag = Label(root, image=photo)
    # imag.pack()
    cv = Canvas(root,  width=200, height=100)
    cv.pack(side='top', fill='both', expand='yes')
    cv.photo = PhotoImage(file="qcode.png")
    cv.create_image(0, 0, image=cv.photo, anchor="nw")
    # cv.create_image(10, 10, image=img, anchor='nw')


MyButton = Button(root, text="Generate", command=myClick)
MyButton.pack()


root.mainloop()

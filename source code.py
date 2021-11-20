# made by akarsh (12012736)
from tkinter import *
from tkinter import messagebox

import os
import pyqrcode

window = Tk()
window.title("QR Code Generator")



def generate():
    if len(Subject.get()) != 0:
        global qr, photo
        qr = pyqrcode.create(Subject.get())
        photo = BitmapImage(data=qr.xbm(scale=8))
    else:
        messagebox.showinfo("Please Enter Details: ")
    try:
        showcode()
    except:
        messagebox.showinfo("", "Nothing is entered")


def showcode():
    imageLabel.config(image=photo)
    subLabel.config(text="QR of " + Subject.get())


def save():
    dir = "QR_Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get()) != 0 and name.get() != "Enter filename here":
            if s == 0:
                messagebox.showinfo("alert", "Select size first")
            else:
                version, level, qr = myqr.run(Subject.get(), version=1, level='H', picture=filename, colorized=True,
                                              contrast=1.0, brightness=1.0, save_name=name.get() + ".png",
                                              save_dir=os.path.join(os.getcwd(), "QR_Codes"))
                os.remove(os.path.join("src", name.get()) + ".png")
                messagebox.showinfo("", "Saved")
        else:
            messagebox.showinfo("", "Please enter a File Name")
    except:
        messagebox.showinfo("", "File Saved!")


# made by akarsh (12012736)
Sub = Label(window, text="Enter subject")
Sub.grid(row=0, column=0, sticky=N + S + W + E)

FName = Label(window, text="Enter FileName")
FName.grid(row=1, column=0, sticky=N + S + W + E)

Subject = StringVar()
SubEntry = Entry(window, textvariable=Subject)
SubEntry.grid(row=0, column=1, sticky=N + S + W + E)

name = StringVar()
nameEntry = Entry(window, textvariable=name)
nameEntry.grid(row=1, column=1, sticky=N + S + W + E)

button = Button(window, text="Generate", width=15, command=generate)
button.grid(row=0, column=3, sticky=N + S + W + E)

imageLabel = Label(window)
imageLabel.grid(row=2, column=1, sticky=N + S + W + E)
subLabel = Label(window, text="")
subLabel.grid(row=3, column=1, sticky=N + S + W + E)

saveB = Button(window, text="Save as PNG", width=15, command=save)
saveB.grid(row=1, column=3, sticky=N + S + W + E)

Rows = 3
Columns = 3
for row in range(Rows + 1):
    window.grid_rowconfigure(row, weight=1)

for col in range(Columns + 1):
    window.grid_columnconfigure(col, weight=1)

window.mainloop()
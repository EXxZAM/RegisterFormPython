from tkinter import *
import tkinter.messagebox as messagebox
import sqlite3
import os
from PIL import ImageTk, Image

root = Tk()
root.geometry('1000x500')
root.title('Main Page')

# Welcome Message
welcomeL = Label(root,text='Please register or login to your account', bg='#16B078', width=len('Please register or login to your account')+10, pady=10)
welcomeL.place(relx=0.5, rely=0.3, anchor=CENTER)


# functions

def register():
    root.destroy()
    os.system('python register.py')

def login():
    pass


#Buttons
registerB = Button(root, text='Register', command=register, padx=10, bg='#06874A')
registerB.place(relx=0.6, rely=0.4, anchor=CENTER)


loginB = Button(root, text='Login', command=login, width=10, bg='#ABB016')
loginB.place(relx=0.4, rely=0.4, anchor=CENTER)



# Image
image = Image.open('image.jpg')
image = image.resize((100, 100), Image.ANTIALIAS)
userIMG = ImageTk.PhotoImage(image)

img_label = Label(root, image=userIMG)
img_label.place(relx=0.5, rely=0.12, anchor=CENTER)
root.mainloop()
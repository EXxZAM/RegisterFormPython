from tkinter import *
import tkinter.messagebox as messagebox
import sqlite3
import os
from PIL import ImageTk, Image

root = Tk()
root.geometry('1000x500')
root.title('Profile Page')

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('SELECT * FROM user_profile')
results = c.fetchall()

if results:
    for i in results:
        profileName = i[0]
        profileLastName = i[1]
        profileEmail = i[2]
        
conn.commit()
conn.close()




welcomeL = Label(root, text='Welcome to your profile {}! Have a nice day'.format(profileName), bg='#16B078',width=50, pady=10)

nameL = Label(root, text=profileName, bg='#9D7FE8', width=len(profileName)+10, pady=10)

lastnameL = Label(root, text=profileLastName, bg='#9D7FE8', width=len(profileLastName)+10, pady=10)

emailL = Label(root, text=profileEmail, bg='#9D7FE8', width=len(profileEmail)+10, pady=10)


welcomeL.place(relx=0.5, rely=0.1, anchor=CENTER)
nameL.place(relx=0.5, rely=0.2, anchor=CENTER)
lastnameL.place(relx=0.5, rely=0.25, anchor=CENTER)
emailL.place(relx=0.5, rely=0.3, anchor=CENTER)

def exit():
    root.destroy()

def logout():
    root.destroy()
    os.system('python main.py')

exitB = Button(root, text='Exit App', command=exit, bg='#ABB016')

logoutB =Button(root, text='Log Out', command=logout, bg='#ABB016')

exitB.place(relx=0.7, rely=0.4, anchor=CENTER)
logoutB.place(relx=0.3, rely=0.4, anchor=CENTER)

root.mainloop()
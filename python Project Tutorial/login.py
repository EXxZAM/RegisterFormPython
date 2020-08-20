from tkinter import *
import tkinter.messagebox as messagebox
import sqlite3
import os
from PIL import ImageTk, Image


# conn = sqlite3.connect('users.db')

# c = conn.cursor()

# c.execute("""CREATE TABLE user_profile (
#          name text,
#          lastname text,
#          email text
         
#          ) """)

# conn.commit()
# conn.close()




root = Tk()
root.geometry('1000x500')
root.title('Login Page')

emailL = Label(root, text='Email :', pady=10)
passL = Label(root, text='Password :', pady=10)


emailE = Entry(root, bg='#AEAEAE')
passE = Entry(root, bg='#AEAEAE')

# Functions
def login():
    email_login = emailE.get()
    pass_login = passE.get()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM user_info WHERE email = ? AND password = ?',(email_login,pass_login,))
    results = c.fetchall()

    if results:
        for i in results:
            messagebox.showinfo('Login Warning', 'Welcome, {} {}'.format(i[0], i[1]))
            userNameLog = str(i[0])
            userLastNameLog = str(i[1])
            userEmailLog = str(i[2])
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('INSERT INTO user_profile VALUES (:nameProfile, :lastnameProfile, :emailProfile)',
                {
                    'nameProfile':userNameLog,
                    'lastnameProfile':userLastNameLog,
                    'emailProfile':userEmailLog,
                })
        conn.commit()
        conn.close()

        root.destroy()
        os.system('python profile.py')
    else:
        messagebox.showinfo('Login Warning', 'Password or Email is incorrect')
    
    conn.commit()
    conn.close()









def register():
    root.destroy()
    os.system('python register.py')



emailL.grid(row=0 , column=0)
emailE.grid(row=0 , column=1)
passL.grid(row=1 , column=0)
passE.grid(row=1 , column=1)



loginB= Button(root, text='Login', command=login, padx=10, bg='#06874A',fg='white')
registerB= Button(root, text='Register', command=register, padx=10, bg='#06874A',fg='white')

loginB.grid(row=2, column=1, columnspan=1)
registerB.grid(row=3, column=1, columnspan=1)

root.mainloop()
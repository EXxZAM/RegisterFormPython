from tkinter import *
import tkinter.messagebox as messagebox
import sqlite3
import os
from PIL import ImageTk, Image

root = Tk()
root.geometry('1000x500')
root.title('Register Form')

# conn = sqlite3.connect('users.db')

# c = conn.cursor()

# c.execute("""CREATE TABLE user_info (
#          name text,
#          lastname text,
#          email text,
#          password text
#          ) """)

# conn.commit()
# conn.close()

#Functions
def emptyError():
    messagebox.showinfo('Warning!','Fill Out every single entry')
def passError():
    messagebox.showinfo('Warning!','Passwords Do not match')

def register():
    name = nameE.get()
    lastname = lastnameE.get()
    email = emailE.get()
    password = passE.get()
    password2 = retrypassE.get()

    def add_user():
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('INSERT INTO user_info VALUES (:Username, :Userlastname, :Useremail, :Userpassword)',
            {
                'Username': name,
                'Userlastname': lastname,
                'Useremail': email,
                'Userpassword': password,
                
            })

        conn.commit()
        conn.close()
        messagebox.showinfo('Warning!','You registered succesfully')
        root.destroy()
        os.system('python login.py')

    # Conditions

    if len(name) == 0 or len(lastname) == 0 or len(email) == 0 or len(password) == 0 or len(password2) == 0:
        emptyError()
    elif password != password2:
        passError()
    elif len(password) < 8:
        messagebox.showinfo('Warning!','Passwords must have over 8 characters')
    else:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT email FROM user_info WHERE email=?',(email,))
        exists = c.fetchall()
        if not exists:
            add_user()
        else:
            messagebox.showinfo('Warning!','Email is taken, Try another email')


        conn.commit()
        conn.close()






#Labels
nameL = Label(root, text='Name : ',pady=10)
lastnameL = Label(root, text='Last Name : ',pady=10)
emailL = Label(root, text='Email : ',pady=10)
passL = Label(root, text='Password : ',pady=10)
retrypassL = Label(root, text='Confirm Password : ',pady=10)

#Entries
nameE = Entry(root, bg='#AEAEAE')
lastnameE = Entry(root, bg='#AEAEAE')
emailE = Entry(root, bg='#AEAEAE')
passE = Entry(root, bg='#AEAEAE')
retrypassE = Entry(root, bg='#AEAEAE')
# Grids
nameL.grid(row=1 ,column=0 )
nameE.grid(row=1, column=1)

lastnameL.grid(row=2 ,column=0 )
lastnameE.grid(row=2, column=1)

emailL.grid(row=3 ,column=0 )
emailE.grid(row=3, column=1)

passL.grid(row=4 ,column=0 )
passE.grid(row=4, column=1)

retrypassL.grid(row=5 ,column=0 )
retrypassE.grid(row=5, column=1)


def login():
    root.destroy()
    os.system('python login.py')



registerB = Button(root, text='Register', command=register, padx=10, bg='#06874A', fg='white')
registerB.grid(row=6, column=1, columnspan=1)

loginB = Button(root, text='Login', command=login, padx=10, bg='#ABB016', fg='black')
loginB.grid(row=7, column=1, columnspan=1)


root.mainloop()
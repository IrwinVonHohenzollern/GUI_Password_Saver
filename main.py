from tkinter import *
from tkinter import messagebox
import string as st
from random import choice, randint
import pyperclip
import json


POSSIBLE_SYMBOLS = st.ascii_letters + st.digits + '!?.,@#$%*'

WHITE = '#FFFFFF'
FONT = ('Arial', '10', 'normal')
MY_EMAIL = 'my_email@gmail.com'
WARNING_TITLE = '!!!Warning!!!'
# -----------------------------SEARCH COMPANY TITLE----------------------------- #
def file_reader():
    try:
        file = open('data.json', 'r')
    except FileNotFoundError:
        data = {}
    else:
        data = json.load(file)
        file.close()
    return data


def search_company():
    data = file_reader()
    site_name = entry_website.get().strip()
    try:
        new_data = data[site_name]
    except KeyError:
        messagebox.showinfo(title='Absent', message='No such site data was found.')
    else:
        messagebox.showinfo(title='Result', message='EMail: {}\nPassword: {}'.format(new_data['email'], new_data['password']))

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#from password_generator import Password_Generator

def show_password():
    entry_password.delete(0, END)
    password = ''
    num = randint(12, 16)
    for _ in range(num):
        password += choice(POSSIBLE_SYMBOLS)
    entry_password.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def may_save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    if website == '':
        messagebox.showwarning(title=WARNING_TITLE, message='Title of website may not be empty.')
    elif email == '':
        messagebox.showwarning(title=WARNING_TITLE, message='EMail may not be empty.')
    elif password == '':
        messagebox.showwarning(title=WARNING_TITLE, message='Password may not be empty.')
    else:
        data = file_reader()
        with open('data.json', 'w') as ouf:
            new_data = {website: {'email': email, 'password': password}}
            data.update(new_data)
            pyperclip.copy(password)
            json.dump(data, ouf, indent=4)
            entry_website.delete(0, END)
            entry_password.delete(0, END)


    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg=WHITE)
canvas = Canvas(width=210, height=200, bg=WHITE, highlightthickness=0)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)


# ------------------BUTTON, ENTRIES AND LABELS ------------------- #
#Labels
website_label = Label(text='WebSite:', bg=WHITE, font=FONT)
email_label = Label(text=r'EMail/UserName:', bg=WHITE, font=FONT)
password_label = Label(text='Password:', bg=WHITE, font=FONT)

#Entries
entry_website = Entry(bg=WHITE, width=32)
entry_email = Entry(bg=WHITE, width=45)
entry_email.insert(0, MY_EMAIL)
entry_password = Entry(bg=WHITE, width=32)

#Buttons
button_search = Button(text='Search', bg=WHITE, width=8, bd=1, command=search_company)
button_generator = Button(text='Generate', bg=WHITE, width=8, bd=1, command=show_password)
button_add = Button(text='Add', bg=WHITE, width=38, bd=1, command=may_save)
# -----------------PLACING ELEMENTS ----------------------#

canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

entry_website.grid(row=1, column=1, sticky=W)
entry_email.grid(row=2, column=1, columnspan=2, sticky=W)
entry_password.grid(row=3, column=1, sticky=W, padx=0)

button_generator.grid(row=3, column=2, sticky=W, padx=0)
button_add.grid(row=4, column=1, columnspan=2, sticky=W)
button_search.grid(row=1, column=2)
window.mainloop()
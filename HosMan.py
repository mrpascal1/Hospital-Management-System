# Author : mrpacal
# Contact : ansarishahid640@gmail.com

import sqlite3
import os
import tkinter
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox

tk = tkinter
root = Tk()
top = Toplevel()
root.title("HosMan")
# Geometry Defined Here
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width, height))
top.geometry('%dx%d+0+0' % (width, height))
# root.geometry("350x150+%d+%d" %( ( (root.winfo_screenwidth() / 2.) - (350 / 2.) ), ( (root.winfo_screenheight() / 2.) - (150 / 2.) ) ) )

main_database = sqlite3.connect("records.db")


def login():
    if username_entry.get() == "admin" and password_entry.get() == "admin":
        root.deiconify()
        top.destroy()


def cancel():
    top.destroy()
    root.destroy()
    sys.exit()


def initialize():
    # main_database = sqlite3.connect("records.db")
    curs = main_database.cursor()
    table = curs.execute('''CREATE TABLE IF NOT EXISTS patientInfo(Patient_ID VARCHAR(1000),
                           First_Name VARCHAR(20),
                           Middle_Name VARCHAR(20),
                           Last_Name VARCHAR(20),
                           Age VARCHAR(3),
                           Sex VARCHAR(10),
                           Address VARCHAR(50))''')


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


def save():
    id_no = ID_entry.get()
    f_name = first_entry.get()
    m_name = middle_entry.get()
    l_name = last_entry.get()
    age_value = age_entry.get()
    sex_value = sex_entry.get()
    add_value = address_entry.get()
    print(f_name, m_name, l_name)

    curs = main_database.cursor()
    """
    table = curs.execute('''CREATE TABLE IF NOT EXISTS patientInfo(Patient_ID VARCHAR(1000),
                            First_Name VARCHAR(20),
                            Middle_Name VARCHAR(20),
                            Last_Name VARCHAR(20),
                            Age VARCHAR(3),
                            Sex VARCHAR(10),
                            Address VARCHAR(50))''')
    """
    insert = 'INSERT INTO patientInfo(Patient_ID, First_Name, Middle_Name, Last_Name, Age, Sex, Address) VALUES(?, ?, ?, ?, ?, ?, ?) '
    inserting = curs.execute(insert, (id_no, f_name, m_name, l_name, age_value, sex_value, add_value))
    main_database.commit()
    print(inserting)


def show():
    curs = main_database.cursor()
    show_table = curs.execute('SELECT * FROM patientInfo')
    patients = show_table.fetchall()
    main_database.commit()
    jj = ('\n'.join(map(str, patients)))
    messagebox.showinfo("Patients", jj)
    # print(patients)


def delete():
    id_no = ID_entry.get()
    if id_no == "":
        messagebox.showerror("Error", "ID box is empty")
    else:
        curs = main_database.cursor()
        show_table = curs.execute("SELECT * FROM patientInfo")
        patients = show_table.fetchall()
        if patients == []:
            print("Database is Empty")
        else:
            show_table = curs.execute("DELETE FROM patientInfo WHERE Patient_ID=" + id_no)
            patients = show_table.fetchall()
            main_database.commit()
            # print(patients)
            messagebox.showinfo("Patients", patients)


image = tk.PhotoImage(file="hospital.png")
panel = tk.Label(root, image=image)
panel.place(x=800)
# panel.pack(expand = "yes")


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

settingsmenu = Menu(menubar, tearoff=0)
settingsmenu.add_command(label="Initialize db", command=initialize)
menubar.add_cascade(label="Settings", menu=settingsmenu)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# Font defined here
customFont = tkFont.Font(family="Arial", size=15)
textFont = tkFont.Font(font="Georgia")
entryFont = tkFont.Font(size=11)

title = "****** Welcome To Hospital Management System *******"

_TITLE_ = tk.Label(root,
                   text=title,
                   fg="Light Green",
                   bg="Dark Green",
                   font=customFont)

username = tk.Label(top, text="Username :", font=textFont)
username.place(x=500, y=250)
password = tk.Label(top, text="Password :", font=textFont)
password.place(x=500, y=300)
username_entry = Entry(top, bd=1.5, font=entryFont)
username_entry.place(x=590, y=252)
password_entry = Entry(top, bd=1.5, font=entryFont)
password_entry.place(x=590, y=302)
button1 = Button(top, text="Login", command=lambda: login())
button1.place(x=599, y=340)
button2 = Button(top, text="Cancel", command=lambda: cancel())
button2.place(x=699, y=340)

# ID
ID = tk.Label(root, text="Patient ID :", font=textFont)
ID.place(x=4)
ID_entry = Entry(root, bd=1.5, font=entryFont)
ID_entry.place(x=6, y=22, width='110px', height='18px')

# Names
first = tk.Label(root, text="First Name :", font=textFont)
first.place(x=4, y=70)
first_entry = Entry(root, bd=1.5, font=entryFont)
first_entry.place(x=6, y=92, width='110px', height='18px')

middle = tk.Label(root, text="Middle Name :", font=textFont)
middle.place(x=208, y=70)
middle_entry = Entry(root, bd=1.5, font=entryFont)
middle_entry.place(x=210, y=92, width='110px', height='18px')

last = tk.Label(root, text="Last Name :", font=textFont)
last.place(x=408, y=70)
last_entry = Entry(root, bd=1.5, font=entryFont)
last_entry.place(x=410, y=92, width='110px', height='18px')

# Age
age = tk.Label(root, text="Age :", font=textFont)
age.place(x=4, y=140)
age_entry = Entry(root, bd=1.5, font=entryFont)
age_entry.place(x=6, y=162, width='110px', height='18px')

# Sex
sex = tk.Label(root, text="Sex :", font=textFont)
sex.place(x=208, y=140)
sex_entry = Entry(root, bd=1.5, font=entryFont)
sex_entry.place(x=210, y=162, width='110px', height='18px')

# Address
address = tk.Label(root, text="Address :", font=textFont)
address.place(x=408, y=140)
address_entry = Entry(root, bd=1.5, font=entryFont)
address_entry.place(x=410, y=162, width='400px', height='18px')

button = Button(root, text="Submit", command=save)
button.place(x=6, y=200)

button = Button(root, text="Show Records", command=show)
button.place(x=70, y=200)

button = Button(root, text="Delete Records", command=delete)
button.place(x=170, y=200)

# print(root.winfo_screenwidth(), root.winfo_screenheight())
root.withdraw()
root.mainloop()

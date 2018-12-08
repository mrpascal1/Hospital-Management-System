#Author : mrpacal
#Contact : ansarishahid640@gmail.com

import tkinter
from tkinter import *
import tkinter.font as tkFont
tk = tkinter

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
root = Tk()
root.title("HosMan")
#Geometry Defined Here
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
#root.geometry("350x150+%d+%d" %( ( (root.winfo_screenwidth() / 2.) - (350 / 2.) ), ( (root.winfo_screenheight() / 2.) - (150 / 2.) ) ) )


menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command = donothing)
filemenu.add_command(label = "Open", command = donothing)
filemenu.add_command(label = "Save", command = donothing)
filemenu.add_command(label = "Save as...", command = donothing)
filemenu.add_command(label = "Close", command = donothing)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label = "Undo", command = donothing)

editmenu.add_separator()

editmenu.add_command(label = "Cut", command = donothing)
editmenu.add_command(label = "Copy", command = donothing)
editmenu.add_command(label = "Paste", command = donothing)
editmenu.add_command(label = "Delete", command = donothing)
editmenu.add_command(label = "Select All", command = donothing)

menubar.add_cascade(label = "Edit", menu = editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Help Index", command = donothing)
helpmenu.add_command(label = "About...", command = donothing)
menubar.add_cascade(label = "Help", menu = helpmenu)

root.config(menu = menubar)



#Font defined here
customFont = tkFont.Font(family="Arial", size=15)
entryFont = tkFont.Font(font = "Georgia")
textFont = tkFont.Font(size = 12)

title = "****** Welcome To Hospital Management System *******"

_TITLE_ = tk.Label(root,
                   text = title,
                   fg = "Light Green",
                   bg = "Dark Green",
                   font = customFont)

#Names
first = tk.Label(root, text = "First Name :", font = entryFont)
first.place(x = 4)
first_entry = Entry(root, bd = 1.5, font = textFont)
first_entry.place(x = 6, y = 22, width = '110px', height = '18px')

middle = tk.Label(root, text = "Middle Name :", font = entryFont)
middle.place(x = 208)
middle_entry = Entry(root, bd = 1.5, font = textFont)
middle_entry.place(x = 210, y = 22, width = '110px', height = '18px')

last = tk.Label(root, text = "Last Name :", font = entryFont)
last.place(x = 408)
last_entry = Entry(root, bd = 1.5, font = textFont)
last_entry.place(x = 410, y = 22, width = '110px', height = '18px')

#Age
age = tk.Label(root, text = "Age :", font = entryFont)
age.place(x = 4, y = 70)
age_entry = Entry(root, bd = 1.5, font = textFont)
age_entry.place(x = 6, y = 92, width = '110px', height = '18px')

#Sex
sex = tk.Label(root, text = "Sex :", font = entryFont)
sex.place(x = 208, y = 70)
sex_entry = Entry(root, bd = 1.5, font = textFont)
sex_entry.place(x = 210, y = 92, width = '110px', height = '18px')


#Address
address = tk.Label(root, text = "Address :", font = entryFont)
address.place(x = 408, y = 70)
address_entry = Entry(root, bd = 1.5, font = textFont)
address_entry.place(x = 410, y = 92, width = '400px', height = '18px')


#print(root.winfo_screenwidth(), root.winfo_screenheight())
root.mainloop()

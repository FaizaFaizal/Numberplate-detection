#!/usr/bin/env python
import mysql.connector
from tkinter import *
#from home import *
#from ColonelHome import *
#from GeneralHome import *
#from LtColonel import *
#from MajorGeneralHome import *
#from AdminHome import *
from tkinter import messagebox
from PIL import Image, ImageTk
#from myprofile import MyprofileClass
import random
import string
#from AdminChangePassword import AdminPasswordChangeClass
#from OtpPassword import OtpPasswordClass
#import foo
import requests
import json


#URL = 'https://www.sms4india.com/api/v1/sendCampaign'




top = Tk()


uname = StringVar()
upass = StringVar()
USER_TYPE=StringVar()
#--------------------------------------------------------------



#------------------------------------------------------------------------------------
def showmyprofile():
        print("clicked")
        window = Toplevel()
        #app = MyprofileClass(window)


def showchangepassword():
    print("clicked")
    window = Toplevel()
    #app = AdminPasswordChangeClass(window)

def showaddnewuser():
    print("clicked")
    window =  Toplevel()
    #app = AddNewOfficerClass(window)
def showremoveofficer():
    print("clicked")
    window = Toplevel()
    #app = RemoveOfficerClass(window)
def idbased():
    print("clicked")
    window = Toplevel()
    #app = AdminIDBasedSearchClass(window)
def rankbased():
    print("clicked")
    window = Toplevel()
    #app = RankBasedSearchClass(window)
def listallofficers():
    print("clicked")
    window = Toplevel()
    #app = ListAllOfficersClass(window)


def adminhome():
    master1 = Toplevel()
    master1.title("Admin Home")
    master1.state("zoomed")

    img = ImageTk.PhotoImage(file='new.jpg')
    w, h = img.width(), img.height()
    canvas = Canvas(master1, width=w, height=h, bg='blue', highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0, 0, image=img, anchor=NW)


    menubar = Menu(master1)
    file = Menu(menubar, tearoff=0)
    #file.add_command(label="my profile")
    file.add_command(label="My Profile", command=showmyprofile)

    #file.add_command(label="New Officer Appointment")
    file.add_command(label="New Officer Appointment", command=showaddnewuser)

    #file.add_command(label="Remove Officer")
    file.add_command(label="Remove Officer", command=showremoveofficer)

    #file.add_command(label="Change Password")
    file.add_command(label="Change Password", command=showchangepassword)

    file.add_separator()
    file.add_command(label="Logout", command=master1.destroy)

    menubar.add_cascade(label="Activites", menu=file)
    edit = Menu(menubar, tearoff=0)
    #edit.add_command(label="IDBased")
    edit.add_command(label="IDBased", command=idbased)

    #edit.add_command(label="Rank Based")
    #edit.add_command(label="Rank Based", command=rankbased)

    edit.add_separator()

    #edit.add_command(label="Select All Officers")
    edit.add_command(label="Select All Officers", command=listallofficers)

    menubar.add_cascade(label="LogReport", menu=edit)
    help = Menu(menubar, tearoff=0)
    help.add_command(label="About")
    menubar.add_cascade(label="Help", menu=help)

    master1.config(menu=menubar)
    master1.mainloop()

def chooseaction():
    get_name = uname.get().strip()
    get_pass = upass.get().strip()
    print("Name:", get_name, ",", "Password:", get_pass)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="speech"
    )
    if get_name == "" and get_pass == "":
        messagebox.showinfo("Entry", "username and pass missing")
    elif get_name == "":
        messagebox.showinfo("Entry", "username is blank")
    elif get_pass == "":
        messagebox.showinfo("Entry", "password is blank")
    else:
        mycursor = mydb.cursor()
        sql = "SELECT * FROM login WHERE userid = %s and password=%s"
        adr = (get_name, get_pass)

        mycursor.execute(sql, adr)

        print("I am here...")
        myresult = mycursor.fetchall()
        print("Count:", mycursor.rowcount)
        if mycursor.rowcount:
            top.withdraw()
            #cp = Toplevel()
            adminhome()
            # adminhome()
        else:
            messagebox.showinfo("Entry", "no such user")
        print("done....")

def validate(e):
    #self.e=e

    if (e.isdigit()):
        return True
    else:
        return False

def loginfunction():
    large_font = ('Verdana', 15)
    large_font2 = ('Verdana', 15)
    lab1 = ('Verdana', 15)
    lab2 = ('Verdana', 15)
    bt_size = ('Verdana', 15)

    img = ImageTk.PhotoImage(file='cr.png')
    w, h = img.width(), img.height()
    canvas = Canvas(top, width=w, height=h, bg='white', highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_image(0, 0, image=img, anchor=NW)

    user_icon = ImageTk.PhotoImage(file="man_user.png")
    pass_icon = ImageTk.PhotoImage(file="pas.png")
    logo_icon = ImageTk.PhotoImage(file="logo.png")
    # logo_icon= PhotoImage(file="password.png")

    Login_Frame = Frame(top, bg="white")
    Login_Frame.place(x=460, y=180)
    logo_lbl = Label(Login_Frame, image=logo_icon).grid(row=0, column=0, pady=20)

    top.title("Login")

    top.configure(bg="light gray")
    top.state("zoomed")

    email = Label(Login_Frame, text="User ID", font=lab1, bg="white", fg="black", image=user_icon, compound=LEFT).grid(row=1, column=0, padx=20, pady=10)

    password = Label(Login_Frame, text="Password", font=lab2, bg="white", fg="black", image=pass_icon,compound=LEFT).grid(row=2, column=0, padx=20, pady=10)


    cancel = Button(top, text="Cancel", font=bt_size,width=20,relief=RIDGE,bg="light gray",command=top.destroy).place(x=970, y=360)
    #logout = Button(top, text="Sign-in", font=bt_size, command = loadhomes).place(x=235, y=170)
    logout = Button(top, text="Sign-in", font=bt_size, width=20,relief=RIDGE,command=chooseaction).place(x=970, y=250)
    psswd = Button(top, text="Forgot Password?", font=bt_size, bg="light gray",width=20,relief=RIDGE, fg="black").place(x=970,y=470)
    val = top.register(validate)

    Entry(Login_Frame, textvariable=uname, width=15, font=large_font, validate="key").grid(row=1,column=1,padx=20,pady=10)
    # e2 = Entry(master,  width=15,font=large_font).place(x = 130, y = 30)
    # text = e2.get()
    e3 = Entry(Login_Frame, textvariable=upass, show="*", width=15, font=large_font2).grid(row=2,column=1,padx=20,pady=10)

    # e3 = Entry(master, width=15,font=large_font2).place(x = 130, y = 100)
    top.mainloop()

loginfunction()




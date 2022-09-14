from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email import message
from fileinput import filename
from functools import partial
from mimetypes import common_types
from operator import getitem
from pickle import EXT4
from tkinter import *
import sqlite3
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.font import Font 
from tkinter import filedialog
import random

def query():
        # Create a database or connect to one
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM buyer")
        user_details = c.fetchall()
        print("buyer: ",user_details)
        print("")

        c.execute("SELECT * FROM seller")
        seller_details = c.fetchall()
        print("seller: ",seller_details)
        print("")

        c.execute("SELECT * FROM item")
        item_details = c.fetchall()
        print("item: ", item_details)
        print("")

        c.execute("SELECT * FROM cart")
        cart_details = c.fetchall()
        print("cart: ", cart_details)
        print("")

        c.execute("SELECT * FROM checkout")
        checkout_details = c.fetchall()
        print("checkout: ", checkout_details)

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

def loginPage():
    # ---------------------------------Enter username and pass label in login page-----------------------------------------------------
    def click1(event):
        enterid.config(state=NORMAL)
        if enterid.get() == "Username":
            enterid.delete(0, END)
        else:
            enterid.config(state=NORMAL)

    def click2(event):
        enterpass.config(state=NORMAL)
        if enterpass.get() == "Password":
            enterpass.delete(0, END)
        else:
            enterpass.config(state=NORMAL)

    def click3(event):
        if enterid.get() == "":
            enterid.insert(0, "Username")
            enterid.config(state=DISABLED)
            enterid.bind("<Button-1>",click1)

    def click4(event):
        if enterpass.get() == "":
            enterpass.insert(0, "Password")
            enterpass.config(state=DISABLED)
            enterpass.bind("<Button-1>",click2)
    # --------------------------------------------------------------------------------------------------------------------------

    global root
    root = Tk()
    root.title('MMU Grocery')
    root.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")

    # Create a database or connect to one
    conn = sqlite3.connect('grocery.db')

    # Create cursor
    c = conn.cursor()

    # # Create table
    # c.execute("""CREATE TABLE buyer (
    #         name text,
    #         day_birth text,
    #         month_birth text,
    #         year_birth text,
    #         phone text,
    #         ic text primary key,
    #         address text,
    #         postcode text,
    #         city text,
    #         state text,
    #         usertype text,
    #         username text,
    #         password1 text,
    #         password2 text
    #         )""")

    # # Create table
    # c.execute("""CREATE TABLE seller (
    #         name text,
    #         day_birth text,
    #         month_birth text,
    #         year_birth text,
    #         phone text,
    #         ic text primary key,
    #         address text,
    #         postcode text,
    #         city text,
    #         state text,
    #         usertype text,
    #         username text,
    #         password1 text,
    #         password2 text
    #         )""")

    # # Create table
    # c.execute("""CREATE TABLE item (
    #         name text,
    #         price_RM text,
    #         price_sen text,
    #         producer text,
    #         expiry_day text,
    #         expiry_month text,
    #         expiry_year text,
    #         category text,
    #         image text,
    #         id text primary key,
    #         seller_username text,
    #         stock text
    #         )""")

    # c.execute("DROP TABLE item")

    # # Create table
    # c.execute("""CREATE TABLE cart (
    #         id text,
    #         buyer_username text,
    #         quantity text
    #         )""")

    # c.execute("DROP TABLE cart")

    # # Create table
    # c.execute("""CREATE TABLE checkout (
    #         id text,
    #         buyer_username text,
    #         quantity text,
    #         status text,
    #         invoice text,
    #         seller_username text
    #         )""")

    # c.execute("DROP TABLE checkout")

    # -----------------------------------------------------Log In title--------------------------------------------------
    logintitle = Label(root, text="Log In")
    logintitle.grid(row=0, column=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------------Enter ID entry box--------------------------------------------
    global enterid
    enterid = Entry(root, width=30, borderwidth=5)
    enterid.insert(0, "Username")
    enterid.config(state=DISABLED)
    enterid.bind("<Button-1>",click1)
    enterid.bind("<FocusOut>",click3)
    enterid.grid(row=2, column=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------

    # ----------------------------------------------------Enter Pass entry box----------------------------------------
    global enterpass
    enterpass = Entry(root, width=30, borderwidth=5, show='*')
    enterpass.insert(0, "Password")
    enterpass.config(state=DISABLED)
    enterpass.bind("<Button-1>",click2)
    enterpass.bind("<FocusOut>",click4)
    enterpass.grid(row=4, column=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------

    # -----------------------------------------------Show password checkbox--------------------------------------------
    c_v1=IntVar(value=0)
    def my_show():
        if(c_v1.get()==1):
            enterpass.config(show="")
        else:
            enterpass.config(show="*")
    c1=Checkbutton(root,text="Show Password",variable=c_v1,
        onvalue=1,offvalue=0,command=my_show)
    c1.grid(row=5,column=0)
    # -----------------------------------------------------------------------------------------------------------------


    #----------------------------------------------Buyer Login Button--------------------------------------------------
    buyerloginbutton = Button(root, text="Buyer Login", padx=15, cursor="mouse", command=buyerLogin)
    buyerloginbutton.grid(row=6, column=0, padx=(0,10))
    # -----------------------------------------------------------------------------------------------------------------


    #----------------------------------------------Seller Login Button--------------------------------------------------
    sellerloginbutton = Button(root, text="Seller Login", padx=10, cursor="mouse", command=sellerLogin)
    sellerloginbutton.grid(row=6, column=1)
    # -----------------------------------------------------------------------------------------------------------------


    # -------------------------------------------------new user label-------------------------------------------------
    newuserlabel = Label(root, text="New User?")
    newuserlabel.grid(row=7, column=0, padx=(70,0), pady=(10,0))
    # -----------------------------------------------------------------------------------------------------------------


    # -----------------------------------------------------Signup button----------------------------------------------
    signupbutton = Button(root, text="Sign Up", borderwidth=0, fg="red", cursor="mouse", command=signupPage) #signupPage
    signupbutton.grid(row=7, column=1, padx=(0,70), pady=(10,0))
    # -----------------------------------------------------------------------------------------------------------------

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    root.mainloop()
    # --------------------------------------------------------------------------------------------------------------------


def signupPage():

    # -----------------------------------------Get data from combobox--------------------------------------------------------------------
    global dayval
    global monthval
    global yearval
    global stateval
    global usertypeval
    
    dayval = ""
    def selection(event):
        global dayval
        dayval = event.widget.get()

    monthval = ""
    def selection1(event):
        global monthval
        monthval = event.widget.get()

    yearval = ""
    def selection2(event):
        global yearval
        yearval = event.widget.get()

    stateval = ""
    def selection3(event):
        global stateval
        stateval = event.widget.get()

    usertypeval = ""
    def selection4(event):
        global usertypeval
        usertypeval = event.widget.get()
    # ---------------------------------------------------------------------------------------------------------------------


    # --------------------------------------------Signup Confirm---------------------------------------------------------------
    def signupConfirm():
        if name_signup.get() == "" or dayval == "" or monthval == "" or yearval == "" or phone_signup.get() == "" or ic_signup.get() == "" or address_signup.get() == "" or postcode_signup.get() == "" or city_signup.get() == "" or stateval == "" or usertypeval == "" or username_signup.get() == "" or pass1_signup.get() == "" or pass2_signup.get() == "":
            messagebox.showerror("Error","All fields are required",parent=signup)

        elif pass1_signup.get() == pass2_signup.get() and pass1_signup != "":
            # print(dayval,monthval,yearval,stateval,usertypeval)
            # Create a database or connect to one
            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()

            if usertypeval == "Buyer":
                c.execute("SELECT * FROM buyer WHERE ic=(?)",(ic_signup.get(),))

                if not c.fetchone():

                    c.execute("SELECT * FROM buyer WHERE username=(?)",(username_signup.get(),))
                    if not c.fetchone():

                        # Insert Into Table
                        c.execute("INSERT INTO buyer VALUES (:name, :day_birth, :month_birth, :year_birth, :phone, :ic, :address, :postcode, :city, :state, :usertype, :username, :password1, :password2)",
                                {
                                    'name': name_signup.get(),
                                    'day_birth': dayval,
                                    'month_birth': monthval,
                                    'year_birth': yearval,
                                    'phone': phone_signup.get(),
                                    'ic' : ic_signup.get(),
                                    'address': address_signup.get(),
                                    'postcode': postcode_signup.get(),
                                    'city': city_signup.get(),
                                    'state': stateval,
                                    'usertype': usertypeval,
                                    'username': username_signup.get(),
                                    'password1': pass1_signup.get(),
                                    'password2': pass2_signup.get()
                                })

                        # Commit Changes
                        conn.commit()

                        # Close Connection
                        conn.close()

                        e1 = username_signup.get()

                        signup.destroy()

                        messagebox.showinfo("MMU Grocery - Sign Up Successfully",f"Congratulation {e1}, You have signed up a BUYER account successfully!")

                    else:
                        messagebox.showerror("error", "This Username has been used to sign up before.", parent=signup)


                else:
                    c.execute("SELECT * FROM buyer WHERE username=(?)",(username_signup.get(),))
                    if not c.fetchone():
                        messagebox.showerror("error", "This NRIC has been used to sign up before.", parent=signup)

                    else:
                        messagebox.showerror("error", "This NRIC and Username have been used to sign up before.", parent=signup)


            else:
                c.execute("SELECT * FROM seller WHERE ic=(?)",(ic_signup.get(),))

                if not c.fetchone():

                    c.execute("SELECT * FROM seller WHERE username=(?)",(username_signup.get(),))
                    if not c.fetchone():

                        # Insert Into Table
                        c.execute("INSERT INTO seller VALUES (:name, :day_birth, :month_birth, :year_birth, :phone, :ic, :address, :postcode, :city, :state, :usertype, :username, :password1, :password2)",
                                {
                                    'name': name_signup.get(),
                                    'day_birth': dayval,
                                    'month_birth': monthval,
                                    'year_birth': yearval,
                                    'phone': phone_signup.get(),
                                    'ic' : ic_signup.get(),
                                    'address': address_signup.get(),
                                    'postcode': postcode_signup.get(),
                                    'city': city_signup.get(),
                                    'state': stateval,
                                    'usertype': usertypeval,
                                    'username': username_signup.get(),
                                    'password1': pass1_signup.get(),
                                    'password2': pass2_signup.get()
                                })

                        # Commit Changes
                        conn.commit()

                        # Close Connection
                        conn.close()

                        e1 = username_signup.get()

                        signup.destroy()

                        messagebox.showinfo("MMU Grocery - Sign Up Successfully",f"Congratulation {e1}, You have signed up a SELLER account successfully!")

                    else:
                        messagebox.showerror("error", "This Username has been used to sign up before.", parent=signup)


                else:
                    c.execute("SELECT * FROM seller WHERE username=(?)",(username_signup.get(),))
                    if not c.fetchone():
                        messagebox.showerror("error", "This NRIC has been used to sign up before.", parent=signup)

                    else:
                        messagebox.showerror("error", "This NRIC and Username have been used to sign up before.", parent=signup)

        else:
            messagebox.showerror("Error","Your Password and Confirm Password are not same!\nPlease Try Again.", parent=signup)
    # -------------------------------------------------------------------------------------------------------------------------


    signup = Tk()
    signup.title('MMU Grocery-Signup')
    signup.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")

    # -----------------------------------------------Signup Frame------------------------------------------------------
    frame1 = LabelFrame(signup, text="Personal Details", padx=30, pady=3)
    frame2 = LabelFrame(signup, text="Address", padx=31, pady=10)
    frame3 = LabelFrame(signup, text="Login Requires", padx=32, pady=5)
    frame1.grid(row=1, column=0, padx=10, pady=(10,0))
    frame2.grid(row=2, column=0, padx=10, pady=0)
    frame3.grid(row=3, column=0, padx=10, pady=(0,10))
    # --------------------------------------------------------------------------------------------------------------------

    # -------------------------------------------------Signup Entry--------------------------------------------------------
    name_signup = Entry(frame1, width=40, borderwidth=5)
    name_signup.grid(row=0, column=1, padx=20, pady=(10, 0), columnspan=3)

    # Combobox creation - day
    day = tk.StringVar()
    days = [str(i).rjust(2, "0") for i in range(1, 32)]
    combo_day = ttk.Combobox(frame1, state="readonly", width = 7, textvariable = day, values=days)
    combo_day.place(x=111, y=40)
    combo_day.set("Day")
    combo_day.current()
    combo_day.bind("<<ComboboxSelected>>",  selection)

    # month
    month = tk.StringVar()
    monthchoosen = ttk.Combobox(frame1, state="readonly", width = 14, textvariable = month)
    # Adding combobox drop down list
    monthchoosen['values'] = (' January', 
                            ' February',
                            ' March',
                            ' April',
                            ' May',
                            ' June',
                            ' July',
                            ' August',
                            ' September',
                            ' October',
                            ' November',
                            ' December')
    
    monthchoosen.place(x=195, y=40)
    monthchoosen.set("Month")
    monthchoosen.current()
    monthchoosen.bind("<<ComboboxSelected>>",  selection1)

    # year
    year = tk.StringVar()
    years = [str(2022-i).rjust(2, "0") for i in range(0, 100)]
    combo_year = ttk.Combobox(frame1, state="readonly", width =10, textvariable = year, values=years)
    combo_year.place(x=335, y=40)
    combo_year.set("Year")
    combo_year.current()
    combo_year.bind("<<ComboboxSelected>>",  selection2)

    phone_signup = Entry(frame1, width=40, borderwidth=5)
    phone_signup.grid(row=2, column=1, columnspan=3)
    ic_signup = Entry(frame1,width=40, borderwidth=5)
    ic_signup.grid(row=3, column=1, columnspan=3)
    address_signup = Entry(frame2, width=40, borderwidth=5)
    address_signup.grid(row=4, column=1, columnspan=3, padx=(0,20))
    postcode_signup = Entry(frame2, width=40, borderwidth=5)
    postcode_signup.grid(row=5, column=1, columnspan=3, padx=(0,20))
    city_signup = Entry(frame2, width=15, borderwidth=5)
    city_signup.place(x=110,y=65)

    # Combobox creation
    state = tk.StringVar()
    statechosen = ttk.Combobox(frame2, state="readonly", width = 15, textvariable = state) 
    # Adding combobox drop down list
    statechosen['values'] = ('Johor', 
                            'Kuala Lumpur',
                            'Kedah',
                            'Kelantan',
                            'Malacca',
                            'Negeri Sembilan',
                            'Pahang',
                            'Perak',
                            'Perlis',
                            'Penang',
                            'Sabah',
                            'Sarawak',
                            'Selangor',
                            'Terengganu')

    statechosen.place(x=295,y=65)    
    statechosen.set("Select Your State")
    statechosen.current()
    statechosen.bind("<<ComboboxSelected>>",  selection3)

    # Combobox creation
    usertype = tk.StringVar()
    usertypechosen = ttk.Combobox(frame3, state="readonly", width = 38, textvariable = usertype)
    # Adding combobox drop down list
    usertypechosen['values'] = ('Buyer', 
                            'Seller')
    
    usertypechosen.grid(row = 8, column = 1, columnspan=3, padx=(0,20))
    usertypechosen.set("Buyer/Seller")
    usertypechosen.current()
    usertypechosen.bind("<<ComboboxSelected>>",  selection4)

    username_signup = Entry(frame3, width=40, borderwidth=5)
    username_signup.grid(row=9, column=1, columnspan=3, padx=(0,20))
    pass1_signup = Entry(frame3, width=40, borderwidth=5)
    pass1_signup.grid(row=10, column=1, columnspan=3, padx=(0,20))
    pass2_signup = Entry(frame3, width=40, borderwidth=5)
    pass2_signup.grid(row=11, column=1, columnspan=3, padx=(0,20))
    # ------------------------------------------------------------------------------------------------------------------------------------


    # -----------------------------------------------------Signup Labels-----------------------------------------------------------
    name_label = Label(frame1, text="Name")
    name_label.place(x=0, y=13)
    age_label = Label(frame1, text="Date of Birth")
    age_label.grid(row=1, column=0)
    phone_label = Label(frame1, text="Phone")
    phone_label.place(x=0, y=71)
    ic_label = Label(frame1, text="NRIC")
    ic_label.place(x=0, y=103)
    address_label = Label(frame2, text="Address")
    address_label.grid(row=4, column=0, padx=(0,51))
    postcode_label = Label(frame2, text="Postcode")
    postcode_label.grid(row=5, column=0, padx=(0,44))
    city_label = Label(frame2, text="City")
    city_label.grid(row=6, column=0, padx=(0,78))
    state_label = Label(frame2, text="State")
    state_label.place(x=247,y=65)    
    usertype_label = Label(frame3, text="User type")
    usertype_label.grid(row=8, column=0, padx=(0,43))
    username_label = Label(frame3, text="Username")
    username_label.grid(row=9, column=0, padx=(0,38))
    pass1_label = Label(frame3, text="Password")
    pass1_label.grid(row=10, column=0, padx=(0,42))
    pass2_label = Label(frame3, text="Confirm\nPassword")
    pass2_label.grid(row=11, column=0, padx=(0,42))
    # ------------------------------------------------------------------------------------------------------------------------


    # -----------------------------------------Signup Button-----------------------------------------------------------------
    signupsucbutton = Button(signup, text="Sign Up", width=15, command=signupConfirm)
    signupsucbutton.grid(row=11, column=0, pady=(0, 10), columnspan=4)
    # ----------------------------------------------------------------------------------------------------------------------


def editUserDetails():

    # -------------------------------------------Delete Acc Function--------------------------------------------------
    def deleteAcc():
        def finalconfirmdeletebuyer():
            # Create a database or connect to one
            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()

            if e10 == "buyer":
                c.execute("SELECT * FROM buyer WHERE username = (?) ",(e3,))
                        
                user_details2 = c.fetchone()

                if enterpasstodeleteuser.get() == user_details2[12]:
                    # Create a database or connect to one
                    conn = sqlite3.connect('grocery.db')
                    # Create cursor
                    c = conn.cursor()
                    c.execute("DELETE from buyer WHERE username=(?)",(e3,))

                    # Commit Changes
                    conn.commit()

                    # Close Connection
                    conn.close()

                    messagebox.showinfo("Account was deleted successfully","This account was deleted successfully.")
                    confirmdeleteuser.destroy()
                    editor.destroy()
                    buyerloginpage.destroy()
                    
                    loginPage()

                else:
                    messagebox.showerror("Error","Password incorrect!\nPlease Try Again.", parent=confirmdeleteuser)

            else:
                c.execute("SELECT * FROM seller WHERE username = (?) ",(e3,))
                        
                user_details2 = c.fetchone()

                if enterpasstodeleteuser.get() == user_details2[12]:
                    # Create a database or connect to one
                    conn = sqlite3.connect('grocery.db')
                    # Create cursor
                    c = conn.cursor()
                    c.execute("DELETE from seller WHERE username=(?)",(e3,))

                    # Commit Changes
                    conn.commit()

                    # Close Connection
                    conn.close()

                    messagebox.showinfo("Account was deleted successfully","This account was deleted successfully.")
                    confirmdeleteuser.destroy()
                    editor.destroy()
                    # sellerloginpage.destroy()
                    
                    # loginPage()
                
                else:
                    messagebox.showerror("Error","Password incorrect!\nPlease Try Again.", parent=confirmdeleteuser)

        def confirmdeleteuser_command():

            global enterpasstodeleteuser

            cdeleteuser_btn.config(state=DISABLED)
            frame1_deletebuyer = LabelFrame(confirmdeleteuser, text="Verify Identity")
            frame1_deletebuyer.grid(row=2, column=0, padx=10, pady=(10,0))
            enterpasstodeleteuser = Entry(frame1_deletebuyer, width=20, borderwidth=5)
            enterpasstodeleteuser.grid(row=0, column=1, pady=(10,0))
            enterpasstodeleteuser_label = Label(frame1_deletebuyer, text="Password")
            enterpasstodeleteuser_label.grid(row=0, column=0, padx=(10,0), pady=(10,0))
            enterpasstodeleteuser_btn = Button(confirmdeleteuser, text="Confirm Delete", command=finalconfirmdeletebuyer)
            enterpasstodeleteuser_btn.grid(row=3, column=0, pady=10)

        confirmdeleteuser = Tk()
        confirmdeleteuser.title('Confirm delete account')
        confirmdeleteuser.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")
        cdeleteuser = Label(confirmdeleteuser, text="Are you sure you want to delete this account?")
        cdeleteuser.grid(row=0, column=0, padx=10, pady=(10,0))
        cdeleteuser_btn = Button(confirmdeleteuser, text="Confirm", command=confirmdeleteuser_command)
        cdeleteuser_btn.grid(row=1, column=0, pady=10)

    # -----------------------------------------Change Password Function-------------------------------------------------
    def changePassword():
        editor.destroy()
        
        changepass = Tk()
        changepass.title('Change Password')
        changepass.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")

        # Final change password
        def finalchangepass():
            if enternewpass1.get() == enternewpass2.get() and enternewpass1.get() != "" and enternewpass1.get() != enterinitialpass.get():
                # Create a database or connect to one
                conn = sqlite3.connect('grocery.db')
                # Create cursor
                c = conn.cursor()

                if e10 == "buyer":
                    c.execute("""UPDATE buyer SET
                            password1 = :password1,
                            password2 = :password2

                            WHERE username = :username""",
                            {'password1': enternewpass1.get(),
                            'password2': enternewpass2.get(),
                            'username' : e3
                            })

                    # Commit Changes
                    conn.commit()

                    # Close Connection
                    conn.close()

                    messagebox.showinfo("Congratulation","Your new password has changed successfully!", parent=buyerloginpage)
                    changepass.destroy()

                else:
                    c.execute("""UPDATE seller SET
                            password1 = :password1,
                            password2 = :password2

                            WHERE username = :username""",
                            {'password1': enternewpass1.get(),
                            'password2': enternewpass2.get(),
                            'username' : e3
                            })

                    # Commit Changes
                    conn.commit()

                    # Close Connection
                    conn.close()

                    messagebox.showinfo("Congratulation","Your new password has changed successfully!")
                    changepass.destroy()

            elif enternewpass1.get() != enternewpass2.get(): 
                messagebox.showerror("Error","Your new password and confirm password are not same!\nPlease Try Again.", parent=changepass)

            elif enternewpass1.get() == enterinitialpass.get():
                messagebox.showerror("Error","Your new password is same with old password!\nPlease Try Again.", parent=changepass)

            else:
                messagebox.showerror("Error","You cannot change to a empty password!\nPlease Try Again.", parent=changepass)

        # Continue change password
        def continuechangepass():
            global enternewpass1
            global enternewpass2
            # Create a database or connect to one
            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()

            if e10 == "buyer":
                c.execute("SELECT * FROM buyer WHERE username = (?) ",(e3,))
                        
                user_details2 = c.fetchone()

                if enterinitialpass.get() == user_details2[12]:
                    enterinitialpass.config(state=DISABLED)
                    continuechangepass_btn.config(state=DISABLED)
                    frame2_changepass = LabelFrame(changepass, text="New Password Set Up")
                    frame2_changepass.grid(row=3, column=0, padx=10, pady=(10,0))
                    enternewpass1 = Entry(frame2_changepass, width=20, borderwidth=5)
                    enternewpass1.grid(row=2, column=1, pady=(20,0))
                    enternewpass2 = Entry(frame2_changepass, width=20, borderwidth=5)
                    enternewpass2.grid(row=3, column=1)

                    enternewpass1_label = Label(frame2_changepass, text="New Password")
                    enternewpass1_label.grid(row=2, column=0, pady=(20,0))
                    enternewpass2_label = Label(frame2_changepass, text="Confirm\nPassword")
                    enternewpass2_label.grid(row=3, column=0)

                    confirmchangepass = Button(changepass, text="Change Password", command=finalchangepass)
                    confirmchangepass.grid(row=4, column=0, columnspan=2, pady=(10,10))

                else:
                    messagebox.showerror("Error","Password incorrect",parent=changepass)

            else:
                c.execute("SELECT * FROM seller WHERE username = (?) ",(e3,))
                        
                user_details2 = c.fetchone()

                if enterinitialpass.get() == user_details2[12]:
                    enterinitialpass.config(state=DISABLED)
                    continuechangepass_btn.config(state=DISABLED)
                    frame2_changepass = LabelFrame(changepass, text="New Password Set Up")
                    frame2_changepass.grid(row=3, column=0, padx=10, pady=(10,0))
                    enternewpass1 = Entry(frame2_changepass, width=20, borderwidth=5)
                    enternewpass1.grid(row=2, column=1, pady=(20,0))
                    enternewpass2 = Entry(frame2_changepass, width=20, borderwidth=5)
                    enternewpass2.grid(row=3, column=1)

                    enternewpass1_label = Label(frame2_changepass, text="New Password")
                    enternewpass1_label.grid(row=2, column=0, pady=(20,0))
                    enternewpass2_label = Label(frame2_changepass, text="Confirm\nPassword")
                    enternewpass2_label.grid(row=3, column=0)

                    confirmchangepass = Button(changepass, text="Change Password", command=finalchangepass)
                    confirmchangepass.grid(row=4, column=0, columnspan=2, pady=(10,10))

                else:
                    messagebox.showerror("Error","Password incorrect",parent=changepass)

        frame1_changepass = LabelFrame(changepass, text="Verify Password")
        frame1_changepass.grid(row=1, column=0, padx=10, pady=(10,0))
        enterinitialpass = Entry(frame1_changepass, width=20, borderwidth=5)
        enterinitialpass.grid(row=0, column=1, pady=(10,0))
        enterinitialpass_label = Label(frame1_changepass, text="Current Password")
        enterinitialpass_label.grid(row=0, column=0, padx=(10,0), pady=(10,0))

        continuechangepass_btn = Button(changepass, text="Continue", command=continuechangepass)
        continuechangepass_btn.grid(row=2, column=0, columnspan=2, pady=(10,0))
    # ----------------------------------------------------------------------------------------------------------------------

    # -------------------------------------------Save Changes Function--------------------------------------------------------
    def saveChanges():
        if name_editor.get() != "" and phone_editor.get() != "" and address_editor.get() != "" and postcode_editor.get() != "" and city_editor.get() != "":
            # Create a database or connect to one
            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()
            if e10 == "buyer":
                c.execute("""UPDATE buyer SET
                        name = :name,
                        day_birth = :day_birth,
                        month_birth = :month_birth,
                        year_birth = :year_birth,
                        phone = :phone,
                        address = :address,
                        postcode = :postcode,
                        city = :city,
                        state = :state

                        WHERE username = :username""",
                        {'name': name_editor.get(),
                        'day_birth': dayval_editor,
                        'month_birth': monthval_editor,
                        'year_birth': yearval_editor,
                        'phone': phone_editor.get(),
                        'address': address_editor.get(),
                        'postcode': postcode_editor.get(),
                        'city': city_editor.get(),
                        'state': stateval_editor,
                        'username' : e3
                        })

                # Commit Changes
                conn.commit()

                # Close Connection
                conn.close()

                editor.destroy()

            else:
                c.execute("""UPDATE seller SET
                        name = :name,
                        day_birth = :day_birth,
                        month_birth = :month_birth,
                        year_birth = :year_birth,
                        phone = :phone,
                        address = :address,
                        postcode = :postcode,
                        city = :city,
                        state = :state

                        WHERE username = :username""",
                        {'name': name_editor.get(),
                        'day_birth': dayval_editor,
                        'month_birth': monthval_editor,
                        'year_birth': yearval_editor,
                        'phone': phone_editor.get(),
                        'address': address_editor.get(),
                        'postcode': postcode_editor.get(),
                        'city': city_editor.get(),
                        'state': stateval_editor,
                        'username' : e3
                        })

                # Commit Changes
                conn.commit()

                # Close Connection
                conn.close()

                editor.destroy()

        else:
            messagebox.showerror("Error","You cannot update to empty details!\nPlease Try Again.", parent=editor)
    # ----------------------------------------------------------------------------------------------------------------------

    global dayval_editor
    global monthval_editor
    global yearval_editor
    global stateval_editor
    global usertypeval_editor

    dayval_editor = ""
    def selection5(event):
        global dayval_editor
        dayval_editor = event.widget.get()

    monthval_editor = ""
    def selection6(event):
        global monthval_editor
        monthval_editor = event.widget.get()

    yearval_editor = ""
    def selection7(event):
        global yearval_editor
        yearval_editor = event.widget.get()

    stateval_editor = ""
    def selection8(event):
        global stateval_editor
        stateval_editor = event.widget.get()

    usertypeval_editor = ""
    def selection9(event):
        global usertypeval_editor
        usertypeval_editor = event.widget.get()

    global editor
    global name_editor
    global day_editor
    global month_editor
    global year_editor
    global phone_editor
    global ic_editor
    global address_editor
    global postcode_editor
    global city_editor
    global state_editor
    global usertype_editor
    global username_editor
    global pass1_editor

    editor = Tk()
    editor.title('Edit User Details')
    editor.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")

    # --------------------------------------------------Create Frame----------------------------------------------------
    frame1_editor = LabelFrame(editor, text="Personal Details", padx=30, pady=3)
    frame2_editor = LabelFrame(editor, text="Address", padx=31, pady=10)
    frame3_editor = LabelFrame(editor, text="Login Requires", padx=32, pady=5)
    frame1_editor.grid(row=1, column=0, padx=10, pady=(10,0))
    frame2_editor.grid(row=2, column=0, padx=10, pady=0)
    frame3_editor.grid(row=3, column=0, padx=10, pady=(0,10))
    # ----------------------------------------------------------------------------------------------------------------------


    # --------------------------------------------------Create Entry------------------------------------------------
    name_editor = Entry(frame1_editor, width=40, borderwidth=5)
    name_editor.grid(row=0, column=1, padx=20, pady=(10, 0), columnspan=3)

    # Combobox creation - day
    day_editor = tk.StringVar()
    days_editor = [str(i).rjust(2, "0") for i in range(1, 32)]
    combo_day_editor = ttk.Combobox(frame1_editor, state="readonly", width = 7, textvariable = day_editor, values=days_editor)
    combo_day_editor.place(x=111, y=40)
    combo_day_editor.current()
    combo_day_editor.bind("<<ComboboxSelected>>",  selection5)

    # - month
    month_editor = tk.StringVar()
    monthchoosen_editor = ttk.Combobox(frame1_editor, state="readonly", width = 14, textvariable = month_editor)
    monthchoosen_editor['values'] = (' January', 
                            ' February',
                            ' March',
                            ' April',
                            ' May',
                            ' June',
                            ' July',
                            ' August',
                            ' September',
                            ' October',
                            ' November',
                            ' December')
    
    monthchoosen_editor.place(x=195, y=40)
    monthchoosen_editor.current()
    monthchoosen_editor.bind("<<ComboboxSelected>>",  selection6)

    # -  year
    year_editor = tk.StringVar()
    years_editor = [str(2022-i).rjust(2, "0") for i in range(0, 100)]
    combo_year_editor = ttk.Combobox(frame1_editor, state="readonly", width =10, textvariable = year_editor, values=years_editor)
    combo_year_editor.place(x=335, y=40)
    combo_year_editor.current()
    combo_year_editor.bind("<<ComboboxSelected>>",  selection7)

    phone_editor = Entry(frame1_editor, width=40, borderwidth=5)
    phone_editor.grid(row=2, column=1, columnspan=3)
    ic_editor = Entry(frame1_editor,width=40, borderwidth=5)
    ic_editor.grid(row=3, column=1, columnspan=3)
    address_editor = Entry(frame2_editor, width=40, borderwidth=5)
    address_editor.grid(row=4, column=1, columnspan=3, padx=(0,20))
    postcode_editor = Entry(frame2_editor, width=40, borderwidth=5)
    postcode_editor.grid(row=5, column=1, columnspan=3, padx=(0,20))
    city_editor = Entry(frame2_editor, width=15, borderwidth=5)
    city_editor.place(x=110,y=65)

    # Combobox creation - state
    state_editor = tk.StringVar()
    statechosen_editor = ttk.Combobox(frame2_editor, state="readonly", width = 15, textvariable = state_editor)
    statechosen_editor['values'] = ('Johor', 
                            'Kuala Lumpur',
                            'Kedah',
                            'Kelantan',
                            'Malacca',
                            'Negeri Sembilan',
                            'Pahang',
                            'Perak',
                            'Perlis',
                            'Penang',
                            'Sabah',
                            'Sarawak',
                            'Selangor',
                            'Terengganu')
    
    # statechosen.grid(row = 6, column = 1, columnspan=3)
    statechosen_editor.place(x=295,y=65)    
    statechosen_editor.current()
    statechosen_editor.bind("<<ComboboxSelected>>",  selection8)

    # Combobox creation - User type
    usertype_editor = tk.StringVar()
    usertypechosen_editor = ttk.Combobox(frame3_editor, state=DISABLED, width = 38, textvariable = usertype_editor)
    usertypechosen_editor['values'] = ('Buyer', 
                            'Seller')
    
    usertypechosen_editor.grid(row = 8, column = 1, columnspan=3, padx=(0,20))
    usertypechosen_editor.current()
    usertypechosen_editor.bind("<<ComboboxSelected>>",  selection9)

    username_editor = Entry(frame3_editor, width=40, borderwidth=5)
    username_editor.grid(row=9, column=1, columnspan=3, padx=(0,20))
    pass1_editor = Entry(frame3_editor, width=40, borderwidth=5, show='*')
    pass1_editor.grid(row=10, column=1, columnspan=3, padx=(0,20))
    # ------------------------------------------------------------------------------------------------------------------


    # --------------------------------------------Create Text Box Labels-------------------------------------------------
    name_label = Label(frame1_editor, text="Name")
    name_label.place(x=0, y=13)
    age_label = Label(frame1_editor, text="Date of Birth")
    age_label.grid(row=1, column=0)
    phone_label = Label(frame1_editor, text="Phone")
    phone_label.place(x=0, y=71)
    ic_label = Label(frame1_editor, text="NRIC")
    ic_label.place(x=0, y=103)
    address_label = Label(frame2_editor, text="Address")
    address_label.grid(row=4, column=0, padx=(0,51))
    postcode_label = Label(frame2_editor, text="Postcode")
    postcode_label.grid(row=5, column=0, padx=(0,44))
    city_label = Label(frame2_editor, text="City")
    city_label.grid(row=6, column=0, padx=(0,78))
    state_label = Label(frame2_editor, text="State")
    state_label.place(x=247,y=65)    
    usertype_label = Label(frame3_editor, text="User type")
    usertype_label.grid(row=8, column=0, padx=(0,43))
    username_label = Label(frame3_editor, text="Username")
    username_label.grid(row=9, column=0, padx=(0,38))
    pass1_label = Label(frame3_editor, text="Password")
    pass1_label.grid(row=10, column=0, padx=(0,42))
    # -----------------------------------------------------------------------------------------------------------
    
    # ---------------------------------------------Get data from database----------------------------------------
    # Create a database or connect to one
    conn = sqlite3.connect('grocery.db')
    # Create cursor
    c = conn.cursor()

    # ----------------------------------------------Buyer database----------------------------------------------
    if e10 == "buyer":
        c.execute("SELECT * FROM buyer WHERE username = (?) ",(e3,))
                
        user_details = c.fetchone()

        # # Loop thru results
        # for record in records:
        name_editor.insert(0, user_details[0])
        combo_day_editor.set(user_details[1])
        dayval_editor = user_details[1]
        monthchoosen_editor.set(user_details[2])
        monthval_editor = user_details[2]
        combo_year_editor.set(user_details[3])
        yearval_editor = user_details[3]
        phone_editor.insert(0, user_details[4])
        ic_editor.insert(0, user_details[5])
        ic_editor.config(state=DISABLED)
        address_editor.insert(0, user_details[6])
        postcode_editor.insert(0, user_details[7])
        city_editor.insert(0, user_details[8])
        statechosen_editor.set(user_details[9])
        stateval_editor = user_details[9]
        usertypechosen_editor.set(user_details[10])
        usertypeval_editor = user_details[10]
        username_editor.insert(0, user_details[11])
        username_editor.config(state=DISABLED)
        pass1_editor.insert(0, user_details[12])
        pass1_editor.config(state=DISABLED)
    # -----------------------------------------------------------------------------------------------------------

    # -----------------------------------------Seller database-----------------------------------------------------
    else:
        c.execute("SELECT * FROM seller WHERE username = (?) ",(e3,))
                
        user_details = c.fetchone()

        # # Loop thru results
        # for record in records:
        name_editor.insert(0, user_details[0])
        combo_day_editor.set(user_details[1])
        dayval_editor = user_details[1]
        monthchoosen_editor.set(user_details[2])
        monthval_editor = user_details[2]
        combo_year_editor.set(user_details[3])
        yearval_editor = user_details[3]
        phone_editor.insert(0, user_details[4])
        ic_editor.insert(0, user_details[5])
        ic_editor.config(state=DISABLED)
        address_editor.insert(0, user_details[6])
        postcode_editor.insert(0, user_details[7])
        city_editor.insert(0, user_details[8])
        statechosen_editor.set(user_details[9])
        stateval_editor = user_details[9]
        usertypechosen_editor.set(user_details[10])
        usertypeval_editor = user_details[10]
        username_editor.insert(0, user_details[11])
        username_editor.config(state=DISABLED)
        
        pass1_editor.insert(0, user_details[12])
        pass1_editor.config(state=DISABLED)
    # -----------------------------------------------------------------------------------------------------
        

    # -------------------------------------------Change Password------------------------------------------
    changepassword_editor = Button(frame3_editor, text="Change Password", command=changePassword)
    changepassword_editor.grid(row=11, column=3, padx=(100,0))
    #-----------------------------------------------------------------------------------------------------


    # -------------------------------------------Save Changes Button---------------------------------------
    savebuyeredit = Button(editor, text="Save", width=15, command=saveChanges)
    savebuyeredit.grid(row=11, column=0, pady=(0, 10), columnspan=4)
    # ------------------------------------------------------------------------------------------------------


    # ---------------------------------------------Delete Acc Button-------------------------------------------
    deletebuyerimage = PhotoImage(file="D:\\Grocery Logo Icon\\remove-user-29.png",master=editor)
    deletebuyer_icon = Button(master=editor,image=deletebuyerimage, borderwidth=0, cursor="mouse", command=deleteAcc)
    deletebuyer_icon.place(x=500, y=475)
    # --------------------------------------------------------------------------------------------------------

    editor.mainloop()

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

def checkout():

    def checkOut():

        def lastCheckOut():

            def randominvoice():
                global invoice_num
                invoice_num2 = random.randint(0,100000)
                invoice_num = str(invoice_num2).rjust(6, "0")



            invoice_num2 = random.randint(0,100000)
            invoice_num = str(invoice_num2).rjust(6, "0")

            conn = sqlite3.connect('grocery.db')

            c = conn.cursor()
            c.execute("SELECT * FROM checkout WHERE invoice=(?)",(invoice_num,))

            if not c.fetchone():
                invoice_num = invoice_num

            else:
                randominvoice()

            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()

            c.execute("SELECT * FROM cart WHERE buyer_username = (?)",(e3,))
            getitemid3 = c.fetchall()
            for i in getitemid3:

                c.execute("SELECT * FROM item WHERE id = (?)",(i[0],))
                # print(i[0])

                item_added_tocart = c.fetchone()

                leftstock = int(item_added_tocart[11]) - int(i[2])
                # print(leftstock)
                # print(item_added_tocart[11])
                # print(i[2])

                c.execute("""UPDATE item SET
                                stock = :stock

                                WHERE id = :id""",
                                {'stock': leftstock,
                                'id' : i[0]
                                })

                c.execute("INSERT INTO checkout VALUES (:id, :buyer_username, :quantity, :status, :invoice, :seller_username)",
                            {
                                'id': i[0],
                                'buyer_username': i[1],
                                'quantity': i[2],
                                'status': 'ToShip',
                                'invoice': invoice_num,
                                'seller_username': item_added_tocart[10]
                            })

            # c.execute("INSERT INTO checkout(id, buyer_username, quantity) SELECT id, buyer_username, quantity FROM cart WHERE buyer_username = (?)",(e3,))

            # c.execute("SELECT * FROM cart WHERE buyer_username = (?)",(e3,))
            # getitemid3 = c.fetchall()
            # for i in getitemid3: 
            #     c.execute("""UPDATE checkout SET
            #                         status = :status

            #                         WHERE id = :id""",
            #                         {'status': "ToShip",
            #                         'id' : i[0]
            #                         })         
        
            c.execute("DELETE from cart WHERE buyer_username=(?)",(e3,))

            

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            messagebox.showinfo("Checkout successfully","Your items were checked out successfully")
            checkoutfinalpage.destroy()
            checkoutpage.destroy()

        def editDetailsCheck():
            checkoutfinalpage.destroy()
            checkoutpage.destroy()
            editUserDetails()


        global checkoutfinalpage
        checkoutfinalpage = Tk()
        checkoutfinalpage.title('MMU Grocery')
        checkoutfinalpage.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")

        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * from cart WHERE buyer_username = (?)",(e3,))
        checkoutitem_id = c.fetchall()

        rwitem = 1
        clitem = 0

        rwprice1 = 1
        clprice1 = 1

        rwtimes = 1
        cltimes = 2

        rwquantity = 1
        clquantity = 3

        rwequal = 1
        clequal = 4

        rwprice2 = 1
        clprice2 = 5

        for i in checkoutitem_id:
            itemid = i[0]
            c.execute("SELECT * from item WHERE id = (?)",(itemid,))
            checkoutitem_details = c.fetchone()

            c.execute("SELECT * from cart WHERE buyer_username = (?) and id = (?)",(e3,itemid))
            checkoutitem_quantity = c.fetchone()

            

            itemname_checkout = Label(checkoutfinalpage, text=checkoutitem_details[0])
            itemname_checkout.grid(row=rwitem, column=clitem, sticky=W)

            itemprice1_checkout = Label(checkoutfinalpage, text=("RM " + checkoutitem_details[1] + "." + checkoutitem_details[2]))
            itemprice1_checkout.grid(row=rwprice1, column=clprice1, sticky=W)

            itemtimes_checkout = Label(checkoutfinalpage, text="x")
            itemtimes_checkout.grid(row=rwtimes, column=cltimes, sticky=W)

            itemquantity_checkout = Label(checkoutfinalpage, text=checkoutitem_quantity[2])
            itemquantity_checkout.grid(row=rwquantity, column=clquantity, sticky=W)

            itemequal_checkout = Label(checkoutfinalpage, text="=")
            itemequal_checkout.grid(row=rwequal, column=clequal, sticky=W)

            priceforone = int(checkoutitem_details[1]) + int(checkoutitem_details[2])/100
            totalpriceforone = priceforone * int(checkoutitem_quantity[2])
            totalpriceforone_2dp = "{:.2f}".format(totalpriceforone)

            itemprice2_checkout = Label(checkoutfinalpage, text=("RM " + totalpriceforone_2dp))
            itemprice2_checkout.grid(row=rwprice2, column=clprice2, sticky=W)



            

            rwitem = rwitem + 1
            clitem = 0

            rwprice1 = rwprice1 + 1
            clprice1 = 1

            rwtimes = rwtimes + 1
            cltimes = 2

            rwquantity = rwquantity + 1
            clquantity = 3

            rwequal = rwequal + 1
            clequal = 4

            rwprice2 = rwprice2 + 1
            clprice2 = 5

            rwdash = rwitem + 1
            
        itemname_checkout_label = Label(checkoutfinalpage, text="Item inside your cart")
        itemname_checkout_label.grid(row=0, column=0)

        itemdash_checkout = Label(checkoutfinalpage, text="------------------------------------------------------------")
        itemdash_checkout.grid(row=rwdash, column=0, columnspan=6, sticky=W)

        rwtotal = rwdash + 1

        itemtotalprice_checkout = Label(checkoutfinalpage, text=("RM " + totalprice_under_2dp))
        itemtotalprice_checkout.grid(row=rwtotal, column=5, sticky=W)

        itemtotal_checkout = Label(checkoutfinalpage, text="Total")
        itemtotal_checkout.grid(row=rwtotal, column=4, padx=(0,5), sticky=W)

        rwpayment = rwtotal + 1

        itempayment_checkout_label = Label(checkoutfinalpage, text="Payment : COD")
        itempayment_checkout_label.grid(row=rwpayment, column=0, sticky=W)

        rwchange = rwpayment + 1

        editpersonaldetails_checkout = Button(checkoutfinalpage, text="Edit Personal Details", command=editDetailsCheck)
        editpersonaldetails_checkout.grid(row=rwchange, column=0, columnspan=6, padx=(0,120))

        proceedcheckout_checkout = Button(checkoutfinalpage, text="Check Out", command=lastCheckOut)
        proceedcheckout_checkout.grid(row=rwchange, column=1, columnspan=6, padx=(80,0))
        


        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        checkoutfinalpage.mainloop()

    global quantity_edit

    quantity_edit = ""
    def selection22(event):
        global quantity_edit
        quantity_edit = event.widget.get()

    def editCart(getitemid2):

        def deleteItemFromCart():
            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()

            c.execute("DELETE from cart WHERE buyer_username = (?) and id = (?)",(e3,getitemid2))

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            messagebox.showinfo("Item was deleted successfully","This item was deleted from cart successfully.")
            checkouteditor.destroy()
            checkoutpage.destroy()

        def saveCartChanges():
            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()

            c.execute("SELECT * FROM cart WHERE buyer_username = (?) and id = (?)",(e3,getitemid2))
            cart_detail = c.fetchone()
            if quantity_edit != cart_detail[2] and quantity_edit != "":
            # print(quantity_edit, cart_detail[2])

                conn = sqlite3.connect('grocery.db')
                # Create cursor
                c = conn.cursor()
                
                c.execute("""UPDATE cart SET
                                quantity = :quantity

                                WHERE id = :id""",
                                {'quantity': quantity_edit,
                                'id' : getitemid2
                                })


                # Commit Changes
                conn.commit()

                # Close Connection
                conn.close()

                messagebox.showinfo("Congratulation","This item is edited successfully")
                checkouteditor.destroy()
                checkoutpage.destroy()
            else:
                checkouteditor.destroy()

        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM cart WHERE buyer_username = (?) and id = (?)",(e3,getitemid2))
        cart_detail = c.fetchone()
        # print(cart_detail)

        c.execute("SELECT * FROM item WHERE id = (?)",(getitemid2,))
        item_detail = c.fetchone()
        # print(item_detail)

        if int(item_detail[11]) != 0:
            global checkouteditor
            checkouteditor = Tk()
            checkouteditor.title('Add to cart')
            checkouteditor.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")

            enteritemquantity = tk.StringVar()
            enteritemquantitys = [str(i) for i in range(1, (int(item_detail[11]))+1)]
            enteritemquantity_cart = ttk.Combobox(checkouteditor, state="readonly", width = 7, textvariable = enteritemquantity, values=enteritemquantitys)
            enteritemquantity_cart.grid(row=0, column=1, padx=(0,10), pady=(10,0))
            enteritemquantity_cart.set(cart_detail[2])
            enteritemquantity_cart.current()
            enteritemquantity_cart.bind("<<ComboboxSelected>>",  selection22)

            enteritemquantity_cart_label = Label(checkouteditor, text="Quantity")
            enteritemquantity_cart_label.grid(row=0, column=0, padx=(10,10), pady=(10,0))

            save_btn = Button(checkouteditor, text="Save", width=8, command=saveCartChanges)
            save_btn.grid(row=1, column=0, padx=(0,40), pady=10, columnspan=2)

            deletecartimage = PhotoImage(file="D:\Grocery Logo Icon\delete-29.png",master=checkouteditor)
            deletecart_icon = Button(master=checkouteditor,image=deletecartimage, borderwidth=0, cursor="mouse", command=deleteItemFromCart)
            deletecart_icon.grid(row=1, column=0, padx=(100,0), columnspan=2)

            checkouteditor.mainloop()

        else:
            messagebox.showerror("Error","Oops, this item was sold out.", parent=checkoutpage)

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

    checkoutpage = Tk()
    checkoutpage.title('MMU Grocery')
    checkoutpage.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")
    checkoutpage.geometry("560x610")

    main_frame2 = LabelFrame(checkoutpage, width=530, height=600)
    main_frame2.grid(row=1,column=0)

    my_canvas2 = Canvas(main_frame2, width=530, height=550)
    my_canvas2.grid(row=1,column=0)

    my_scrollbar = ttk.Scrollbar(main_frame2, orient=VERTICAL, command=my_canvas2.yview)
    my_scrollbar.grid(column=1, row=1, sticky='NS')

    my_canvas2.configure(yscrollcommand=my_scrollbar.set)
    my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion= my_canvas2.bbox("all")))

    second_frame2 = Frame(my_canvas2, width=530, height=550)

    my_canvas2.create_window((0,0), window=second_frame2, anchor="nw")

    checkout_btn = Button(checkoutpage, text="Check Out", width=15, bg="orange", padx=10, pady=12, command=checkOut)
    checkout_btn.place(x=420, y=555)

    conn = sqlite3.connect('grocery.db')
    # Create cursor
    c = conn.cursor()
    c.execute("SELECT * FROM cart WHERE buyer_username = (?)",(e3,))
    cartitemexist = c.fetchall()

    if not cartitemexist:
        checkout_btn.config(state=DISABLED, bg="lightgray")

    total_label = Label(checkoutpage, text="Total", font=8)
    total_label.place(x=230, y=578)

    conn = sqlite3.connect('grocery.db')
    # Create cursor
    c = conn.cursor()
    c.execute("SELECT * FROM cart WHERE buyer_username = (?)",(e3,))
    cart_detail = c.fetchall()
    totalprice_under = 0
    if cart_detail:
        for i in cart_detail:
            itemidincart = i[0]

            c.execute("SELECT * FROM item WHERE id = (?)",(itemidincart,))

            item_details = c.fetchone()

            totalprice_under_1 = (int(item_details[1])+(int(item_details[2])/100))*int(i[2])
            totalprice_under = totalprice_under + totalprice_under_1
            # totalprice_2dp_1 = "{:.2f}".format(totalprice_under)
            # print(totalprice_2dp_1)
            
    else:
        totalprice_under = 0

    global totalprice_under_2dp
    totalprice_under_2dp = "{:.2f}".format(totalprice_under)
    totalprice_under_show = Label(checkoutpage, text=("RM "+totalprice_under_2dp), fg="orange", font=10)
    totalprice_under_show.place(x=300, y=578)

    conn = sqlite3.connect('grocery.db')
    # Create cursor
    c = conn.cursor()

    # rowframe = 0
    # colframe = 0
    rowpic = 1
    colpic = 0
    rowname = 1
    colname = 1
    rowprice1 = 2
    colprice1 = 1
    rowstock = 3
    colstock = 1
    rowprice2 = 4
    colprice2 = 1
    rowedit = 1
    coledit = 2
    rowdash2 = 5
    coldash2 = 0

    dash1 = Label(second_frame2, text="---------------------------------------------------------------------------------------")
    dash1.grid(row=0, column=0, columnspan=3)

    c.execute("SELECT * FROM cart WHERE buyer_username = (?)",(e3,))
    cart_detail = c.fetchall()
    for i in cart_detail:
        itemidincart = i[0]

        c.execute("SELECT * FROM item WHERE id = (?)",(itemidincart,))

        item_details = c.fetchall()

        #concept

        for f in item_details:

            # frameforcart = LabelFrame(second_frame2)
            # frameforcart.grid(row=rowframe, column=colframe, pady=10, padx=10)

            img=Image.open(f[8]) # read the image file
            img=img.resize((100,100)) # new width & height
            img=ImageTk.PhotoImage(img, master=second_frame2)
            e1 =tk.Label(second_frame2)
            e1.grid(row=rowpic,column=colpic, rowspan=4, padx=35)
            e1.image = img
            e1['image']=img # garbage collection 

            showname = Label(second_frame2, text=f[0])
            showname.grid(row=rowname,column=colname, sticky=W, padx=60)

            showprice = Label(second_frame2, text=("RM "+f[1]+"."+f[2]+" per unit"))
            showprice.grid(row=rowprice1,column=colprice1, sticky=W, padx=60)

            showstock = Label(second_frame2, text=("Quantity: "+i[2]))
            showstock.grid(row=rowstock,column=colstock, sticky=W, padx=60)

            totalprice = (int(f[1])+(int(f[2])/100))*int(i[2])
            totalprice_2dp = "{:.2f}".format(totalprice)

            showtotalprice = Label(second_frame2, text=("Total: RM "+str(totalprice_2dp)))
            showtotalprice.grid(row=rowprice2,column=colprice2, sticky=W, padx=60)

            global getitemid2
            getitemid2 = f[9]
            action_w_arg3 = partial(editCart,getitemid2)
            editcart_btn = Button(second_frame2, text="Edit", borderwidth=0, fg="gray", command=action_w_arg3)
            editcart_btn.grid(row=rowedit, column=coledit, padx=30)

            dash2 = Label(second_frame2, text="---------------------------------------------------------------------------------------")
            dash2.grid(row=rowdash2, column=coldash2, columnspan=3)

            rowpic = rowpic + 5
            colpic = 0

            rowname = rowname + 5
            colname = 1

            rowprice1 = rowprice1 + 5
            colprice1 = 1

            rowstock = rowstock + 5
            colstock = 1

            rowprice2 = rowprice2 + 5
            colprice2 = 1

            rowedit = rowedit + 5
            coledit = 2

            rowdash2 = rowdash2 + 5
            coldash2 = 0


    checkoutpage.mainloop()

sortStatus2 = 1
def checkbill():

    def cancelOrder(getinvoicenum):

        def confirmcancelorder():
            # Create a database or connect to one
            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()

            c.execute("SELECT * FROM checkout WHERE invoice = (?)",(getinvoicenum,)) # [11]
            stockitem = c.fetchall()

            for i in stockitem:
                getitem = i[0]
                getquantity = i[2]

                c.execute("SELECT * FROM item WHERE id = (?)",(getitem,)) # [11]
                stockitem = c.fetchone()

                ori_quantity = int(getquantity) + int(stockitem[11])

                c.execute("""UPDATE item SET
                                stock = :stock

                                WHERE id = :id""",
                                {'stock': ori_quantity,
                                'id' : getitem
                                })



            c.execute("DELETE from checkout WHERE invoice=(?)",(getinvoicenum,))

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            messagebox.showinfo("Cancel Order","Your order has been cancelled!", parent=buyerloginpage)
            cancelorderpage.destroy()
            checkbillpage.destroy()
            
        # Create a database or connect to one
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()
        c.execute("SELECT * FROM checkout WHERE invoice=(?)",(getinvoicenum,))
        checkstatus = c.fetchall()
        count = 0
        size = 0
        for a in checkstatus:
            size += 1
            if a[3] == 'ToShip':
                count += 1
        if count == size:

            cancelorderpage = Tk()
            cancelorderpage.title('MMU Grocery')
            cancelorderpage.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")

            cancelorder_label = Label(cancelorderpage, text="Are you sure you want to cancel this order?")
            cancelorder_label.grid(row=0, column=0)

            cancelorder_button = Button(cancelorderpage, text="Confirm", command=confirmcancelorder)
            cancelorder_button.grid(row=1, column=0)
        
        else:
            messagebox.showerror("Error","Some of the items in this bill was shipped or received by you. Therefore, you cannot cancel this order anymore.", parent=checkbillpage)

    checkbillpage = Tk()
    checkbillpage.title('MMU Grocery')
    checkbillpage.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")
    checkbillpage.geometry("560x610")

    main_frame2 = Frame(checkbillpage, width=530, height=600)
    main_frame2.grid(row=1,column=0)

    my_canvas2 = Canvas(main_frame2, width=530, height=550)
    my_canvas2.grid(row=1,column=0)

    my_scrollbar2 = ttk.Scrollbar(main_frame2, orient=VERTICAL, command=my_canvas2.yview)
    my_scrollbar2.grid(column=1, row=1, sticky='NS')

    my_canvas2.configure(yscrollcommand=my_scrollbar2.set)
    my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion= my_canvas2.bbox("all")))

    second_frame2 = Frame(my_canvas2, width=530, height=600)

    my_canvas2.create_window((0,0), window=second_frame2, anchor="nw")

    def sortByToShip():
        global sortStatus2
        sortStatus2 = 1
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM checkout WHERE buyer_username = (?) and status = (?)",(e3,"ToShip"))
        global cart_detail
        cart_detail = c.fetchall()
        checkbillpage.destroy()
        checkbill()

    def sortByToReceive():
        global sortStatus2
        sortStatus2 = 2
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM checkout WHERE buyer_username = (?) and status = (?)",(e3,"ToReceive"))
        global cart_detail
        cart_detail = c.fetchall()
        checkbillpage.destroy()
        checkbill()


    def sortByDelivered():
        global sortStatus2
        sortStatus2 = 3
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM checkout WHERE buyer_username = (?) and status = (?)",(e3,"Completed"))
        global cart_detail
        cart_detail = c.fetchall()
        checkbillpage.destroy()
        checkbill()

    conn = sqlite3.connect('grocery.db')
    # Create cursor
    c = conn.cursor()

    rowdash1 = 0
    coldash1 = 0
    rowinv = 1
    colinv = 0
    rowccl = 1
    colccl = 1
    rowdash2 = 2
    coldash2 = 0
    rowpic = 3
    colpic = 0
    rowname = 3
    colname = 1
    rowprice1 = 4
    colprice1 = 1
    rowstock = 5
    colstock = 1
    rowprice2 = 6
    colprice2 = 1
    # rowdash3 = 7
    # coldash3 = 0

    toship_btn = Button(checkbillpage, text="To Ship", width=9, bg="#FFF0BC", command=sortByToShip)
    toship_btn.grid(row=0, column=0, pady=(15,0), padx=(0,350))

    toreceive_btn = Button(checkbillpage, text="To Receive", width=9, bg="#F5FFBC", command=sortByToReceive)
    toreceive_btn.grid(row=0, column=0, pady=(15,0), padx=(0,150))

    delivered_btn = Button(checkbillpage, text="Completed", width=9, bg="#D0FFBC", command=sortByDelivered)
    delivered_btn.grid(row=0, column=0, pady=(15,0), padx=(50,0))

    # dash1 = Label(second_frame2, text="=====================================================")
    # dash1.grid(row=0, column=0, columnspan=2)


    if sortStatus2 == 1:
        toship_btn.config(state=DISABLED, bg="lightgray")
        c.execute("SELECT * FROM checkout WHERE buyer_username = (?) and status = (?)",(e3,"ToShip"))
        global cart_detail
        cart_detail = c.fetchall()

    elif sortStatus2 == 2:
        toreceive_btn.config(state=DISABLED, bg="lightgray")

    elif sortStatus2 == 3:
        delivered_btn.config(state=DISABLED, bg="lightgray")

    global invno_diff
    invno_diff = 0
    for i in cart_detail:
        itemidincart = i[0]

        c.execute("SELECT * FROM item WHERE id = (?)",(itemidincart,))

        item_details = c.fetchall()

        #concept
        
        for f in item_details:
            if invno_diff != i[4] or invno_diff == 0:
                dash1 = Label(second_frame2, text="=====================================================")
                dash1.grid(row=rowdash1, column=coldash1, columnspan=2)

            # else:
            #     dash1 = Label(second_frame2, text="----------------------------------------------------------------------------------------")
            #     dash1.grid(row=rowdash1, column=coldash1, columnspan=2)

            if invno_diff != i[4] or invno_diff == 0:
                showinvoice = Label(second_frame2, text="Invoice No: "+i[4]) # select * from checkout, if invoice number is not same, then print invoice number
                showinvoice.grid(row=rowinv, column=colinv)

                if i[3] == "ToShip":
                    global getinvoicenum
                    getinvoicenum = i[4]
                    action_w_arg4 = partial(cancelOrder,getinvoicenum)
                    cancelorder_btn = Button(second_frame2, text="Cancel Order", borderwidth=0, fg="gray", command=action_w_arg4)
                    cancelorder_btn.grid(row=rowccl, column=colccl, padx=(140,0))

                dash2 = Label(second_frame2, text="----------------------------------------------------------------------------------------")
                dash2.grid(row=rowdash2, column=coldash2, columnspan=2)

            else:
                dash2 = Label(second_frame2, text="----------------------------------------------------------------------------------------")
                dash2.grid(row=rowdash2, column=coldash2, columnspan=2)
            

            img=Image.open(f[8]) # read the image file
            img=img.resize((100,100)) # new width & height
            img=ImageTk.PhotoImage(img, master=second_frame2)
            e1 =tk.Label(second_frame2)
            e1.grid(row=rowpic,column=colpic, rowspan=4, padx=(0,20))
            e1.image = img
            e1['image']=img # garbage collection 

            showname = Label(second_frame2, text=f[0])
            showname.grid(row=rowname,column=colname, sticky=W, padx=(0,40))

            showprice = Label(second_frame2, text=("RM "+f[1]+"."+f[2]+" per unit"))
            showprice.grid(row=rowprice1,column=colprice1, sticky=W, padx=(0,40))

            showstock = Label(second_frame2, text=("Quantity: "+i[2]))
            showstock.grid(row=rowstock,column=colstock, sticky=W, padx=(0,40))

            totalprice = (int(f[1])+(int(f[2])/100))*int(i[2])
            totalprice_2dp = "{:.2f}".format(totalprice)

            showtotalprice = Label(second_frame2, text=("Total: RM "+str(totalprice_2dp)))
            showtotalprice.grid(row=rowprice2,column=colprice2, sticky=W, padx=(0,40))

            # global getitemid2
            # getitemid2 = f[9]
            # action_w_arg3 = partial(cancelOrder,getitemid2) # add a status in checkout (eg. preparing, shipping, delivered)
            # editcart_btn = Button(second_frame2, text="Edit", borderwidth=0, fg="gray", command=action_w_arg3)
            # editcart_btn.grid(row=rowedit, column=coledit, padx=30)


            # Dash 1
            if invno_diff != i[4] or invno_diff == 0:
                rowdash1 = rowdash1 + 7
                coldash1 = 0

            else:
                rowdash1 = rowdash1 + 7
                coldash1 = 0


            # invoice number
            if invno_diff != i[4] or invno_diff == 0:
                rowinv = rowinv + 7
                colinv = 0

            else:
                rowinv = rowinv + 7
                colinv = 0

            # cancel order
            if invno_diff != i[4] or invno_diff == 0:
                rowccl = rowccl + 7
                colccl = 1

            else:
                rowccl = rowccl + 7
                colccl = 1

            # Dash 2
            if invno_diff != i[4] or invno_diff == 0:
                rowdash2 = rowdash2 + 7
                coldash2 = 0

            else:
                rowdash2 = rowdash2 + 7
                coldash2 = 0

            # picture
            if invno_diff != i[4] or invno_diff == 0:
                rowpic = rowpic + 7
                colpic = 0

            else:
                rowpic = rowpic + 7
                colpic = 0

            # name
            if invno_diff != i[4] or invno_diff == 0:
                rowname = rowname + 7
                colname = 1

            else:
                rowname = rowname + 7
                colname = 1

            # price 1
            if invno_diff != i[4] or invno_diff == 0:
                rowprice1 = rowprice1 + 7
                colprice1 = 1

            else:
                rowprice1 = rowprice1 + 7
                colprice1 = 1

            # stock
            if invno_diff != i[4] or invno_diff == 0:
                rowstock = rowstock + 7
                colstock = 1

            else:
                rowstock = rowstock + 7
                colstock = 1

            # price 2
            if invno_diff != i[4] or invno_diff == 0:
                rowprice2 = rowprice2 + 7
                colprice2 = 1

            else:
                rowprice2 = rowprice2 + 7
                colprice2 = 1
            
            invno_diff = i[4]

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    checkbillpage.mainloop()

def addToCart(getitemid):

    global quantity_added

    quantity_added = ""
    def selection21(event):
        global quantity_added
        quantity_added = event.widget.get()

    def continueAddToCart():
        if quantity_added != "":
            # Create a database or connect to one
            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()
            # Insert Into Table
            c.execute("SELECT * FROM item WHERE id = (?)",(getitemid,)) # [11]
            stockitem = c.fetchone()

            c.execute("SELECT * FROM cart WHERE id = (?) and buyer_username = (?)",(getitemid,e3))
            addedtocartbefore = c.fetchone()
            if addedtocartbefore:

                new_quantity = int(quantity_added) + int(addedtocartbefore[2])

                if int(new_quantity) < int(stockitem[11]):

                    c.execute("""UPDATE cart SET
                                    quantity = :quantity

                                    WHERE id = :id""",
                                    {'quantity': new_quantity,
                                    'id' : getitemid
                                    })


                    # Commit Changes
                    conn.commit()

                    # Close Connection
                    conn.close()

                    messagebox.showinfo("Congratulation","This item is added to cart successfully",parent=buyerloginpage)
                    addquantitypage.destroy()

                else:
                    messagebox.showerror("Error","Oops, the quantity of this item (inside your cart + you are adding now) are more than the stock left.", parent=buyerloginpage)

            else:
                c.execute("INSERT INTO cart VALUES (:id, :buyer_username, :quantity)",
                        {
                            'id': getitemid,
                            'buyer_username': e3,
                            'quantity': quantity_added
                        })

    

                # Commit Changes
                conn.commit()

                # Close Connection
                conn.close()

                messagebox.showinfo("Congratulation","This item is added to cart successfully",parent=buyerloginpage)
                addquantitypage.destroy()

        else:
            addquantitypage.destroy()


    # Create a database or connect to one
    conn = sqlite3.connect('grocery.db')
    # Create cursor
    c = conn.cursor()
    c.execute("SELECT * FROM item WHERE id = (?)",(getitemid,))

    item_added_tocart = c.fetchone()
    if int(item_added_tocart[11]) != 0:
        global addquantitypage
        addquantitypage = Tk()
        addquantitypage.title('Add to cart')
        addquantitypage.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")

        enteritemquantity = tk.StringVar()
        enteritemquantitys = [str(i) for i in range(1, (int(item_added_tocart[11]))+1)]
        enteritemquantity_cart = ttk.Combobox(addquantitypage, state="readonly", width = 7, textvariable = enteritemquantity, values=enteritemquantitys)
        enteritemquantity_cart.grid(row=0, column=1)
        enteritemquantity_cart.set("0")
        enteritemquantity_cart.current()
        enteritemquantity_cart.bind("<<ComboboxSelected>>",  selection21)

        enteritemquantity_cart_label = Label(addquantitypage, text="Quantity")
        enteritemquantity_cart_label.grid(row=0, column=0)

        add_to_cart_btn = Button(addquantitypage, text="Add to cart", command=continueAddToCart)
        add_to_cart_btn.grid(row=1, column=0, columnspan=2)

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

    else:
        messagebox.showerror("Error","Oops, this item was sold out.", parent=buyerloginpage)


def buyerPageQuit():

    buyerloginpage.destroy()

    loginPage()

def loginagain_buyer():
    global e10
    global buyerloginpage
    buyerloginpage = Tk()
    buyerloginpage.title('MMU Grocery')
    buyerloginpage.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")
    buyerloginpage.geometry("560x620")
    e10 = "buyer"

    
    
    main_frame2 = Frame(buyerloginpage, width=530, height=600)
    main_frame2.grid(row=1,column=0)

    my_canvas2 = Canvas(main_frame2, width=530, height=550)
    my_canvas2.grid(row=1,column=0)

    my_scrollbar2 = ttk.Scrollbar(main_frame2, orient=VERTICAL, command=my_canvas2.yview)
    my_scrollbar2.grid(column=1, row=1, sticky='NS')

    my_canvas2.configure(yscrollcommand=my_scrollbar2.set)
    my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion= my_canvas2.bbox("all")))

    second_frame2 = Frame(my_canvas2, width=530, height=600)

    my_canvas2.create_window((0,0), window=second_frame2, anchor="nw")



    buyerimage = PhotoImage(file="D:\\Grocery Logo Icon\\user_25x29.png", master=buyerloginpage)
    buyer_details_icon = Button(master=buyerloginpage, image=buyerimage, borderwidth=0, cursor="mouse", command=editUserDetails)
    buyer_details_icon.place(x=390, y=10)

    cartimage = PhotoImage(file="D:\\Grocery Logo Icon\\shopping_cart 25x29.png", master=buyerloginpage)
    cartimage_icon = Button(master=buyerloginpage, image=cartimage, borderwidth=0, cursor="mouse", command=checkout)
    cartimage_icon.place(x=480, y=10)

    logoutimage = PhotoImage(file="D:\Grocery Logo Icon\logout4-removebg-29x29.png", master=buyerloginpage)
    logoutimage_icon = Button(master=buyerloginpage, image=logoutimage, borderwidth=0, cursor="mouse", command=buyerPageQuit)
    # logoutimage_icon.grid(row=0, column=0, padx=(400,0), pady=(7,0))
    logoutimage_icon.place(x=525, y=10)

    billimage = PhotoImage(file="D:\Grocery Logo Icon\purchase-order-28.png", master=buyerloginpage)
    billimage_icon = Button(master=buyerloginpage, image=billimage, borderwidth=0, cursor="mouse", command=checkbill)
    # logoutimage_icon.grid(row=0, column=0, padx=(400,0), pady=(7,0))
    billimage_icon.place(x=435, y=10)

    def sortByAll():
        global sortStatus
        sortStatus = 1
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM item")
        global seller_details
        seller_details = c.fetchall()
        buyerloginpage.destroy()
        loginagain_buyer()

    def sortByVege():
        global sortStatus
        sortStatus = 2
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM item WHERE category=(?)",("Vegetable",))
        global seller_details
        seller_details = c.fetchall()
        buyerloginpage.destroy()
        loginagain_buyer()


    def sortByFruits():
        global sortStatus
        sortStatus = 3
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM item WHERE category=(?)",("Fruits",))
        global seller_details
        seller_details = c.fetchall()
        buyerloginpage.destroy()
        loginagain_buyer()


    def sortByHerb():
        global sortStatus
        sortStatus = 4
        sortbyHerb.config(state=DISABLED, bg="lightgray")
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM item WHERE category=(?)",("Herb",))
        global seller_details
        seller_details = c.fetchall()
        buyerloginpage.destroy()
        loginagain_buyer()


    sortbyAll = Button(buyerloginpage, text="All", width=9, bg="#FFF0BC", command=sortByAll)
    sortbyAll.place(x=10, y=10)

    sortbyVege = Button(buyerloginpage, text="Vegetable", width=9, bg="#F5FFBC", command=sortByVege)
    sortbyVege.place(x=100, y=10)

    sortbyFruits = Button(buyerloginpage, text="Fruit", width=9, bg="#D0FFBC", command=sortByFruits)
    sortbyFruits.place(x=190, y=10)

    sortbyHerb = Button(buyerloginpage, text="Herb", width=9, bg="#BDFFFE", command=sortByHerb)
    sortbyHerb.place(x=280, y=10)


    sellingitem_label_buyer = Label(buyerloginpage, text="Welcome to MMU Grocery")
    sellingitem_label_buyer.grid(row=0, column=0, pady=(50,0))

    





    if sortStatus == 1:
        sortbyAll.config(state=DISABLED, bg="lightgray")
        # global sortStatus
        # sortStatus = 1
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM item")
        global seller_details
        seller_details = c.fetchall()
        # sortByAll()

    # elif sortStatus2 == 1:
    #     sortbyAll.config(state=DISABLED, bg="lightgray")

    elif sortStatus == 2:
        sortbyVege.config(state=DISABLED, bg="lightgray")

    elif sortStatus == 3:
        sortbyFruits.config(state=DISABLED, bg="lightgray")

    elif sortStatus == 4:
        sortbyHerb.config(state=DISABLED, bg="lightgray")

    #concept
    
    rowpic = 2
    colpic = 0
    rowname = 3
    colname = 0
    rowprice = 4
    colprice = 0
    rowstock = 5
    colstock = 0
    rowedit = 6
    coledit = 0

    for f in seller_details:
        img=Image.open(f[8]) # read the image file
        img=img.resize((150,150)) # new width & height
        img=ImageTk.PhotoImage(img, master=second_frame2)
        getitemid_show = f[9]
        action_a_arg = partial(showItemDetails,getitemid_show)
        e1 =tk.Button(master=second_frame2, command=action_a_arg)
        e1.grid(row=rowpic,column=colpic, padx=10)
        e1.image = img
        e1['image']=img # garbage collection 

        showname = Label(second_frame2, text=f[0])
        showname.grid(row=rowname,column=colname)

        showprice = Label(second_frame2, text=("RM "+f[1]+"."+f[2]))
        showprice.grid(row=rowprice,column=colprice)

        showstock = Label(second_frame2, text=("Stock Left: "+f[11]))
        showstock.grid(row=rowstock,column=colstock)

        global getitemid
        getitemid = f[9]
        action_w_arg2 = partial(addToCart,getitemid)
        edititem_btn = Button(second_frame2, width=18, text="Add to cart", bg='#FFBFBF', command=action_w_arg2)
        edititem_btn.grid(row=rowedit,column=coledit, pady=(0,15))

        if(colpic==2): # start new line after third column
            rowpic=rowpic+5# start wtih next row
            colpic=0    # start with first column
        else:       # within the same row 
            colpic=colpic+1

        if(colname==2):
            rowname=rowname+5
            colname=0
        else:
            colname=colname+1

        if(colprice==2):
            rowprice=rowprice+5
            colprice=0
        else:
            colprice=colprice+1

        if(colstock==2):
            rowstock=rowstock+5
            colstock=0
        else:
            colstock=colstock+1

        if(coledit==2):
            rowedit=rowedit+5
            coledit=0
        else:
            coledit=coledit+1

    buyerloginpage.mainloop()

sortStatus = 1
def buyerLogin():
    
    

    if enterid.get() == "" or enterid["state"]==DISABLED or enterpass.get() == "" or enterpass["state"]==DISABLED:
        messagebox.showerror("Error","All fields are required",parent=root)

    else:
        # Create a database or connect to one
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()
        c.execute("SELECT * FROM buyer WHERE username = (?) and password1 = (?) ",(enterid.get(),enterpass.get()))
                
        buyer_details = c.fetchone()

        if buyer_details:
            global e3
            e3 = enterid.get()

            global e4
            e4 = enterpass.get()

            root.destroy()

            loginagain_buyer()

            
            

        else:
            messagebox.showerror("Error","Invalid Username and/or Password\nPlease try again.")

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()


filename = ""

def addItem():

    global dayval_item
    global monthval_item
    global yearval_item
    global categoryval_item
    # global imageval_item
    
    dayval_item = ""
    def selection10(event):
        global dayval_item
        dayval_item = event.widget.get()

    monthval_item = ""
    def selection11(event):
        global monthval_item
        monthval_item = event.widget.get()

    yearval_item = ""
    def selection12(event):
        global yearval_item
        yearval_item = event.widget.get()

    categoryval_item = ""
    def selection13(event):
        global categoryval_item
        categoryval_item = event.widget.get()

    additempage = Tk()
    additempage.title('Add item')
    additempage.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")

    # -----------------------------------------------Add Item Frame------------------------------------------------------------
    frame1_add = LabelFrame(additempage, text="Item Details", padx=30, pady=10)
    frame1_add.grid(row=1, column=0, padx=10, pady=10)
    # ------------------------------------------------------------------------------------------------------------------


    # -----------------------------------------------Add Item Entry-------------------------------------------------------
    itemname = Entry(frame1_add, width=40, borderwidth=5)
    itemname.grid(row=0, column=1, padx=20)
    itemprice_RM = Entry(frame1_add, width=8, borderwidth=5, justify=RIGHT)
    itemprice_RM.grid(row=1, column=1, padx=(0,255))
    itemprice_sen = Entry(frame1_add, width=5, borderwidth=5)
    itemprice_sen.grid(row=1, column=1, padx=(0,100))
    itemstock = Entry(frame1_add, width=11, borderwidth=5)
    itemstock.grid(row=1, column=1, padx=(232,0))

    # ------------------------------------------------------------------------------------------------
    # def limitSizeDay(*args):
    #     value = dayValue.get()
    #     if len(value) > 2: dayValue.set(value[:2])

    # dayValue = StringVar()
    # dayValue.trace('w', limitSizeDay)

    # day_entry1=Entry(frame1_add, bg="#282B2B", fg="white", width=6, textvariable=dayValue)
    # day_entry1.grid(row=1, column=1, padx=(273,0))

    # var = StringVar()

    # max_len = 2
    # def on_write(*args):
    #     s = var.get()
    #     if len(s) > max_len:
    #         var.set(s[:max_len])

    # var.trace_variable("w", on_write)
    # entry = Entry(frame1_add, textvariable=var)
    # entry.grid(row=1, column=1, padx=(273,0))
    # ---------------------------------------------------------------------------------------------------

    itemproducer = Entry(frame1_add, width=40, borderwidth=5)
    itemproducer.grid(row=2, column=1)

    # Combobox creation
    day = tk.StringVar()
    days = [str(i).rjust(2, "0") for i in range(1, 32)]
    combo_day = ttk.Combobox(frame1_add, state="readonly", width = 7, textvariable = day, values=days)
    combo_day.grid(row=3, column=1, padx=(0, 248))
    combo_day.set("Day")
    combo_day.current()
    combo_day.bind("<<ComboboxSelected>>",  selection10)

    month = tk.StringVar()
    monthchoosen = ttk.Combobox(frame1_add, state="readonly", width = 14, textvariable = month)
    
    # Adding combobox drop down list
    monthchoosen['values'] = (' January', 
                            ' February',
                            ' March',
                            ' April',
                            ' May',
                            ' June',
                            ' July',
                            ' August',
                            ' September',
                            ' October',
                            ' November',
                            ' December')

    monthchoosen.grid(row=3, column=1, padx=(0, 25))
    monthchoosen.set("Month")
    monthchoosen.current()
    monthchoosen.bind("<<ComboboxSelected>>",  selection11)

    year = tk.StringVar()
    years = [str(2032-i).rjust(2, "0") for i in range(0, 100)]
    combo_year = ttk.Combobox(frame1_add, state="readonly", width =10, textvariable = year, values=years)
    combo_year.grid(row=3, column=1, padx=(223, 0))
    combo_year.set("Year")
    combo_year.current()
    combo_year.bind("<<ComboboxSelected>>",  selection12)

    # Combobox creation
    category_add = tk.StringVar()
    categorychosen_add = ttk.Combobox(frame1_add, state='readonly', width = 38, textvariable = category_add)
    
    # Adding combobox drop down list
    categorychosen_add['values'] = ('Vegetable', 
                            'Fruits',
                            'Herb')
    
    categorychosen_add.grid(row = 4, column = 1)
    categorychosen_add.set("Category")
    categorychosen_add.current()
    categorychosen_add.bind("<<ComboboxSelected>>",  selection13)
    # ----------------------------------------------------------------------------------------------------------------


    # -----------------------------------------------Label--------------------------------------------------------------
    itemname_label = Label(frame1_add, text="Name")
    itemname_label.grid(row=0, column=0, sticky=W)
    itemprice_label = Label(frame1_add, text="Price (RM)")
    itemprice_label.grid(row=1, column=0, sticky=W)
    itemprice_dot_label = Label(frame1_add, text=".")
    itemprice_dot_label.grid(row=1, column=1, padx=(0,167))
    itemstock_label = Label(frame1_add, text="Stock")
    itemstock_label.grid(row=1, column=1, padx=(50,0))
    itemproducer_label = Label(frame1_add, text="Producer")
    itemproducer_label.grid(row=2, column=0, sticky=W)
    itemexpiry_label = Label(frame1_add, text="Expiry date")
    itemexpiry_label.grid(row=3, column=0, sticky=W)
    itemcategory_label = Label(frame1_add, text="Category")
    itemcategory_label.grid(row=4, column=0, sticky=W)
    # ---------------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------Select Image-------------------------------------------------------------
    itemimage_label = Label(frame1_add, text="Select image")
    itemimage_label.grid(row=5, column=0, sticky=W)

    b1 = Button(frame1_add, text='Upload Files', 
    width=40,command = lambda:upload_file())
    b1.grid(row=5,column=1)

    

    def upload_file():
        global filename
        f_types = [('Jpg Files', '*.jpg'),
        ('PNG Files','*.png')]   # type of files to select 
        filename = tk.filedialog.askopenfilename(filetypes=f_types, parent=additempage)
        b1["text"] = filename
    # ------------------------------------------------------------------------------------------------------------------------
    
    # -----------------------------------------------Create Item Button---------------------------------------------------------
    
    def createItem():

        def randomid():
            global itemid
            number_id_item = random.randint(0,100)

            if categoryval_item == "Fruits":
                alphabet_id_item = "F"

            elif categoryval_item == "Vegetable":
                alphabet_id_item = "V"

            elif categoryval_item == "Herb":
                alphabet_id_item  = "H"

            else:
                alphabet_id_item = ""

            itemid = alphabet_id_item + str(number_id_item)

        number_id_item = random.randint(0,100)

        if categoryval_item == "Fruits":
            alphabet_id_item = "F"

        elif categoryval_item == "Vegetable":
            alphabet_id_item = "V"

        elif categoryval_item == "Herb":
            alphabet_id_item  = "H"

        else:
            alphabet_id_item = ""

        itemid = alphabet_id_item + str(number_id_item)

        conn = sqlite3.connect('grocery.db')

        c = conn.cursor()
        c.execute("SELECT * FROM item WHERE id=(?)",(itemid,))

        if not c.fetchone():
            itemid = itemid

        else:
            randomid()

        if itemname.get() == "" or itemprice_RM.get() == "" or itemprice_sen.get() == "" or itemproducer.get() == "" or dayval_item == "" or monthval_item == "" or yearval_item == "" or categoryval_item == "" or filename == "" or itemstock.get() == "":
            messagebox.showerror("Error","All fields are required",parent=additempage)

        else:
            # Create a database or connect to one
            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()

            # c.execute("SELECT * FROM item WHERE id=(?)",(itemid,))

            # if not c.fetchone():

            # Insert Into Table
            c.execute("INSERT INTO item VALUES (:name, :price_RM, :price_sen, :producer, :expiry_date, :expiry_month, :expiry_year, :category, :image, :id, :seller_username, :stock)",
                    {
                        'name': itemname.get(),
                        'price_RM': itemprice_RM.get(),
                        'price_sen': itemprice_sen.get(),
                        'producer': itemproducer.get(),
                        'expiry_date': dayval_item,
                        'expiry_month' : monthval_item,
                        'expiry_year': yearval_item,
                        'category': categoryval_item,
                        'image': filename,
                        'id': itemid,
                        'seller_username': e3,
                        'stock': itemstock.get()
                    })

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            additempage.destroy()

            messagebox.showinfo("MMU Grocery - Create Item Successfully",f"Congratulation, The item is created successfully!")
    

        
    
    createitem = Button(additempage, text="Create", width=8, command=createItem)
    createitem.grid(row=2, column=0)
    # -------------------------------------------------------------------------------------------------------------------------

def editItemDetails(getitemid):

    def deleteItem():
        def finalconfirmdeleteitem():
            # Create a database or connect to one
            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()

            c.execute("SELECT * FROM seller WHERE username = (?) ",(e3,))
                    
            user_details2 = c.fetchone()

            if enterpasstodeleteitem.get() == user_details2[12]:
                # Create a database or connect to one
                conn = sqlite3.connect('grocery.db')
                # Create cursor
                c = conn.cursor()
                c.execute("DELETE from item WHERE id=(?)",(getitemid,))

                # Commit Changes
                conn.commit()

                # Close Connection
                conn.close()

                messagebox.showinfo("Item was deleted successfully","This item was deleted successfully.")
                confirmdeleteitem.destroy()
                itemeditor.destroy()

            else:
                messagebox.showerror("Error","Password incorrect!\nPlease Try Again.", parent=confirmdeleteitem)


        def confirmdeleteitem_command():

            global enterpasstodeleteitem

            cdeleteitem_btn.config(state=DISABLED)
            frame1_deleteitem = LabelFrame(confirmdeleteitem, text="Verify Identity")
            frame1_deleteitem.grid(row=2, column=0, padx=10, pady=(10,0))
            enterpasstodeleteitem = Entry(frame1_deleteitem, width=20, borderwidth=5)
            enterpasstodeleteitem.grid(row=0, column=1, pady=(10,0))
            enterpasstodeleteitem_label = Label(frame1_deleteitem, text="Password")
            enterpasstodeleteitem_label.grid(row=0, column=0, padx=(10,0), pady=(10,0))
            enterpasstodeleteitem_btn = Button(confirmdeleteitem, text="Confirm Delete", command=finalconfirmdeleteitem)
            enterpasstodeleteitem_btn.grid(row=3, column=0, pady=10)

        confirmdeleteitem = Tk()
        confirmdeleteitem.title('Confirm delete account')
        confirmdeleteitem.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")
        cdeleteitem = Label(confirmdeleteitem, text="Are you sure you want to delete this item?")
        cdeleteitem.grid(row=0, column=0, padx=10, pady=(10,0))
        cdeleteitem_btn = Button(confirmdeleteitem, text="Confirm", command=confirmdeleteitem_command)
        cdeleteitem_btn.grid(row=1, column=0, pady=10)

    def saveItem():
        if itemname_editor.get() != "" or itemprice_RM_editor.get() != "" or itemprice_sen_editor.get() != "" or itemproducer_editor.get() != "" or dayval_item_editor != "" or monthval_item_editor != "" or yearval_item_editor != "" or itemstock_editor.get() != "":
            # print(itemname_editor.get(),itemprice_RM_editor.get(),itemprice_sen_editor.get(),itemproducer_editor.get(),dayval_item_editor,monthval_item_editor,yearval_item_editor,itemstock_editor.get(),filename)
            # Create a database or connect to one
            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()
            if filename != "":
                c.execute("""UPDATE item SET
                        name = :name,
                        price_RM = :price_RM,
                        price_sen = :price_sen,
                        producer = :producer,
                        expiry_day = :expiry_day,
                        expiry_month = :expiry_month,
                        expiry_year = :expiry_year,
                        image = :image,
                        stock = :stock

                        WHERE id = :id""",
                        {'name': itemname_editor.get(),
                        'price_RM': itemprice_RM_editor.get(),
                        'price_sen': itemprice_sen_editor.get(),
                        'producer': itemproducer_editor.get(),
                        'expiry_day': dayval_item_editor,
                        'expiry_month': monthval_item_editor,
                        'expiry_year': yearval_item_editor,
                        'image': filename,
                        'stock': itemstock_editor.get(),
                        'id' : getitemid
                        })

                # Commit Changes
                conn.commit()

                # Close Connection
                conn.close()

                itemeditor.destroy()

            else:
                # Create a database or connect to one
                conn = sqlite3.connect('grocery.db')
                # Create cursor
                c = conn.cursor()
                if filename == "":
                    c.execute("""UPDATE item SET
                            name = :name,
                            price_RM = :price_RM,
                            price_sen = :price_sen,
                            producer = :producer,
                            expiry_day = :expiry_day,
                            expiry_month = :expiry_month,
                            expiry_year = :expiry_year,
                            stock = :stock

                            WHERE id = :id""",
                            {'name': itemname_editor.get(),
                            'price_RM': itemprice_RM_editor.get(),
                            'price_sen': itemprice_sen_editor.get(),
                            'producer': itemproducer_editor.get(),
                            'expiry_day': dayval_item_editor,
                            'expiry_month': monthval_item_editor,
                            'expiry_year': yearval_item_editor,
                            'stock': itemstock_editor.get(),
                            'id' : getitemid
                            })

                    # Commit Changes
                    conn.commit()

                    # Close Connection
                    conn.close()

                    messagebox.showinfo("Congratulation","You have updated the details of this item successfully")
                    itemeditor.destroy()

        else:
            messagebox.showerror("Error","You cannot update to empty details!\nPlease Try Again.", parent=itemeditor)

    global dayval_item_editor
    global monthval_item_editor
    global yearval_item_editor
    global categoryval_item_editor

    global itemname_editor
    global itemprice_RM_editor
    global itemprice_sen_editor
    global itemstock_editor
    global itemproducer_editor
    global filename
    
    dayval_item_editor = ""
    def selection14(event):
        global dayval_item_editor
        dayval_item_editor = event.widget.get()

    monthval_item_editor = ""
    def selection15(event):
        global monthval_item_editor
        monthval_item_editor = event.widget.get()

    yearval_item_editor = ""
    def selection16(event):
        global yearval_item_editor
        yearval_item_editor = event.widget.get()

    categoryval_item_editor = ""
    def selection17(event):
        global categoryval_item_editor
        categoryval_item_editor = event.widget.get()

    global itemeditor
    itemeditor = Tk()
    itemeditor.title('MMU Grocery')
    itemeditor.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")
    # print(getitemid)

    # -----------------------------------------------Add Item Frame------------------------------------------------------------
    frame1_add_editor = LabelFrame(itemeditor, text="Item Details", padx=30, pady=10)
    frame1_add_editor.grid(row=1, column=0, padx=10, pady=10)
    # ------------------------------------------------------------------------------------------------------------------


    # -----------------------------------------------Add Item Entry-------------------------------------------------------
    itemname_editor = Entry(frame1_add_editor, width=40, borderwidth=5)
    itemname_editor.grid(row=0, column=1, padx=20)
    itemprice_RM_editor = Entry(frame1_add_editor, width=8, borderwidth=5, justify=RIGHT)
    itemprice_RM_editor.grid(row=1, column=1, padx=(0,255))
    itemprice_sen_editor = Entry(frame1_add_editor, width=5, borderwidth=5)
    itemprice_sen_editor.grid(row=1, column=1, padx=(0,100))
    itemstock_editor = Entry(frame1_add_editor, width=11, borderwidth=5)
    itemstock_editor.grid(row=1, column=1, padx=(232,0))
    itemproducer_editor = Entry(frame1_add_editor, width=40, borderwidth=5)
    itemproducer_editor.grid(row=2, column=1)

    # Combobox creation
    day_itemeditor = tk.StringVar()
    days_itemeditor = [str(i).rjust(2, "0") for i in range(1, 32)]
    combo_day_item = ttk.Combobox(frame1_add_editor, state="readonly", width = 7, textvariable = day_itemeditor, values=days_itemeditor)
    combo_day_item.grid(row=3, column=1, padx=(0, 248))
    combo_day_item.set("Day")
    combo_day_item.current()
    combo_day_item.bind("<<ComboboxSelected>>",  selection14)

    month_itemeditor = tk.StringVar()
    monthchoosen_item = ttk.Combobox(frame1_add_editor, state="readonly", width = 14, textvariable = month_itemeditor)
    
    # Adding combobox drop down list
    monthchoosen_item['values'] = (' January', 
                            ' February',
                            ' March',
                            ' April',
                            ' May',
                            ' June',
                            ' July',
                            ' August',
                            ' September',
                            ' October',
                            ' November',
                            ' December')

    monthchoosen_item.grid(row=3, column=1, padx=(0, 25))
    monthchoosen_item.set("Month")
    monthchoosen_item.current()
    monthchoosen_item.bind("<<ComboboxSelected>>",  selection15)

    year_itemeditor = tk.StringVar()
    years_itemeditor = [str(2032-i).rjust(2, "0") for i in range(0, 100)]
    combo_year_item = ttk.Combobox(frame1_add_editor, state="readonly", width =10, textvariable = year_itemeditor, values=years_itemeditor)
    combo_year_item.grid(row=3, column=1, padx=(223, 0))
    combo_year_item.set("Year")
    combo_year_item.current()
    combo_year_item.bind("<<ComboboxSelected>>",  selection16)

    # Combobox creation
    category_add_editor = tk.StringVar()
    categorychosen_add_editor = ttk.Combobox(frame1_add_editor, state=DISABLED, width = 38, textvariable = category_add_editor)
    
    # Adding combobox drop down list
    categorychosen_add_editor['values'] = ('Vegetable', 
                            'Fruits',
                            'Herb')
    
    categorychosen_add_editor.grid(row = 4, column = 1)
    categorychosen_add_editor.set("Category")
    categorychosen_add_editor.current()
    categorychosen_add_editor.bind("<<ComboboxSelected>>",  selection17)
    # ----------------------------------------------------------------------------------------------------------------


    # -----------------------------------------------Label--------------------------------------------------------------
    itemname_label = Label(frame1_add_editor, text="Name") # , padx=(0,33)
    itemname_label.grid(row=0, column=0, sticky=W)
    itemprice_label = Label(frame1_add_editor, text="Price (RM)")
    itemprice_label.grid(row=1, column=0, sticky=W)
    itemprice_dot_label = Label(frame1_add_editor, text=".")
    itemprice_dot_label.grid(row=1, column=1, padx=(0,167))
    itemstock_label = Label(frame1_add_editor, text="Stock")
    itemstock_label.grid(row=1, column=1, padx=(50,0))
    itemproducer_label = Label(frame1_add_editor, text="Producer")
    itemproducer_label.grid(row=2, column=0, sticky=W)
    itemexpiry_label = Label(frame1_add_editor, text="Expiry date")
    itemexpiry_label.grid(row=3, column=0, sticky=W) # , pady=(3,0)
    itemcategory_label = Label(frame1_add_editor, text="Category")
    itemcategory_label.grid(row=4, column=0, sticky=W)
    # ---------------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------Select Image-------------------------------------------------------------
    itemimage_label = Label(frame1_add_editor, text="Select image")
    itemimage_label.grid(row=5, column=0, sticky=W)

    b1_editor = Button(frame1_add_editor, text='Upload Files', 
    width=40,command = lambda:upload_file())
    b1_editor.grid(row=5,column=1)

    

    def upload_file():
        global filename
        f_types = [('Jpg Files', '*.jpg'),
        ('PNG Files','*.png'), ('Jpeg Files', '*.jpeg')]   # type of files to select 
        filename = tk.filedialog.askopenfilename(filetypes=f_types, parent=itemeditor)
        b1_editor["text"] = filename
    # ------------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------Get data from database----------------------------------------
    # Create a database or connect to one
    conn = sqlite3.connect('grocery.db')
    # Create cursor
    c = conn.cursor()

    # ----------------------------------------------Buyer database----------------------------------------------
    c.execute("SELECT * FROM item WHERE id = (?) ",(getitemid,))
            
    user_details = c.fetchone()

    # # Loop thru results
    # for record in records:
    itemname_editor.insert(0, user_details[0])
    itemprice_RM_editor.insert(0, user_details[1])
    itemprice_sen_editor.insert(0, user_details[2])
    itemproducer_editor.insert(0, user_details[3])
    combo_day_item.set(user_details[4])
    dayval_item_editor = user_details[4]
    monthchoosen_item.set(user_details[5])
    monthval_item_editor = user_details[5]
    combo_year_item.set(user_details[6])
    yearval_item_editor = user_details[6]
    categorychosen_add_editor.set(user_details[7])
    categoryval_item_editor = user_details[7]
    b1_editor["text"] = user_details[8]
    itemstock_editor.insert(0, user_details[11])
    # -----------------------------------------------------------------------------------------------------------

    # -------------------------------------------Save Changes Button---------------------------------------
    saveitemedit = Button(itemeditor, text="Save", width=15, command=saveItem)
    saveitemedit.grid(row=6, column=0, pady=(0, 10), columnspan=4)
    # ------------------------------------------------------------------------------------------------------


    # ---------------------------------------------Delete Acc Button-------------------------------------------
    deletebuyerimage = PhotoImage(file="D:\Grocery Logo Icon\delete-29.png",master=itemeditor)
    deletebuyer_icon = Button(master=itemeditor,image=deletebuyerimage, borderwidth=0, cursor="mouse", command=deleteItem)
    deletebuyer_icon.place(x=500, y=250)
    # --------------------------------------------------------------------------------------------------------

    itemeditor.mainloop()

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

def showItemDetails(getitemid_show):
    # ---------------------------------------------Get data from database----------------------------------------
    # Create a database or connect to one
    conn = sqlite3.connect('grocery.db')
    # Create cursor
    c = conn.cursor()

    # ----------------------------------------------Buyer database----------------------------------------------
    c.execute("SELECT * FROM item WHERE id = (?) ",(getitemid_show,))
            
    user_details = c.fetchone()
    global itemdisplayer
    itemdisplayer = Tk()
    itemdisplayer.title(user_details[0])
    itemdisplayer.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")

    # -----------------------------------------------Add Item Frame------------------------------------------------------------
    frame1_add_displayer = LabelFrame(itemdisplayer, text="Item Details", padx=30, pady=10)
    frame1_add_displayer.grid(row=1, column=0, padx=10, pady=10)
    # ------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------Get data from database----------------------------------------
    # Create a database or connect to one
    conn = sqlite3.connect('grocery.db')
    # Create cursor
    c = conn.cursor()

    # ----------------------------------------------Buyer database----------------------------------------------
    c.execute("SELECT * FROM item WHERE id = (?) ",(getitemid_show,))
            
    user_details = c.fetchone()

    # -----------------------------------------------Add Item Entry-------------------------------------------------------
    itemname_displayer = Label(frame1_add_displayer, text=user_details[0])
    itemname_displayer.grid(row=1, column=2, sticky=W)
    itemprice_displayer = Label(frame1_add_displayer, text=('RM '+user_details[1]+'.'+user_details[2]))
    itemprice_displayer.grid(row=2, column=2, sticky=W)
    itemstock_displayer = Label(frame1_add_displayer, text=user_details[11])
    itemstock_displayer.grid(row=3, column=2, sticky=W)
    itemproducer_displayer = Label(frame1_add_displayer, text=user_details[3])
    itemproducer_displayer.grid(row=4, column=2, sticky=W)
    itemexpiry_displayer = Label(frame1_add_displayer, text=(user_details[4]+'/'+user_details[5]+'/'+user_details[6]))
    itemexpiry_displayer.grid(row=5, column=2, sticky=W)
    itemcategory_displayer = Label(frame1_add_displayer, text=user_details[7])
    itemcategory_displayer.grid(row=6, column=2, sticky=W)
    # ----------------------------------------------------------------------------------------------------------------

    

    # -----------------------------------------------Label--------------------------------------------------------------
    itemname_displayer_label = Label(frame1_add_displayer, text="Name") # , padx=(0,33)
    itemname_displayer_label.grid(row=1, column=0, sticky=W)
    itemprice_displayer_label = Label(frame1_add_displayer, text="Price")
    itemprice_displayer_label.grid(row=2, column=0, sticky=W)
    itemstock_displayer_label = Label(frame1_add_displayer, text="Stock")
    itemstock_displayer_label.grid(row=3, column=0, sticky=W)
    itemproducer_displayer_label = Label(frame1_add_displayer, text="Producer")
    itemproducer_displayer_label.grid(row=4, column=0, sticky=W)
    itemexpiry_displayer_label = Label(frame1_add_displayer, text="Expiry date")
    itemexpiry_displayer_label.grid(row=5, column=0, sticky=W)
    itemcategory_displayer_label = Label(frame1_add_displayer, text="Category")
    itemcategory_displayer_label.grid(row=6, column=0, sticky=W)
    
    for i in range(6):
        row = 1 + i
        itemmidcolon = Label(frame1_add_displayer, text=":")
        itemmidcolon.grid(row=row, column=1)
        
    # ---------------------------------------------------------------------------------------------------------------------

    itemdisplayer.mainloop()

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

sortStatus5 = 1
def checkorder():

    def getbuyerdetail(getinvoicenum):

        checkbuyerdetailpage = Tk()
        checkbuyerdetailpage.title('MMU Grocery')
        checkbuyerdetailpage.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")

        # Create a database or connect to one
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()
        c.execute("SELECT * FROM checkout WHERE invoice = (?)",(getinvoicenum,))
        getbuyerusername = c.fetchone()

        c.execute("SELECT * FROM buyer WHERE username = (?)",(getbuyerusername[1],))
        getbuyerdetailinck = c.fetchone()

        labelframe5 = LabelFrame(checkbuyerdetailpage, text="Buyer Details", padx=10, pady=10)
        labelframe5.grid(row=0, column=0, padx=10, pady=10)

        # buyertitle = Label(checkbuyerdetailpage, text="Buyer Details")
        # buyertitle.grid(row=0, column=0, sticky=W)

        buyername = Label(labelframe5, text=getbuyerdetailinck[0])
        buyername.grid(row=0, column=2, sticky=W)
        buyername_label = Label(labelframe5, text="Name")
        buyername_label.grid(row=0, column=0, sticky=W)

        buyerphone = Label(labelframe5, text=getbuyerdetailinck[4])
        buyerphone.grid(row=1, column=2, sticky=W)
        buyerphone_label = Label(labelframe5, text="Phone")
        buyerphone_label.grid(row=1, column=0, sticky=W)

        buyeraddress = Label(labelframe5, text=getbuyerdetailinck[6] + ",")
        buyeraddress.grid(row=2, column=2, sticky=W)
        buyeraddress_label = Label(labelframe5, text="Address")
        buyeraddress_label.grid(row=2, column=0, sticky=W)

        buyercolon = Label(labelframe5, text=":")
        buyercolon.grid(row=0, column=1)

        buyercolon2 = Label(labelframe5, text=":")
        buyercolon2.grid(row=1, column=1)

        buyercolon3 = Label(labelframe5, text=":")
        buyercolon3.grid(row=2, column=1)

        buyeraddress2 = Label(labelframe5, text=getbuyerdetailinck[7] + ", " + getbuyerdetailinck[8] + ",")
        buyeraddress2.grid(row=3, column=2, sticky=W)

        buyeraddress3 = Label(labelframe5, text=getbuyerdetailinck[9] + ".")
        buyeraddress3.grid(row=4, column=2, sticky=W)

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

    def arereceived(getinvoicenum):

        def confirmreceived():
            # Create a database or connect to one
            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()
            c.execute("""UPDATE checkout SET
                            status = :status

                            WHERE invoice = :invoice and seller_username = :seller_username""",
                            {'status': 'Completed',
                            'invoice': getinvoicenum,
                            'seller_username': e3
                            })

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            messagebox.showinfo("Status Changed","The status of these items has changed to 'Completed'!", parent=sellerloginpage)
            arereceivedrpage.destroy()
            checkorderpage.destroy()
            

        arereceivedrpage = Tk()
        arereceivedrpage.title('MMU Grocery')
        arereceivedrpage.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")

        arereceived_label = Label(arereceivedrpage, text="Are you sure these items are received by buyer?")
        arereceived_label.grid(row=0, column=0)

        arereceived_button = Button(arereceivedrpage, text="Confirm", command=confirmreceived)
        arereceived_button.grid(row=1, column=0)

    def areshipped(getinvoicenum):

        def confirmshipped():
            # Create a database or connect to one
            conn = sqlite3.connect('grocery.db')
            # Create cursor
            c = conn.cursor()
            c.execute("""UPDATE checkout SET
                            status = :status

                            WHERE invoice = :invoice and seller_username = :seller_username""",
                            {'status': 'ToReceive',
                            'invoice': getinvoicenum,
                            'seller_username': e3
                            })

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            messagebox.showinfo("Status Changed","The status of these items has changed to 'To Receive'!", parent=sellerloginpage)
            areshippedrpage.destroy()
            checkorderpage.destroy()
            

        areshippedrpage = Tk()
        areshippedrpage.title('MMU Grocery')
        areshippedrpage.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")

        areshipped_label = Label(areshippedrpage, text="Are you sure these items are shipped to buyer?")
        areshipped_label.grid(row=0, column=0)

        areshipped_button = Button(areshippedrpage, text="Confirm", command=confirmshipped)
        areshipped_button.grid(row=1, column=0)

    checkorderpage = Tk()
    checkorderpage.title('MMU Grocery')
    checkorderpage.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")
    checkorderpage.geometry("560x610")

    main_frame2 = Frame(checkorderpage, width=530, height=600)
    main_frame2.grid(row=1,column=0)

    my_canvas2 = Canvas(main_frame2, width=530, height=550)
    my_canvas2.grid(row=1,column=0)

    my_scrollbar2 = ttk.Scrollbar(main_frame2, orient=VERTICAL, command=my_canvas2.yview)
    my_scrollbar2.grid(column=1, row=1, sticky='NS')

    my_canvas2.configure(yscrollcommand=my_scrollbar2.set)
    my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion= my_canvas2.bbox("all")))

    second_frame2 = Frame(my_canvas2, width=530, height=600)

    my_canvas2.create_window((0,0), window=second_frame2, anchor="nw")

    def sortByToShip():
        global sortStatus5
        sortStatus5 = 1
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM checkout WHERE seller_username = (?) and status = (?)",(e3,"ToShip"))
        global cart_detail
        cart_detail = c.fetchall()
        checkorderpage.destroy()
        checkorder()

    def sortByToReceive():
        global sortStatus5
        sortStatus5 = 2
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM checkout WHERE seller_username = (?) and status = (?)",(e3,"ToReceive"))
        global cart_detail
        cart_detail = c.fetchall()
        checkorderpage.destroy()
        checkorder()


    def sortByDelivered():
        global sortStatus5
        sortStatus5 = 3
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM checkout WHERE seller_username = (?) and status = (?)",(e3,"Completed"))
        global cart_detail
        cart_detail = c.fetchall()
        checkorderpage.destroy()
        checkorder()

    conn = sqlite3.connect('grocery.db')
    # Create cursor
    c = conn.cursor()

    rowdash1 = 0
    coldash1 = 0
    rowinv = 1
    colinv = 0
    rowccl = 1
    colccl = 1
    rowdash2 = 2
    coldash2 = 0
    rowpic = 3
    colpic = 0
    rowname = 3
    colname = 1
    rowprice1 = 4
    colprice1 = 1
    rowstock = 5
    colstock = 1
    rowprice2 = 6
    colprice2 = 1
    # rowdash3 = 7
    # coldash3 = 0

    toship_btn = Button(checkorderpage, text="To Ship", width=9, bg="#FFF0BC", command=sortByToShip)
    toship_btn.grid(row=0, column=0, pady=(15,0), padx=(0,350))

    toreceive_btn = Button(checkorderpage, text="To Receive", width=9, bg="#F5FFBC", command=sortByToReceive)
    toreceive_btn.grid(row=0, column=0, pady=(15,0), padx=(0,150))

    delivered_btn = Button(checkorderpage, text="Completed", width=9, bg="#D0FFBC", command=sortByDelivered)
    delivered_btn.grid(row=0, column=0, pady=(15,0), padx=(50,0))

    # dash1 = Label(second_frame2, text="=====================================================")
    # dash1.grid(row=0, column=0, columnspan=2)


    if sortStatus5 == 1:
        toship_btn.config(state=DISABLED, bg="lightgray")
        c.execute("SELECT * FROM checkout WHERE seller_username = (?) and status = (?)",(e3,"ToShip"))
        global cart_detail
        cart_detail = c.fetchall()

    elif sortStatus5 == 2:
        toreceive_btn.config(state=DISABLED, bg="lightgray")

    elif sortStatus5 == 3:
        delivered_btn.config(state=DISABLED, bg="lightgray")

    global invno_diff
    invno_diff = 0
    for i in cart_detail:
        itemidincart = i[0]

        c.execute("SELECT * FROM item WHERE id = (?)",(itemidincart,))

        item_details = c.fetchall()

        #concept
        
        for f in item_details:
            if invno_diff != i[4] or invno_diff == 0:
                dash1 = Label(second_frame2, text="=====================================================")
                dash1.grid(row=rowdash1, column=coldash1, columnspan=2)

            # else:
            #     dash1 = Label(second_frame2, text="----------------------------------------------------------------------------------------")
            #     dash1.grid(row=rowdash1, column=coldash1, columnspan=2)

            if invno_diff != i[4] or invno_diff == 0:
                global getinvoicenum
                getinvoicenum = i[4]
                action_w_arg6 = partial(getbuyerdetail,getinvoicenum)
                showinvoice = Button(second_frame2, text=("Invoice No: "+i[4]), command=action_w_arg6) # select * from checkout, if invoice number is not same, then print invoice number
                showinvoice.grid(row=rowinv, column=colinv)

                if i[3] == "ToShip":
                    getinvoicenum = i[4]
                    action_w_arg4 = partial(areshipped,getinvoicenum)
                    cancelorder_btn = Button(second_frame2, text="Shipped to buyer", borderwidth=0, fg="gray", command=action_w_arg4)
                    cancelorder_btn.grid(row=rowccl, column=colccl, padx=(140,0))

                elif i[3] == "ToReceive":
                    getinvoicenum = i[4]
                    action_w_arg5 = partial(arereceived,getinvoicenum)
                    cancelorder_btn = Button(second_frame2, text="Received by buyer", borderwidth=0, fg="gray", command=action_w_arg5)
                    cancelorder_btn.grid(row=rowccl, column=colccl, padx=(140,0))

                dash2 = Label(second_frame2, text="----------------------------------------------------------------------------------------")
                dash2.grid(row=rowdash2, column=coldash2, columnspan=2)

            else:
                dash2 = Label(second_frame2, text="----------------------------------------------------------------------------------------")
                dash2.grid(row=rowdash2, column=coldash2, columnspan=2)
            

            img=Image.open(f[8]) # read the image file
            img=img.resize((100,100)) # new width & height
            img=ImageTk.PhotoImage(img, master=second_frame2)
            e1 =tk.Label(second_frame2)
            e1.grid(row=rowpic,column=colpic, rowspan=4, padx=(0,20))
            e1.image = img
            e1['image']=img # garbage collection 

            showname = Label(second_frame2, text=f[0])
            showname.grid(row=rowname,column=colname, sticky=W, padx=(0,40))

            showprice = Label(second_frame2, text=("RM "+f[1]+"."+f[2]+" per unit"))
            showprice.grid(row=rowprice1,column=colprice1, sticky=W, padx=(0,40))

            showstock = Label(second_frame2, text=("Quantity: "+i[2]))
            showstock.grid(row=rowstock,column=colstock, sticky=W, padx=(0,40))

            totalprice = (int(f[1])+(int(f[2])/100))*int(i[2])
            totalprice_2dp = "{:.2f}".format(totalprice)

            showtotalprice = Label(second_frame2, text=("Total: RM "+str(totalprice_2dp)))
            showtotalprice.grid(row=rowprice2,column=colprice2, sticky=W, padx=(0,40))

            # global getitemid2
            # getitemid2 = f[9]
            # action_w_arg3 = partial(cancelOrder,getitemid2) # add a status in checkout (eg. preparing, shipping, delivered)
            # editcart_btn = Button(second_frame2, text="Edit", borderwidth=0, fg="gray", command=action_w_arg3)
            # editcart_btn.grid(row=rowedit, column=coledit, padx=30)


            # Dash 1
            if invno_diff != i[4] or invno_diff == 0:
                rowdash1 = rowdash1 + 7
                coldash1 = 0

            else:
                rowdash1 = rowdash1 + 7
                coldash1 = 0


            # invoice number
            if invno_diff != i[4] or invno_diff == 0:
                rowinv = rowinv + 7
                colinv = 0

            else:
                rowinv = rowinv + 7
                colinv = 0

            # cancel order
            if invno_diff != i[4] or invno_diff == 0:
                rowccl = rowccl + 7
                colccl = 1

            else:
                rowccl = rowccl + 7
                colccl = 1

            # Dash 2
            if invno_diff != i[4] or invno_diff == 0:
                rowdash2 = rowdash2 + 7
                coldash2 = 0

            else:
                rowdash2 = rowdash2 + 7
                coldash2 = 0

            # picture
            if invno_diff != i[4] or invno_diff == 0:
                rowpic = rowpic + 7
                colpic = 0

            else:
                rowpic = rowpic + 7
                colpic = 0

            # name
            if invno_diff != i[4] or invno_diff == 0:
                rowname = rowname + 7
                colname = 1

            else:
                rowname = rowname + 7
                colname = 1

            # price 1
            if invno_diff != i[4] or invno_diff == 0:
                rowprice1 = rowprice1 + 7
                colprice1 = 1

            else:
                rowprice1 = rowprice1 + 7
                colprice1 = 1

            # stock
            if invno_diff != i[4] or invno_diff == 0:
                rowstock = rowstock + 7
                colstock = 1

            else:
                rowstock = rowstock + 7
                colstock = 1

            # price 2
            if invno_diff != i[4] or invno_diff == 0:
                rowprice2 = rowprice2 + 7
                colprice2 = 1

            else:
                rowprice2 = rowprice2 + 7
                colprice2 = 1
            
            invno_diff = i[4]

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    checkorderpage.mainloop()

def sellerPageQuit():

    sellerloginpage.destroy()

    loginPage()

def loginagain_seller():
    global e10
    global sellerloginpage
    sellerloginpage = Tk()
    sellerloginpage.title('MMU Grocery')
    sellerloginpage.iconbitmap("D:\Grocery Logo Icon\grocery_logo_rbg.ico")
    sellerloginpage.geometry("560x700")
    e10 = "seller"

    main_frame = Frame(sellerloginpage, width=530, height=600)
    main_frame.grid(row=1,column=0)

    my_canvas = Canvas(main_frame, width=530, height=550)
    my_canvas.grid(row=1,column=0)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.grid(column=1, row=1, sticky='NS')

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

    second_frame = Frame(my_canvas, width=530, height=600)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")



    sellerimage = PhotoImage(file="D:\\Grocery Logo Icon\\user_25x29.png")
    seller_details_icon = Button(image=sellerimage, borderwidth=0, cursor="mouse", command=editUserDetails)
    seller_details_icon.place(x=435, y=10)

    soldimage = PhotoImage(file="D:\\Grocery Logo Icon\\bill-27.png")
    soldimage_icon = Button(image=soldimage, borderwidth=0, cursor="mouse", command=checkorder)
    soldimage_icon.place(x=480, y=10)

    logoutimage = PhotoImage(file="D:\Grocery Logo Icon\logout4-removebg-29x29.png")
    logoutimage_icon = Button(image=logoutimage, borderwidth=0, cursor="mouse", command=sellerPageQuit)
    # logoutimage_icon.grid(row=0, column=0, padx=(400,0), pady=(7,0))
    logoutimage_icon.place(x=525, y=10)

    addimage = PhotoImage(file="D:\Grocery Logo Icon\plus-4-64.png", master=sellerloginpage)
    addimage_icon = Button(master=sellerloginpage, image=addimage, borderwidth=0, cursor="mouse", command=addItem)
    addimage_icon.place(x=480, y=627)

    sellingitem_label = Label(sellerloginpage, text="Your selling item")
    sellingitem_label.grid(row=0, column=0, pady=(50,0))

    def sortByAll():
        global sortStatus4
        sortStatus4 = 1
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM item WHERE seller_username = (?)",(e3,))
        global seller_details
        seller_details = c.fetchall()
        sellerloginpage.destroy()
        loginagain_seller()

    def sortByVege():
        global sortStatus4
        sortStatus4 = 2
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM item WHERE seller_username = (?) and category=(?)",(e3,"Vegetable"))
        global seller_details
        seller_details = c.fetchall()
        sellerloginpage.destroy()
        loginagain_seller()


    def sortByFruits():
        global sortStatus4
        sortStatus4 = 3
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM item WHERE seller_username = (?) and category=(?)",(e3,"Fruits"))
        global seller_details
        seller_details = c.fetchall()
        sellerloginpage.destroy()
        loginagain_seller()


    def sortByHerb():
        global sortStatus4
        sortStatus4 = 4
        sortbyHerb.config(state=DISABLED, bg="lightgray")
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM item WHERE seller_username = (?) and category=(?)",(e3,"Herb"))
        global seller_details
        seller_details = c.fetchall()
        sellerloginpage.destroy()
        loginagain_seller()


    sortbyAll = Button(sellerloginpage, text="All", width=9, bg="#FFF0BC", command=sortByAll)
    sortbyAll.place(x=10, y=10)

    sortbyVege = Button(sellerloginpage, text="Vegetable", width=9, bg="#F5FFBC", command=sortByVege)
    sortbyVege.place(x=100, y=10)

    sortbyFruits = Button(sellerloginpage, text="Fruit", width=9, bg="#D0FFBC", command=sortByFruits)
    sortbyFruits.place(x=190, y=10)

    sortbyHerb = Button(sellerloginpage, text="Herb", width=9, bg="#BDFFFE", command=sortByHerb)
    sortbyHerb.place(x=280, y=10)

    





    if sortStatus4 == 1:
        sortbyAll.config(state=DISABLED, bg="lightgray")
        # global sortStatus
        # sortStatus = 1
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM item WHERE seller_username = (?)",(e3,))
        global seller_details
        seller_details = c.fetchall()

    elif sortStatus4 == 2:
        sortbyVege.config(state=DISABLED, bg="lightgray")

    elif sortStatus4 == 3:
        sortbyFruits.config(state=DISABLED, bg="lightgray")

    elif sortStatus4 == 4:
        sortbyHerb.config(state=DISABLED, bg="lightgray")

    #concept
    
    rowpic = 2
    colpic = 0
    rowname = 3
    colname = 0
    rowprice = 4
    colprice = 0
    rowstock = 5
    colstock = 0
    rowedit = 6
    coledit = 0

    for f in seller_details:
        img=Image.open(f[8]) # read the image file
        img=img.resize((150,150)) # new width & height
        img=ImageTk.PhotoImage(img)
        getitemid_show = f[9]
        action_a_arg = partial(showItemDetails,getitemid_show)
        e1 =tk.Button(second_frame, command=action_a_arg)
        e1.grid(row=rowpic,column=colpic, padx=10)
        e1.image = img
        e1['image']=img # garbage collection 

        showname = Label(second_frame, text=f[0])
        showname.grid(row=rowname,column=colname)

        showprice = Label(second_frame, text=("RM "+f[1]+"."+f[2]))
        showprice.grid(row=rowprice,column=colprice)

        showstock = Label(second_frame, text=("Stock Left: "+f[11]))
        showstock.grid(row=rowstock,column=colstock)

        global getitemid
        getitemid = f[9]
        action_w_arg = partial(editItemDetails,getitemid)
        edititem_btn = Button(second_frame, width=18, text="Edit item", bg='#FFBFBF', command=action_w_arg)
        edititem_btn.grid(row=rowedit,column=coledit, pady=(0,15))

        if(colpic==2): # start new line after third column
            rowpic=rowpic+5# start wtih next row
            colpic=0    # start with first column
        else:       # within the same row 
            colpic=colpic+1

        if(colname==2):
            rowname=rowname+5
            colname=0
        else:
            colname=colname+1

        if(colprice==2):
            rowprice=rowprice+5
            colprice=0
        else:
            colprice=colprice+1

        if(colstock==2):
            rowstock=rowstock+5
            colstock=0
        else:
            colstock=colstock+1

        if(coledit==2):
            rowedit=rowedit+5
            coledit=0
        else:
            coledit=coledit+1


    sellerloginpage.mainloop()

sortStatus4 = 1
def sellerLogin():


    if enterid.get() == "" or enterid["state"]==DISABLED or enterpass.get() == "" or enterpass["state"]==DISABLED:
        messagebox.showerror("Error","All fields are required",parent=root)

    else:
        # Create a database or connect to one
        conn = sqlite3.connect('grocery.db')
        # Create cursor
        c = conn.cursor()
        c.execute("SELECT * FROM seller WHERE username = (?) and password1 = (?) ",(enterid.get(),enterpass.get()))
                
        seller_details = c.fetchone()

        if seller_details:
            global e3
            e3 = enterid.get()

            global e4
            e4 = enterpass.get()
            
            root.destroy()

            loginagain_seller()
            

        else:
            messagebox.showerror("Error","Invalid Username and/or Password\nPlease try again.")

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

loginPage()
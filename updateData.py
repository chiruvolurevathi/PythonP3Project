from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="revathi"

)
mycursor = mydb.cursor()

mycursor.execute("UPDATE studentdetails SET aadharCard= 222222 WHERE Id=1;")
mycursor.execute("commit")
MessageBox.showinfo("Status","Data updated SuccessFully")


mydb.close()

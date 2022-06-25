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

mycursor.execute("DELETE FROM studentdetails WHERE Id=1;")
mycursor.execute("commit")
MessageBox.showinfo("Status","Data deleted SuccessFully")



mydb.close()
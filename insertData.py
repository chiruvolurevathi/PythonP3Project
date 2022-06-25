from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


try:
    mydb = mysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="revathi"

    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "INSERT INTO studentdetails(Id,name,aadharCard,parentName,phoneNumber,class,section,feesStatus)VALUES (1,'Adithya',1252421,'pranav',923434322,7,'A','paid');")

    mycursor.execute("commit")
    MessageBox.showinfo("Status", "Data Inserted SuccessFully")

    mydb.close()
except:
    MessageBox.showinfo("Status", "Duplicate values are not allowed")


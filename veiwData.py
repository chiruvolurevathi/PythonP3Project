from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root=Tk()
mydb = mysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="revathi"

)
mycursor = mydb.cursor()

mycursor.execute("select * from studentdetails")
rows=mycursor.fetchall()

tree=ttk.Treeview(root)

tree["columns"] =("Id","name","aadharCard","parentName","phoneNumber","class","section","feesStatus")
tree.column("Id",width=100,minwidth=50)
tree.column("name",width=100,minwidth=50)
tree.column("aadharCard",width=100,minwidth=50)
tree.column("parentName",width=100,minwidth=50)
tree.column("phoneNumber",width=100,minwidth=50)
tree.column("class",width=100,minwidth=60)
tree.column("section",width=100,minwidth=70)
tree.column("feesStatus",width=100,minwidth=70)

tree.heading("Id",text="Id")
tree.heading("name",text="name")
tree.heading("aadharCard",text="aadharCard")
tree.heading("parentName",text="parentName")
tree.heading("phoneNumber",text="phoneNumber")
tree.heading("class",text="class")
tree.heading("section",text="section")
tree.heading("feesStatus",text="section")

i=0
for row in rows:
    tree.insert("",i,text="",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    i=i+1

tree.pack()

MessageBox.showinfo("Status","Data fetched successfully")


mydb.close()
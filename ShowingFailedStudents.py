from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
root=Tk()
root.title("revathi")
root.geometry('400x450')
root.title("entering Marks")

def submitdata():
    subject_data = (subject.get())
    if (subject_data==""):
        MessageBox.showinfo("Insert Status","You need to enter all the Details")
    else:
        try:
            mydb = mysql.connect(
                host="localhost",
                user="root",
                password="root",
                database="revathi"

            )
            mycursor = mydb.cursor()
            mycursor.execute("select Id from subjectmarks where "+subject_data+" > 40;")
            rows=mycursor.fetchall()
            print(subject_data)
            print(rows)
            inner=Tk()
            j=0
            for i in rows:
                insert=Label(inner,text=i[0])
                insert.grid(row=j,column=0)
                j=j+1
            mydb.close()
        except:
            MessageBox.showinfo("Insert Status","You need to enter Subject name Correctly(maths,science,social,language)")

    subject.delete(0, END)

subject=Label(root,text="enter the Subject")
subject.place(x=20,y=60)

subject=Entry()
subject.place(x=150,y=60)

insert=Button(root,text="submit",fg='green',command=submitdata)
insert.place(x=150,y=120)

root.mainloop()
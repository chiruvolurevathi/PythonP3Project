import winreg
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkinter.ttk import Notebook
root = Tk()

root.title("revathi")
root.geometry('800x850+0+0')
notebook=Notebook(root)
notebook.pack(pady=10,expand=False)
def View_data():
    Id_data = Id.get()
    if Id_data != "":
        anx=Tk()
        anx.title("Data from DataBase")
        anx.geometry('700x800')
        label = Label(anx, text="Data of the Student  having Id'"+Id_data+"'", font='time 15 bold')
        label.grid(row=0, column=0,columnspan=20)
        d1 = Label(anx,text='Id',font='time 9 bold')
        d1.grid(row=1,column=1,padx=2,pady=2)
        d2 = Label(anx, text='name', font='time 9 bold')
        d2.grid(row=1, column=2,padx=2,pady=2)
        d3 = Label(anx, text='AdharCard', font='time 9 bold')
        d3.grid(row=1, column=3,padx=2,pady=2)
        d4 = Label(anx, text='Parent Name', font='time 9 bold')
        d4.grid(row=1, column=4, padx=2, pady=2)
        d5 = Label(anx, text='phoneNumber', font='time 9 bold')
        d5.grid(row=1, column=5, padx=2, pady=2)
        d6 = Label(anx, text='class', font='time 9 bold')
        d6.grid(row=1, column=6, padx=2, pady=2)
        d7 = Label(anx, text='section', font='time 9 bold')
        d7.grid(row=1, column=7, padx=2, pady=2)
        d8 = Label(anx, text='feesStatus', font='time 9 bold')
        d8.grid(row=1, column=8, padx=2, pady=2)
        try:
            mydb = mysql.connect(
                host="localhost",
                user="root",
                password="root",
                database="revathi"

            )
            mycursor = mydb.cursor()
            mycursor.execute("select * from studentdetails where Id = "+Id_data+";")
            rows = mycursor.fetchall()
            mydb.close()
            num=2
            for i in rows:
                id = Label(anx, text=i[0], font='time 9 bold')
                id.grid(row=num, column=1, padx=10, pady=10)
                name = Label(anx, text=i[1], font='time 9 bold')
                name.grid(row=num, column=2, padx=10, pady=10)
                AdharCard= Label(anx, text=i[2], font='time 9 bold')
                AdharCard.grid(row=num, column=3, padx=10, pady=10)
                Pname = Label(anx, text=i[3], font='time 9 bold')
                Pname.grid(row=num, column=4, padx=10, pady=10)
                Pnumber = Label(anx, text=i[4], font='time 9 bold')
                Pnumber.grid(row=num, column=5, padx=10, pady=10)
                Class = Label(anx, text=i[5], font='time 9 bold')
                Class.grid(row=num, column=6, padx=10, pady=10)
                Section = Label(anx, text=i[6], font='time 9 bold')
                Section.grid(row=num, column=7, padx=10, pady=10)
                feesStatus = Label(anx, text=i[7], font='time 9 bold')
                feesStatus.grid(row=num, column=8, padx=10, pady=10)

            MessageBox.showinfo("Status", "Data fetched successfully  of student having Id "+Id_data+"")
        except:
            MessageBox.showinfo("Status", "Data  not fetched successfully  of student having Id " + Id_data + " please enter correct data")
    else:
        MessageBox.showinfo("Status", "Please enter data")

def admin_Submit():
    Id_data=Id.get()
    fstatus=e_feesstatus.get()
    if Id_data != "" and fstatus != "":
        try:
            mydb = mysql.connect(
                host="localhost",
                user="root",
                password="root",
                database="revathi"

            )
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE studentdetails SET feesStatus = '"+fstatus+"' WHERE Id="+Id_data+";")
            mycursor.execute("commit")
            mydb.close()
            MessageBox.showinfo("Status", "Fees Status Inserted  successfully if you want to see data give ID and press View Details")
        except:
            MessageBox.showinfo("Status","Fees Status not inserted enter valid Id and Data")

    else:
        MessageBox.showinfo("Status", "We Need to Enter both Id and fees Status to Update the Fees Status")


    Id.delete(0, END)
    e_feesstatus.delete(0, END)

def teacher_Submit():
    # nx=Tk()
    # nx.title("Data from DataBase")
    # nx.geometry('500x600')
    # label=Label(nx,text='Data of the Student',font='time 15 bold')
    # label.grid(row=0,column=0)
    Id_data = e2_Id.get()
    if Id_data != "":
        anx = Tk()
        anx.title("Marks Data of Student ")
        anx.geometry('500x600')
        label = Label(anx, text="Marks Data of  selected Student of having Id  '"+Id_data+"'", font='time 15 bold')
        label.grid(row=0, column=0, columnspan=20)
        d1 = Label(anx, text='Id', font='time 9 bold')
        d1.grid(row=1, column=1, padx=10, pady=10)
        d2 = Label(anx, text='maths', font='time 9 bold')
        d2.grid(row=1, column=2, padx=10, pady=10)
        d3 = Label(anx, text='science', font='time 9 bold')
        d3.grid(row=1, column=3, padx=10, pady=10)
        d4 = Label(anx, text='social', font='time 9 bold')
        d4.grid(row=1, column=4, padx=10, pady=10)
        d5 = Label(anx, text='language', font='time 9 bold')
        d5.grid(row=1, column=5, padx=10, pady=10)
        try:
            mydb = mysql.connect(
                host="localhost",
                user="root",
                password="root",
                database="revathi"

            )
            mycursor = mydb.cursor()
            mycursor.execute("select * from subjectmarks where Id = " + Id_data + ";")
            rows = mycursor.fetchall()
            mydb.close()
            num = 2
            for i in rows:
                id = Label(anx, text=i[0], font='time 9 bold')
                id.grid(row=num, column=1, padx=10, pady=10)
                maths = Label(anx, text=i[1], font='time 9 bold')
                maths.grid(row=num, column=2, padx=10, pady=10)
                science = Label(anx, text=i[2], font='time 9 bold')
                science.grid(row=num, column=3, padx=10, pady=10)
                social = Label(anx, text=i[3], font='time 9 bold')
                social.grid(row=num, column=4, padx=10, pady=10)
                language = Label(anx, text=i[4], font='time 9 bold')
                language.grid(row=num, column=5, padx=10, pady=10)
                MessageBox.showinfo("Status", "Marks Data fetched successfully of student having Id "+Id_data+" see new Window")
                e2_Id.delete(0, END)
        except:
            MessageBox.showinfo("Status", "Please Enter valid Data")
    else:
        MessageBox.showinfo("Status", "Please Enter the Data")



frame1=Frame(notebook,width=1000,height=500)
Label(frame1, text='Enter your ID to View the Details',fg='blue').pack()
Id=Entry(frame1,width=50)
Id.pack()
view_data=Button(frame1,text="ViewDetails",fg='red',command=View_data)
view_data.pack()

Label(frame1, text='Enter Id and status to Update the feesStatus',fg='blue').pack()
e_feesstatus=Entry(frame1,width=50)
e_feesstatus.pack()
submit_button=Button(frame1,text="submit",fg='red',command=admin_Submit)
submit_button.pack()
frame1.pack()

frame2=Frame(notebook,width=1000,height=500)
Label(frame2, text='Enter ID please to Get Student Details').pack()
e2_Id=Entry(frame2,width=50)
submit_button=Button(frame2,text="submit",fg='red',command=teacher_Submit)
e2_Id.pack()
submit_button.pack()
frame2.pack()


notebook.add(frame1,text="Admin Page")

notebook.add(frame2,text="Teacher Page")


root.mainloop()

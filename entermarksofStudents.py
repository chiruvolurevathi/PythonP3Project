from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
def submitdata():

    id_data=id.get()
    maths_data=maths.get()
    science_data=science.get()
    social_data=social.get()
    language_data=language.get()
    id_data=(id_data)
    id.delete(0, END)
    maths.delete(0, END)
    science.delete(0, END)
    social.delete(0, END)
    language.delete(0, END)
    if (id_data== "" or maths_data=="" or science_data=="" or social_data=="" or language_data==""):
        MessageBox.showinfo("Insert Status","You need to enter all the Details")
    elif (id_data.isalpha() or maths_data.isalpha() or science_data.isalpha() or social_data.isalpha() or language_data.isalpha()):
        MessageBox.showinfo("Status", "Id  and Marks should be Integer only")
    else:
        try:
            mydb = mysql.connect(
                host="localhost",
                user="root",
                password="root",
                database="revathi"

            )
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO subjectmarks(Id,maths,science,social,language)VALUES ('"+str(id_data)+"','"+maths_data+"','"+science_data+"','"+social_data+"','"+language_data+"');")
            mycursor.execute("commit")
            MessageBox.showinfo("Status", "Data Inserted SuccessFully")
            mydb.close()

        except:
            MessageBox.showinfo("Status", "Data can not be duplicate values")

root=Tk()
root.title("revathi")
root.geometry('800x850')
root.title("entering Marks")


id=Label(root,text="enter the Id")
id.place(x=20,y=30)

maths=Label(root,text="enter the maths")
maths.place(x=20,y=60)

science=Label(root,text="enter the science")
science.place(x=20,y=90)

social=Label(root,text="enter the social")
social.place(x=20,y=120)

language=Label(root,text="enter the language")
language.place(x=20,y=150)

id=Entry()
id.place(x=150,y=30)

maths=Entry()
maths.place(x=150,y=60)

science=Entry()
science.place(x=150,y=90)

social=Entry()
social.place(x=150,y=120)

language=Entry()
language.place(x=150,y=150)

insert=Button(root,text="Insert",fg='green',command=submitdata)
insert.place(x=150,y=200)

root.mainloop()

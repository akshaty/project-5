from Tkinter import *
def EntryM():
 def insert():
    import pymysql
 #connection with the database1
    z=e1.get() 
    x=e2.get()
    m=int(e3.get())
    n=int(e4.get())
    l=int(e5.get())
    k=int(e6.get())
    p=int(e7.get())
    connect=pymysql.connect(host="localhost",user="akshat",passwd="Super_10",db="project")
    cur=connect.cursor()
 #Inserting data in the database
    sql_command="INSERT INTO Marks values(%s,%s,%s,%s,%s,%s,%s)"
    data=(z,x,int(m),int(n),int(l),int(k),int(p))
    cur.execute(sql_command,data) 
    #print z,x,m,n,l,k,p
    connect.commit()
    connect.close()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)



 window = Tk()
 window.title("Marks updation")
 A=Label(window, text="Rollno")
 B=Label(window, text="Name")
 C=Label(window, text="English")
 D=Label(window, text="Hindi")
 E=Label(window, text="Maths")
 F=Label(window, text="Science")
 G=Label(window, text="Computers")

 A.grid(row=0,column=0)
 B.grid(row=1,column=0)
 C.grid(row=2,column=0)
 D.grid(row=3,column=0)
 E.grid(row=4,column=0)
 F.grid(row=5,column=0)
 G.grid(row=6,column=0)
 e1=Entry(window)
 e2=Entry(window)
 e3=Entry(window)
 e4=Entry(window)
 e5=Entry(window)
 e6=Entry(window)
 e7=Entry(window)
 e1.grid(row=0,column=1)
 e2.grid(row=1,column=1)
 e3.grid(row=2,column=1)
 e4.grid(row=3,column=1)
 e5.grid(row=4,column=1)
 e6.grid(row=5,column=1)
 e7.grid(row=6,column=1)
 Q=Button(window,text="Save",fg="Blue",command=insert) 
 W=Button(window,text="Quit",fg="Red",command=window.destroy)
 W.grid(row=7, column=2)
 Q.grid(row=7,column=1)
 window.mainloop()
    
def EntryA():
 def insert1():
    import pymysql
 #connection with the database1
    z=e1.get() 
    x=e2.get()
    m=int(e3.get())
    n=int(e4.get())
    l=int(e5.get())
    k=int(e6.get())
    p=int(e7.get())
    connect=pymysql.connect(host="localhost",user="akshat",passwd="Super_10",db="project")
    cur=connect.cursor()
 #Inserting data in the database
    sql_command="INSERT INTO Attendence values(%s,%s,%s,%s,%s,%s,%s)"
    data=(z,x,int(m),int(n),int(l),int(k),int(p))
    cur.execute(sql_command,data) 
    #print z,x,m,n,l,k,p
    connect.commit()
    connect.close()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)



 window = Tk()
 window.title("Attendence updation")
 A=Label(window, text="Rollno")
 B=Label(window, text="Name")
 C=Label(window, text="English")
 D=Label(window, text="Hindi")
 E=Label(window, text="Maths")
 F=Label(window, text="Science")
 G=Label(window, text="Computers")

 A.grid(row=0,column=0)
 B.grid(row=1,column=0)
 C.grid(row=2,column=0)
 D.grid(row=3,column=0)
 E.grid(row=4,column=0)
 F.grid(row=5,column=0)
 G.grid(row=6,column=0)
 e1=Entry(window)
 e2=Entry(window)
 e3=Entry(window)
 e4=Entry(window)
 e5=Entry(window)
 e6=Entry(window)
 e7=Entry(window)
 e1.grid(row=0,column=1)
 e2.grid(row=1,column=1)
 e3.grid(row=2,column=1)
 e4.grid(row=3,column=1)
 e5.grid(row=4,column=1)
 e6.grid(row=5,column=1)
 e7.grid(row=6,column=1)
 Q=Button(window,text="Save",fg="Blue",command=insert1) 
 W=Button(window,text="Quit",fg="Red",command=window.destroy)
 W.grid(row=7, column=2)
 Q.grid(row=7,column=1)
 window.mainloop()
    
    
window2 = Tk()
window2.title("Entry Choice")
Q=Button(window2,text="Marks",fg="Blue",command=EntryM) 
W=Button(window2,text="Attendence",fg="Red",command=EntryA)
W.grid(row=1, column=0)
Q.grid(row=1,column=2)
window2.mainloop()

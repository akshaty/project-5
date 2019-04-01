from Tkinter import *
def Marks():
 def Results1():
    import pymysql
    l=f1.get()
    connect=pymysql.connect(host="localhost",user="akshat",passwd="Super_10",db="project")
    cur=connect.cursor()
    sql_command="Select English,Hindi,Maths,Science,Computers from Marks where Rollno=%s"
    kp=l
    try:
        cur.execute(sql_command,kp)
    except:
        print "<Error: Account name already Exist>" 
    data=cur.fetchall()
    print "Marks of English,Hindi,Science,Maths,Computers out of 100 are as follows "
    print data
    connect.commit()
    connect.close()
 window = Tk()
 window.title("Marks info")
 A=Label(window, text="Rollno")

 A.grid(row=0,column=0)
 f1=Entry(window)
 f1.grid(row=0,column=1)
 Q=Button(window,text="Ok",fg="Blue",command=Results1) 
 W=Button(window,text="Quit",fg="Red",command=window.destroy)
 W.grid(row=2, column=0)
 Q.grid(row=2,column=2)
 window.mainloop()
def Attendence():
 def Results2():
    import pymysql
    m=g1.get()
    connect=pymysql.connect(host="localhost",user="akshat",passwd="Super_10",db="project")
    cur=connect.cursor()
    sql_command="Select English,Hindi,Maths,Science,Computers from Attendence where Rollno=%s"
    ab=m
    try:
        cur.execute(sql_command,ab)
    except:
        print "<Error: Account name already Exist>" 
    data1=cur.fetchall()
    print "Attendence of English,Hindi,Science,Maths,Computers out of 30 are as follows "
    print data1
    connect.commit()
    connect.close()
 window = Tk()
 window.title("Attendence info")
 A=Label(window, text="Rollno")

 A.grid(row=0,column=0)
 g1=Entry(window)
 g1.grid(row=0,column=1)
 Q=Button(window,text="Ok",fg="Blue",command=Results2) 
 W=Button(window,text="Quit",fg="Red",command=window.destroy)
 W.grid(row=2, column=0)
 Q.grid(row=2,column=2)
 window.mainloop()


window1 = Tk()
window1.title("Choice")
Q=Button(window1,text="Marks",fg="Blue",command=Marks) 
W=Button(window1,text="Attendence",fg="Red",command=Attendence)
W.grid(row=2, column=0)
Q.grid(row=2,column=2)
window1.mainloop()

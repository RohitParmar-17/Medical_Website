from tkinter import *
import mysql.connector
from tkinter import messagebox
import main

db=mysql.connector.connect(user='root',password='Rohit@17',host='localhost',database='db_proj1')
c=db.cursor()
       
class College:
    def __init__(self):
        self.root=Tk()
        self.root.title('College')
        self.root.geometry('300x150')

        self.l1=Label(self.root,text='Operation ')
        self.l1.grid(row=0,column=0)
        self.clicked=StringVar()
        self.clicked.set('Choose')
        self.options=["Insert","Delete","Update","Show"]
        self.drop=OptionMenu(self.root,self.clicked,*self.options)
        self.drop.grid(row=0,column=1)
        self.b1=Button(self.root,text="Submit",width=20,command=self.next1)
        self.b1.grid(row=1,column=0,columnspan=2)

    def next1(self):
        if self.clicked.get()=="Insert":
            self.com_insert()
        if self.clicked.get()=="Delete":
            self.com_delete()
        if self.clicked.get()=="Update":
            self.com1_update()
        if self.clicked.get()=="Show":
            self.com_show()
        self.root.destroy()
        
    def com_insert(self):
        self.root1=Tk()
        self.root1.title('College Insertion')
        self.root1.geometry('300x150')
                    
        self.l1=Label(self.root1,text="College RegId ")
        self.l1.grid(row=0,column=0)
        v1=StringVar(self.root1,value="None")
        self.e1=Entry(self.root1,textvariable=v1,borderwidth=5)
        self.e1.grid(row=0,column=1)
                    
        self.l2=Label(self.root1,text="College Name ")
        self.l2.grid(row=1,column=0)
        v2=StringVar(self.root1,value="None")
        self.e2=Entry(self.root1,textvariable=v2,borderwidth=5)
        self.e2.grid(row=1,column=1)
                    
        self.l3=Label(self.root1,text="College Location ")
        self.l3.grid(row=2,column=0)
        v3=StringVar(self.root1,value="None")
        self.e3=Entry(self.root1,textvariable=v3,borderwidth=5)
        self.e3.grid(row=2,column=1)

        self.b1=Button(self.root1,text="Submit",width=20,command=self.f_insert)
        self.b1.grid(row=3,column=0,columnspan=2)
        
    def f_insert(self):
        if "None"or"" in [self.e1.get(),self.e2.get(),self.e3.get()]:
            messagebox.showerror("Error","All important fields not filled")
        else:
            try:
                c.execute(f'insert into College values ("{int(self.e1.get())}","{self.e2.get()}","{self.e3.get()}");')
                db.commit()
                self.root1.destroy()
                messagebox.showinfo("Inserted","Data inserted succesfully")
            except mysql.connector.errors.IntegrityError:
                  db.rollback()
                  self.root1.destroy()
                  messagebox.showerror("Error","Data already exist in relation")
            except:
                  db.rollback()
                  self.root1.destroy()
                  messagebox.showerror("Error","The required data could not be inserted")  
            finally:
                main.main()
        
        
    
    def com_delete(self):
        self.root2=Tk()
        self.root2.title('College Deletion')
        self.root2.geometry('300x150')
        
        self.l1=Label(self.root2,text=" College RegId")
        self.l1.grid(row=0,column=0)
        self.v4=StringVar(self.root2,value="None")
        self.list1=[]
        c.execute(f"select * from College")
        
        for i in c.fetchall():
            self.list1.append(i[0])
            
        self.drop=OptionMenu(self.root2,self.v4,*self.list1)
        self.drop.grid(row=0,column=1)
        self.b1=Button(self.root2,text="Submit",width=20,command=self.f_delete)
        self.b1.grid(row=1,column=0,columnspan=2)

    def f_delete(self):
        if self.v4.get() == "None"or"":
               messagebox.showerror("Error","College RegId not selected")
        else:
            try:
                  c.execute(f'DELETE FROM College WHERE Cregid= "{int(self.v4.get())}";')
                  db.commit()
                  self.root2.destroy()
                  messagebox.showinfo("Succesfull","Sucessfully deleted")
            except:
                  db.rollback()
                  self.root2.destroy()
                  messagebox.showerror("Error","Could not be deleted")
            finally:
                main.main()
                
    def com1_update(self):
        self.root3=Tk()
        self.root3.title('College Updation')
        self.root3.geometry('300x150')

        self.l1=Label(self.root3,text=" College RegId")
        self.l1.grid(row=0,column=0)
        self.v5=StringVar(self.root3,value="None")
        self.list2=[]
        c.execute(f"select * from College")
        
        for i in c.fetchall():
            self.list2.append(i[0])
            
        self.drop=OptionMenu(self.root3,self.v5,*self.list2)
        self.drop.grid(row=0,column=1)
        self.b1=Button(self.root3,text="Submit",width=20,command=self.com2_update)
        self.b1.grid(row=1,column=0,columnspan=2)
        
    def com2_update(self):
        self.root3.destroy()
        self.root4=Tk()
        self.root4.title('College Updation')
        self.root4.geometry('300x150')
                    
        self.l2=Label(self.root4,text="College Name ")
        self.l2.grid(row=1,column=0)
        self.e2s=Entry(self.root4,borderwidth=5)
        self.e2s.grid(row=1,column=1)
                    
        self.l3=Label(self.root4,text="College Location")
        self.l3.grid(row=2,column=0)
        self.e3s=Entry(self.root4,borderwidth=5)
        self.e3s.grid(row=2,column=1)

        c.execute(f"SELECT * FROM College WHERE Cregid = {int(self.v5.get())}")
        records=c.fetchall()
        self.b1=Button(self.root4,text="Save Changes",width=20,command=self.f_update)
        self.b1.grid(row=3,column=0,columnspan=2)
    
        for i in records:
            self.e2s.insert(0,i[1])
            self.e3s.insert(0,i[2])
        
    def f_update(self):
         c.execute(f'UPDATE College SET Cname = "{self.e2s.get()}",Clocation = "{self.e3s.get()}" WHERE Cregid= "{int(self.v5.get())}";' )
         db.commit()
         self.root4.destroy()
         messagebox.showinfo("Succesfull","Sucessfully Updated")
         main.main()
         
    def com_show(self):
        self.root5=Tk()
        self.root5.title("College Database")
        self.root5.geometry('300x150')
        
        self.l8=Label(self.root5,text="Cregid  ")
        self.l8.grid(row=0,column=0)
        self.l9=Label(self.root5,text="Cname  ")
        self.l9.grid(row=0,column=1)
        self.l10=Label(self.root5,text="Clocation  ")
        self.l10.grid(row=0,column=2)
        
        c.execute(f'select * from College')
        j=1
        for i in c.fetchall():
            self.l6=Label(self.root5,text=f'{i[0]}')
            self.l6.grid(row=j,column=0)
            j=j+1
        c.execute(f'select * from College')
        j=1
        for i in c.fetchall():
            self.l11=Label(self.root5,text=f'{i[1]}')
            self.l11.grid(row=j,column=1)
            j=j+1
        c.execute(f'select * from College')
        j=1
        for i in c.fetchall():
            self.l12=Label(self.root5,text=f'{i[2]}')
            self.l12.grid(row=j,column=2)
            j=j+1
            
        self.b5=Button(self.root5,text="Exit",width=20,command=self.dest)
        self.b5.grid(row=j,column=0,columnspan=2)
        
    def dest(self):
            self.root5.destroy()
            main.main()

            
if __name__=="__main__":
    College()

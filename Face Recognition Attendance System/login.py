from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import tkinter
import os
import mysql.connector
from student_details import Student_Details
from train import Train_Data
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from main import Face_Recognition_Attendance_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()




class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        img=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Main Bg.jpg")
        img=img.resize((500,130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=6,y=0,width=500,height=130)

        img1=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Upper Image 2.jpg")
        img1=img1.resize((500,130), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=511,y=0,width=500,height=130)
        
        img2=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Upper Image 3.jpg")
        img2=img2.resize((500,130), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1016,y=0,width=500,height=130)

        img3=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Login Bg.jpg")
        img3=img3.resize((1530,710), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 30, "bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1530, height= 45)
        

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=200,width=340,height=450)

        
        img4=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Login Icon.png")
        img4=img4.resize((100,100), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl=Label(image=self.photoimg4,bg="black", borderwidth=0)
        f_lbl.place(x=730,y=205,width=100,height=100)

        get_str=Label(frame,text="Get Started", font=("times new roman",20,"bold"),fg="white", bg="black")
        get_str.place(x=95,y=110)
        
        username=lbl=Label(frame,text="Username:", font=("times new roman",15,"bold"),fg="white", bg="black")
        username.place(x=70,y=160)
        self.txtuser=ttk.Entry(frame,font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40,y=185,width=270)
        
        password=lbl=Label(frame,text="Password:", font=("times new roman",15,"bold"),fg="white", bg="black")
        password.place(x=70,y=230)
        self.txtpass=ttk.Entry(frame, font=("times new roman", 15, "bold"),show="*")
        self.txtpass.place(x=40,y=255,width=270)

        
        img5=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Login Icon.png")
        img5=img5.resize((25,25), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        f_lbl=Label(image=self.photoimg5,bg="black", borderwidth=0)
        f_lbl.place(x=650,y=358,width=25,height=25)
        
        img6=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Password Icon.png")
        img6=img6.resize((25,25), Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        f_lbl=Label(image=self.photoimg6,bg="black", borderwidth=0)
        f_lbl.place(x=650,y=429,width=25,height=25)

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110,y=308,width=120,height=35)
        
        registerbtn=Button(frame,text="New User Register",command=self.register_window, font=("times new roman",10,"bold"), borderwidth=0,fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15,y=353,width=160)
        
        registerbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window, font=("times new roman",10,"bold"), borderwidth=0,fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=10,y=373,width=160)
        
        footer_lbl=Label(bg_img,text="Note: First Input Valid Username and Valid Password", font=("times new roman", 25, "bold"),bg="white", fg="Blue")
        footer_lbl.place(x=0,y=607,width=1530, height= 45)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
                messagebox.showerror("Error","All fields Required")
        elif self.txtuser.get()=="Golu" and self.txtpass.get()=="ab8":
                messagebox.showinfo("Success","Welcome to Face Recognition Attendance System")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Lm87#nhJ365#e8",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (
                                                                            self.txtuser.get(),
                                                                            self.txtpass.get()                                                                    
                                                      ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password") 
            else:
                open_main=messagebox.askyesno("Yes/No","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_Attendance_System(self.new_window)
                else:
                    if not open_main:
                        return    
            conn.commit()
            self.clear()
            conn.close()


    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")



    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the Security Answer",parent=self.root2)
        elif self.new_pass.get()=="":
            messagebox.showerror("Error","Please enter the New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Lm87#nhJ365#e8",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_pass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset, please login with new password",parent=self.root2)
                self.root2.destroy()



    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email Address to reset the password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Lm87#nhJ365#e8",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Wrong Username","Please Enter the valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password", font=("times new roman", 20, "bold"),bg="white", fg="red" )
                l.place(x=0,y=10,relwidth=1)


                
                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman", 15, "bold"),bg="white")
                security_Q.place(x=50,y=80)
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"]=("Select","Your Favourite Sports", "Ypur Pet Name", "Your Birth Place")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                security_A=Label(self.root2,text="Security Answer",font=("times new roman", 15, "bold"),bg="white")
                security_A.place(x=50,y=150)
                self.txt_security=ttk.Entry(self.root2,font=("times new roman", 15, "bold"))
                self.txt_security.place(x=50,y=180,width=250)
                
                new_password=Label(self.root2,text="New Password",font=("times new roman", 15, "bold"),bg="white")
                new_password.place(x=50,y=220)
                self.new_pass=ttk.Entry(self.root2,font=("times new roman", 15, "bold"))
                self.new_pass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass, font=("times new roman", 20, "bold"),bg="green", fg="white" )
                btn.place(x=130,y=290)
                    








class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")


        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        
        img3=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Register.jpg")
        img3=img3.resize((1530,790), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        
        img2=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\RegisterL.jpg")
        img2=img2.resize((500,130), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=50,y=100,width=470,height=550)


        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20,y=20)


        fname=Label(frame,text="First Name",font=("times new roman", 15, "bold"),bg="white")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman", 15, "bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roman", 15, "bold"),bg="white")
        l_name.place(x=370,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact No",font=("times new roman", 15, "bold"),bg="white")
        contact.place(x=50,y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman", 15, "bold"),bg="white")
        email.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370,y=200,width=250)
        
        security_Q=Label(frame,text="Select Security Question",font=("times new roman", 15, "bold"),bg="white")
        security_Q.place(x=50,y=240)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"]=("Select","Your Favourite Sports", "Ypur Pet Name", "Your Birth Place")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        security_A=Label(frame,text="Security Answer",font=("times new roman", 15, "bold"),bg="white")
        security_A.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370,y=270,width=250)
        
        pswd=Label(frame,text="Password",font=("times new roman", 15, "bold"),bg="white")
        pswd.place(x=50,y=310)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman", 15, "bold"),bg="white")
        confirm_pswd.place(x=370,y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman", 15, "bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the Terms & Conditions", font=("times new roman", 12, "bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=390)


        
        img4=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Registerbtn.jpg")
        img4=img4.resize((200,50), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1_1= Button(frame, image=self.photoimg4,command=self.register_data,borderwidth=0,cursor="hand2", font=("times new roman", 15, "bold"))
        b1_1.place(x=45,y=440,width=200)
        
        img5=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Loginbtn.jpg")
        img5=img5.resize((200,45), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1_1= Button(frame, image=self.photoimg5, borderwidth=0,cursor="hand2", font=("times new roman", 15, "bold"))
        b1_1.place(x=375,y=440,width=200)




    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All Fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
                messagebox.showerror("Error","Please Agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Lm87#nhJ365#e8",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get()
                                                                                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registered Successfully")

            


class Face_Recognition_Attendance_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_Attendance_System")

        img=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Upper Image 1.jpg")
        img=img.resize((500,130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=6,y=0,width=500,height=130)

        img1=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Upper Image 2.jpg")
        img1=img1.resize((500,130), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=511,y=0,width=500,height=130)
        
        img2=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Upper Image 3.jpg")
        img2=img2.resize((500,130), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1016,y=0,width=500,height=130)

        img3=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Main Bg.jpg")
        img3=img3.resize((1530,710), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="Face_Recognition_Attendance_System", font=("times new roman", 35, "bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=0, width=1530, height= 45)


        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=("times new roman", 14, "bold"), background="white",foreground="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        

        img4=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Student Details.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1= Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        b1_1= Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2", font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        img5=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Face Recognition.jpg")
        img5=img5.resize((220,220), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1= Button(bg_img, image=self.photoimg5,cursor="hand2", command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        b1_1= Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        img6=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Attendance.jpg")
        img6=img6.resize((220,220), Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1= Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)
        b1_1= Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        img7=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Helpdesk.jpg")
        img7=img7.resize((220,220), Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1= Button(bg_img, image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)
        b1_1= Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data, font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        img8=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Train Data.jpg")
        img8=img8.resize((220,220), Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1= Button(bg_img, image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)
        b1_1= Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        img9=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Photos.jpg")
        img9=img9.resize((220,220), Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1= Button(bg_img, image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        b1_1= Button(bg_img,text="Photos",cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        img10=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Developer.jpg")
        img10=img10.resize((220,220), Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b1= Button(bg_img, image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)
        b1_1= Button(bg_img,text="Developer",command=self.developer_data, cursor="hand2", font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

        img11=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Exit.jpg")
        img11=img11.resize((220,220), Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b1= Button(bg_img, image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)
        b1_1= Button(bg_img,text="Exit",cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)



    def open_img(self):
        os.startfile("Data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return



    def student_details(self):
        self.new_windows=Toplevel(self.root)
        self.app=Student_Details(self.new_windows)


    def train_data(self):
        self.new_windows=Toplevel(self.root)
        self.app=Train_Data(self.new_windows)

    
    def face_data(self):
        self.new_windows=Toplevel(self.root)
        self.app=Face_Recognition(self.new_windows)

    
    def attendance_data(self):
        self.new_windows=Toplevel(self.root)
        self.app=Attendance(self.new_windows)

        
    def developer_data(self):
        self.new_windows=Toplevel(self.root)
        self.app=Developer(self.new_windows)
        
    def help_data(self):
        self.new_windows=Toplevel(self.root)
        self.app=Help(self.new_windows)



if __name__ == "__main__":
    main()
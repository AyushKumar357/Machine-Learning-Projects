from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_Attendance_System")


        title_lbl=Label(self.root,text="DEVELOPER", font=("times new roman", 35, "bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=0, width=1530, height= 45)


        img=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Dev.jpg")
        img=img.resize((1530,720), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=20,y=55,width=1530,height=720)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)
        
        img1=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\goku up.jpg")
        img1=img1.resize((200,200), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(main_frame,image=self.photoimg1)
        f_lbl.place(x=300,y=0,width=200,height=200)
        

        dev_label=Label(main_frame,text="Hello !! My Name is Ayush", font=("times new roman",18,"bold"),bg="white")
        dev_label.place(x=0,y=5)
        dev_label=Label(main_frame,text="ML Developer", font=("times new roman",18,"bold"),bg="white")
        dev_label.place(x=0,y=40)
        
        img2=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Dev2.jpg")
        img2=img2.resize((500,390), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=390)






if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
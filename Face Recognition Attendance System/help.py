from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_Attendance_System")


        title_lbl=Label(self.root,text="HELP DESK", font=("times new roman", 35, "bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=0, width=1530, height= 45)


        img=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Help.jpg")
        img=img.resize((1530,720), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=20,y=55,width=1530,height=720)

        dev_label=Label(f_lbl,text="Chaudhary@gmail.com", font=("times new roman",18,"bold"),bg="white")
        dev_label.place(x=550,y=250)





if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
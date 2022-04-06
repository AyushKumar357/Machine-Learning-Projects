from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train_Data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data Set")

        
        title_lbl=Label(self.root,text="TRAIN DATA SET", font=("times new roman", 35, "bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=0, width=1530, height= 45)


        img=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Top1U.jpg")
        img=img.resize((455,325), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=20,y=55,width=455,height=325)
        img1=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Top2U.jpg")
        img1=img1.resize((455,325), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=540,y=55,width=455,height=325)
        img2=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Top3U.jpg")
        img2=img2.resize((455,325), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1060,y=55,width=455,height=325)

        
        b1_1= Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2", font=("times new roman", 30, "bold"),bg="red", fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)
        
        img_bottom=Image.open(r"C:\Users\Ayush\OneDrive\Documents\Face Recognition Attendance System\Images\Photos.jpg")
        img_bottom=img_bottom.resize((1530,325), Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)



    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed !!")








if __name__ == "__main__":
    root=Tk()
    obj=Train_Data(root)
    root.mainloop()
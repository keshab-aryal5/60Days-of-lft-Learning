from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry("1500x800")
footer = Label(text="My text",font=("arial",10),bg="red",fg="white",padx=10,pady=10,borderwidth=3,relief=SUNKEN)
footer.pack(side="bottom",anchor="sw",fill=X)
img = Image.open("Photos/1 (1).jpg")
image1 = ImageTk(img)
first_pic = Label(photo=image1,width=30)
first_pic.pack()
root.mainloop()
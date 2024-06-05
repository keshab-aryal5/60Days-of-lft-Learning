from tkinter import *
from PIL import Image,ImageTk

root = Tk()
# root.config(width=444,height=234)

# root.geometry("644x434")

# root.minsize(444,234)

# root.maxsize(555,555)

# new_label = Label(text="I am in day 5 of lftlearning")


root.geometry("733x434")
pycharm_intro = Label(text="PyCharm Community Edition",font=("arial",22,"bold"))
pycharm_intro.pack()
root.padx = 50

button = Button(root,text="Stop",width=25,command=root.destroy)
button.pack()
 
self_image = PhotoImage(file="./Day4/Capture.PNG")
myimage = Label(image=self_image)

# myimage.pack()

my_label = Label(text="Keshab, a 22-year-old IT student in Kathmandu, Nepal, is a diligent and \ncurious individual with a passion for technology. Despite his academic efforts, \nhe feels uncertain about his future career path and is often anxious \nabout the rapidly changing tech landscape. However, his willingness to explore new \nopportunities and learn continuously sets a solid foundation for his future. With \nperseverance and adaptability, Keshab has the potential to thrive in various IT roles, \nwhether in software development, cybersecurity, or data science, ultimately finding a \nfulfilling career path that aligns with his evolving interests.",bg="red",fg="blue",font=('arial',22,"bold"),padx=50,pady=50 )
my_label.pack()
root.mainloop()
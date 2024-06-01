from tkinter import *
window = Tk()
window.minsize(width=400,height=200)
window.title("Mile to Km Converter")


def calculate():
    miles = int(text_input.get())
    km = miles*1.6
    ans_label.config(text=km)


miles_label = Label(text="Miles",font=("Arial",20,"normal"))
miles_label.grid(column=3,row=2)

km_label = Label(text="Km",font=("Arial",20,"normal"))
km_label.grid(column=3,row=3)

is_equal_to_label = Label(text="is equal to",font=("Arial",20,"normal"))
is_equal_to_label.grid(columns=1,row=3)

button = Button(text="Calculate",font=("Arial",15,"normal"),command=calculate)
button.grid(column=2,row=4)

text_input = Entry(width=20)
text_input.focus()
text_input.insert(END,string="0")
text_input.grid(column=2,row=2)

ans_label = Label(text="0",font=("Arial",20,"normal"))
ans_label.grid(column=2,row=3)


window.mainloop()
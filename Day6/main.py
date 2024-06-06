from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.geometry("744x433")
root.title("Mytitle")

# Important label options:
# text = adds the text
# bg/bd = background
# fg = foreground
# font = sets the font
# padx = x padding
# pady = y padding
# relief = border styling sunken,raised,groove,ridge
title_label = Label(text="Lorem ipsum dolor sit amet consectetur adipisicing elit.\n Incidunt placeat nobis assumenda dicta perferendis. Cum, alias. \nQuia in voluptatum alias quas, dolor nam soluta magnam. Fugiat alias nostrum possimus \npraesentium perspiciatis ullam molestias modi exercitationem dolorum.\n Quis aperiam neque expedita vero dolorum unde, nisi minima ullam rem\n recusandae. Reiciendis a maxime optio exercitationem ad?\n Deserunt, ea quia. Doloremque quos culpa neque officiis cumque maxime\n repellendus vel quisquam voluptatum nostrum? Nulla veniam perferendis\n at illum ducimus non architecto eos, accusantium obcaecati\n fugit ab laborum voluptates minima deserunt modi \nlaboriosam in voluptatum, facere vel! Dolorem officia mollitia \ndeleniti alias architecto maiores nemo cupiditate magni.\n Porro esse eaque voluptatibus aliquid",
                    bg="red",
                    foreground="white",
                    padx = 23,
                    pady = 44,
                    font = ("comicsans",9,"normal"),
                    borderwidth=3,
                    relief = SUNKEN
                    )

# Important pack options:
# Anchor = nw
# side = top,bottom,left,right
# fill = 
title_label.pack(side="bottom",anchor="sw",fill="x")
root.mainloop()
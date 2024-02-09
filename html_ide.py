from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.minsize(650, 650)
root.maxsize(650, 650)
root.configure(background = "orange")

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

label = Label(root, text = "File Name")
label.place(relx= 0.28, rely= 0.03, anchor= CENTER)

input_box = Entry(root)
input_box.place(relx= 0.46, rely= 0.03, anchor= CENTER)

my_text = Text(root, height = 35, width = 80, bg= "blue", fg= "white")
my_text.place(relx= 0.5, rely= 0.55, anchor= CENTER,)

root.mainloop()
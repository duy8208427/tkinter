from tkinter import *

root = Tk()

photo = PhotoImage(file="Hinh_moi.PNG")
label = Label(root, image=photo)
label.pack()

root.mainloop()
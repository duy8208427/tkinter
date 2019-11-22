from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title", "Monkeys can live up to 300 years.")

answer = tkinter.messagebox.askquestion("Question 1", "Do you like dog?")

if answer == "yes":
	print("Me too")
else:
	print ("I don't like you")

root.mainloop()
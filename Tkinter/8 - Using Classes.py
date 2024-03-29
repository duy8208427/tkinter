from tkinter import *

class BuckysButton:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		
		self.printButton = Button(frame, text="Print Message", command=self.printMessage)
		self.printButton.pack(side=LEFT)
		
		self.quitButton = Button(frame, text="Quit", command=frame.quit)
		self.quitButton.pack(side=LEFT)
		
	def printMessage(self):
		print("Nice to meet you!")
		
root = Tk()
b = BuckysButton(root)
root.mainloop()

from tkinter import *

def greating():
	msg = Label(windows, text = "Hello " + entry_box.get())
	windows["bg"] = 'grey'
	windows["bg"] = 'yellow'
	# msg ["bg"] = "grey"
	# msg ["fg"] = "yellow"
	msg.pack()

windows = Tk()
windows.title("Greating")

entry_box = Entry(windows)
entry_box.pack() 
button = Button(text = "Click here", command = greating)
button.pack()

windows.mainloop()
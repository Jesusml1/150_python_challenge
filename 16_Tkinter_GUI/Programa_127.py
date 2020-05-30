from tkinter import *


def add_to_list():
	toAdd = name_entry.get()
	list_box.insert(END, toAdd)
	name_entry.delete(0, END)
	
def reset_list():
	list_box.delete(0, END)
	name_entry.delete(0, END)


windows = Tk()
windows.title("List")

name_entry = Entry(windows)
name_entry.grid(row = 0, column = 0, columnspan = 2)

submit_button = Button(text = "Add to list", command = add_to_list)
submit_button.grid(row = 1, column = 0)

list_box = Listbox(windows)
list_box.grid(row = 3, column = 0, columnspan = 2)

reset_button = Button(text = "Reset list", command = reset_list)
reset_button.grid(row = 1, column = 1)

windows.mainloop()
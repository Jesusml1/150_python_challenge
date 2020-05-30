from tkinter import *
import csv

def add_to_list():
	toAdd = name_entry.get()
	if toAdd.isdigit() == True:
		list_box.insert(END, toAdd)
	name_entry.delete(0, END)
	
def reset_list():
	list_box.delete(0, END)
	name_entry.delete(0, END)

def export_list():
	numbersToExport = list_box.get(0, END)
	
	with open("Number_list.csv", "w") as file:
		# writer = csv.writer(file)
		# writer.writerows(numbersToExport)
		for item in numbersToExport:
			file.write(item + "\n")


windows = Tk()
windows.title("List")

name_entry = Entry(windows)
name_entry.grid(row = 0, column = 0, pady = 10, padx = 10)

submit_button = Button(text = "Add to list", command = add_to_list)
submit_button.grid(row = 0, column = 1, pady = 10, padx = 10)

list_box = Listbox(windows)
list_box.grid(row = 1, column = 0)

reset_button = Button(text = "Reset list", command = reset_list)
reset_button.grid(row = 2, column = 0, pady = 10, padx = 10)

export_button = Button(text = "Export to csv", command = export_list)
export_button.grid(row = 2, column = 1, pady = 10, padx = 10)

windows.mainloop()
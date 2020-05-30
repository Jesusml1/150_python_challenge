from tkinter import *
import tkinter as tk

import csv

def submit():
	
	file_name = file_entry.get()
	name = name_entry.get()
	age =  age_entry.get()

	with open(file_name + ".csv", "a") as file:
		file.write(name + " " + age + "\n")

	name_entry.delete(0, END)
	age_entry.delete(0, END)

def display():

	file_name = file_entry.get()
	imported_list = [] 
	
	with open(file_name + ".csv", "r") as file:
		reader = csv.reader(file)
		for item in reader:
			imported_list.append(item)
	
	for item in imported_list:
		list_display.insert(END, "".join(item))

def clear():

	list_display.delete(0,END)

windows = Tk()
windows.tk.call('wm', 'iconphoto', windows._w, tk.PhotoImage(file='icon.ico'))
windows.title("Create/add to CSV file")


file_label = Label(windows, text = "CSV file name: " )
file_label.grid(row = 0, column = 0, pady = 10, padx = 10)
file_entry = Entry(windows)
file_entry.grid(row = 0, column = 1, pady = 10, padx = 10)

name_label = Label(windows, text = "Name:")
name_label.grid(row = 1, column = 0, pady = 10, padx = 10)
name_entry = Entry(windows)
name_entry.grid(row = 1, column = 1, pady = 10, padx = 10)

age_label = Label(windows, text = "Age:")
age_label.grid(row = 2, column = 0, pady = 10, padx = 10)
age_entry = Entry(windows)
age_entry.grid(row = 2, column = 1, pady = 10, padx = 10)

submit_button = Button(text = "Create/add to CSV file", command = submit)
submit_button.grid(row = 3, column = 0, pady = 10, padx = 10, columnspan = 2)

display_button = Button(text = "Display CSV file", command = display)
display_button.grid(row = 4, column = 0, pady = 10, padx = 10, columnspan = 2)

list_display = Listbox(windows)
list_display.grid(row = 5, column = 0, pady = 20, padx = 10, columnspan = 2)

clear_button = Button(text = "Clear list", command = clear)
clear_button.grid(row = 6, column = 0, pady = 10, padx = 10, columnspan = 2)

windows.mainloop()
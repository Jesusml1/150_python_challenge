from tkinter import *

windows = Tk()
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
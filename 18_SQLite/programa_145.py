from tkinter import *
import sqlite3



conn = sqlite3.connect("TestScores.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS scores (
	Name text,
	grade integer)""")

conn.commit()
conn.close()


def add():
	
	name = name_entry.get()
	grade = grade_entry.get()

	conn = sqlite3.connect("TestScores.db")
	c = conn.cursor()

	c.execute("""INSERT INTO scores VALUES (?, ?)""", (name, grade))

	conn.commit()
	conn.close()

	name_entry.delete(0, END)
	grade_entry.delete(0, END)

def clear():
	
	name_entry.delete(0, END)
	grade_entry.delete(0, END)


windows = Tk()
windows.title("Test Score")

name_label = Label(windows, text = "Enter student's name:")
name_label.grid(column = 0, row = 0, padx = 10, pady = 10)

grade_label = Label(windows, text = "Enter student's grade:")
grade_label.grid(column = 0, row = 1, padx = 10, pady = 10)

name_entry = Entry(windows)
name_entry.grid(column = 1, row = 0, padx = 10, pady = 10, columnspan = 2)

grade_entry = Entry(windows)
grade_entry.grid(column = 1, row = 1, padx = 10, pady = 10, columnspan = 2)

add_button = Button(text = "Add", command = add)
add_button.grid(column = 1, row = 2, padx = 10, pady = 10)

clear_button = Button(text = "Clear", command = clear)
clear_button.grid(column = 2, row = 2, padx = 10, pady = 10)

windows.mainloop()
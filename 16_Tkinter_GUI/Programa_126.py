from tkinter import *


def add_to_counter():
	num = number_entry.get()
	num = int(num)
	ans = counter_display["text"]
	ans = int(ans)
	total = num + ans
	counter_display["text"] = total
	
	
def reset_counter():
	total = 0
	counter_display["text"] = 0
	number_entry.delete(0, END)

total = 0
num = 0

windows = Tk()
windows.geometry("300x200")
windows.title("~~~Counter~~~")

number_entry = Entry(windows)
number_entry.grid(row = 0, column = 0)

submit_button = Button(text = "Add number", command = add_to_counter)
submit_button.grid(row = 0, column = 1)

counter_display = Message(text = 0)
counter_display.grid(row = 1, column = 0)

reset_button = Button(text = "Reset", command = reset_counter)
reset_button.grid(row = 1, column = 1)

windows.mainloop()
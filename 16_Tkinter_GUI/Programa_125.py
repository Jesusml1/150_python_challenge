from tkinter import *
import random

def roll_dice():
	msg = Label(windows, text = str(random.randint(1, 6)))
	msg.pack()

windows = Tk()
windows.geometry("300x200")
windows.title("Dice")

button = Button(text = "Roll a dice", command = roll_dice)
button.pack()

windows.mainloop()
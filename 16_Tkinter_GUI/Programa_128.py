# DISTANCE CONVVERTER

from tkinter import *

def km_to_ml():
	numToConvert = km_entry.get()
	numToConvert = int(numToConvert)
	numConverted = numToConvert * 0.6214
	label_convertion_result["text"] = f"{numToConvert} Km = {round(numConverted, 3)} ml"
	km_entry.delete(0, END)
	
def ml_to_km():
	numToConvert = ml_entry.get()
	numToConvert = int(numToConvert)
	numConverted = numToConvert * 1.6093
	label_convertion_result["text"] = f"{numToConvert} ml = {round(numConverted, 3)} Km"
	ml_entry.delete(0, END)

def clear():
	label_convertion_result["text"] = ""

windows = Tk()
windows.title("Distance converter")

# KILOMETERS TO MILLES
label_km_to_ml = Label(windows, text = "Kilometer to mille:", justify = "left")
label_km_to_ml.grid(row = 0, column = 0, padx = 10, pady = 5)

km_entry = Entry(windows)
km_entry.grid(row = 1, column = 0, padx = 10)

km_submit_button = Button(text = "Convert", command = km_to_ml)
km_submit_button.grid(row = 1, column = 1, padx = 10)

# MILLES TO KILOMETER
label_ml_to_km = Label(windows, text = "Mille to killometer:", justify = "left")
label_ml_to_km.grid(row = 2, column = 0, padx = 10, pady = 5)

ml_entry = Entry(windows)
ml_entry.grid(row = 3, column = 0, padx = 10)

ml_submit_button = Button(text = "Convert", command = ml_to_km)
ml_submit_button.grid(row = 3, column = 1, padx = 10)

# CONVERTION RESULT
label_convertion_result = Label(windows)
label_convertion_result.grid(row = 4, column = 0, padx = 10)

# CLEAR BUTTON
clear_button = Button(text = "Clear", command = clear)
clear_button.grid(row = 4, column = 1, pady = 10)

windows.mainloop()
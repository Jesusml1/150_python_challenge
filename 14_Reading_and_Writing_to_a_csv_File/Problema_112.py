import csv

with open("Books.csv", "r") as file:
	print(file.read())

with open("Books.csv", "a") as file:
	newrecord = str(input("Introduce a new book (Title, Author, Year):\n"))
	file.write(newrecord + "\n")

with open("Books.csv", "r") as file:
	# print(file.read())
	for row in file:
		print(row)
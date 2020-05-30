import csv

with open("Books.csv", "r") as file:
	print(file.read())

with open("Books.csv", "a") as file:
	selection = str(input("Want to add more? (y/n) ")).lower()
	if selection == "y":
		many = int(input("How many? "))
		added = 0
		while added < many:
			newrecord = str(input("Introduce a book (Title, Author, Year)\n"))
			file.write(newrecord + "\n")
			added += 1
	else:
		print("No changes done.\n")

author = str(input("Enter an author name: \n"))

with open("Books.csv", "r") as file:
	count = 0
	for row in file:
		if author in str(row):
			print(row)
			count += 1
	if count == 0:
		print("There is no books in this name.")

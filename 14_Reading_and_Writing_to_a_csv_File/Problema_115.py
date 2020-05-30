import csv

with open("Books.csv", "r") as file:
	reader = csv.reader(file)
	for line in enumerate(reader, start=1):
		print(str(line[0]) + ". " + str(line[1][0]))
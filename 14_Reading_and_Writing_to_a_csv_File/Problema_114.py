import csv

startYear = int(input("Enter a starting year: "))
endingYear = int(input("Enter an ending year: "))

founds = 0

with open("Books.csv", "r") as file:
	reader = csv.reader(file)
	for line in reader:
		year = int(line[2])
		if startYear < year < endingYear:
			print(line[0])
	founds += 1


if founds < 1: 
	print("\nNo books were found.\n")
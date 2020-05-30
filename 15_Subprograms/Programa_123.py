import csv

def menu_selection():
	goodChoice = False
	while goodChoice == False:
		print("1) Add to file")
		print("2) View all records")
		print("3) Delete record")
		print("4) Quit program")
		menuChoice = int(input("Enter the number of your selection: "))
		if menuChoice < 1 or menuChoice > 4:
			print("Invalid option")
		else:
			goodChoice = True
	return menuChoice

def add_to_file():
	toAdd = []
	name = input("Enter name: ")
	salary = input ("Enter salary: ")
	toAdd.append(name)
	toAdd.append(salary)
	with open("Salaries.csv", "a") as file:
		writer = csv.writer(file, delimiter="	")	
		writer.writerow(item for item in toAdd)

def viewer():
	with open("Salaries.csv", "r") as file:
		reader = csv.reader(file, delimiter="	")
		for row in reader:
			print('	'.join(row))


def delete_record():
	records = []
	with open("Salaries.csv", "r") as file:
		reader = csv.reader(file, delimiter="	")
		for row in reader:
			records.append(row)
	for index, element in enumerate(records):
		print(index, element[0], element[1])
	toDelete = int(input("Enter the record index to delete: "))
	del records[toDelete]

	with open("Salaries.csv", "w") as file:
		writer = csv.writer(file, delimiter=" ")
		writer.writerows(records)
		



def main():
	end = False
	while end == False:
		try:
			choice = menu_selection()
			if choice == 1:
				add_to_file()
			elif choice == 2:
				viewer()
			elif choice == 3:
				delete_record()
			else: 
				end = True
		except ValueError:
			print("Input Error. Try again!\n")

main()
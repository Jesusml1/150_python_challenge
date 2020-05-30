# NAME LIST PROGRAM 

import csv

def menu():
	goodChoice = False
	while goodChoice == False:
		print("\n## NAME LIST ##\n")
		print("1) REVIEW list")
		print("2) ADD name to the list")
		print("3) CHANGE name in the list")
		print("4) DELETE name from the list")
		print("5) EXPORT list to csv")
		print("6) EXIT\n")
		menuSelection = int(input("Enter a menu option..."))
		if menuSelection < 1 or menuSelection > 6:
			print("\nInavlid option!")
		else:
			goodChoice = True
	return menuSelection

def review_names(nameList):
	for index, name in enumerate(nameList, start=1):
		print(f"{index}. {name}")

def add_name(nameList):
	toAdd = input("Introduce a name: ")
	nameList.append(toAdd)
	for index, name in enumerate(nameList, start=1):
		print(f"{index}. {name}")

def change_name(nameList):
	nameNumber = int(input("Introduce the number of the name to change: "))
	nameList[nameNumber - 1] = input("Introduce the name to replace: ")
	for index, name in enumerate(nameList, start=1):
		print(f"{index}. {name}")

def delete_name(nameList):
	nameNumber = int(input("Introduce the number of the name to delete: "))
	del nameList[nameNumber - 1]
	for index, name in enumerate(nameList, start=1):
		print(f"{index}. {name}")

def export_names(nameList):
	with open("ListName.csv", "w") as file:
		for i in nameList:
			file.write(i + "\n")
	print("Name list exported")

def main():
	names = []
	end = False
	while end == False:
		try:
			choice = menu()
			if choice == 1:
				review_names(names)
			elif choice == 2:
				add_name(names)
			elif choice == 3:
				change_name(names)
			elif choice == 4:
				delete_name(names)
			elif choice == 5:
				export_names(names)
			else: 
				end = True
		except ValueError:
			print("Input Error. Try again!\n")

main()
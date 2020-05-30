import re
import csv

with open("database.csv", 'r') as file:
	pass

def menu():
	
	good_choice = False
	while good_choice == False:
		print("")
		print("--------PASSWORD MANAGER---------")
		print("")
		print("1) Create a new User ID")
		print("2) Change a password")
		print("3) Display all User IDs")
		print("4) Quit")
		print("")
		menu_choice = int(input("Enter the number of your selection: "))
		if menu_choice < 1 or menu_choice > 4:
			print("\nInvalid option!")
		else:
			good_choice = True
	return menu_choice


def create_user():

	valid_user = False
	while valid_user == False:
		username = input("Enter a username: ")
		with open("database.csv", 'r') as file:
			if username in file.read():
				print("The username it is already in use.")
			else:
				valid_user = True

	valid_password = False
	while valid_password == False:
		password_strength = 0
		password = input("Enter a valid password: ")
		if len(password) >= 8:
			password_strength += 1
		if re.search('[A-Z]', password) != None:
			password_strength += 1
		if re.search('[a-z]', password) != None:
			password_strength += 1
		if re.search('[0-9]', password) != None:
			password_strength += 1
		if re.search('[\!\£\$\%\&\<\*\@]', password) != None:
			password_strength += 1
		
		if password_strength <= 2:
			print("Invalid password. Too weak.")
		elif password_strength <= 4:
			print("This password could be improved.")
			second = input("Want to try again? (y/n) ")
			if second == "n":
				valid_password = True
		elif password_strength == 5:
			print("This password is strong!")
			print("\nUser registration was successfully done.")
			print("Press enter to return the menu.")
			to_end = input("...")
			valid_password = True

	to_add = []
	to_add.append(username)
	to_add.append(password)

	with open("database.csv", "a") as file:
		# file.write(to_add[0] + to_add[1])
		writer = csv.writer(file, delimiter='-')
		writer.writerow(to_add)


def change_password():

	updated_list = []
	with open("database.csv", "r") as file:
		reader = csv.reader(file)
		for row in reader:
			updated_list.append(row[0].split("-"))

	username = input("Enter the username: ")
	checked = False
	index = 0
	for item in updated_list:
		if username in item[0]:
			checked = True
			index = updated_list.index(item)
			
	if checked == True:
		valid_password = False
		while valid_password == False:
			password_strength = 0
			password = input("Enter a valid password: ")
			if len(password) >= 8:
				password_strength += 1
			if re.search('[A-Z]', password) != None:
				password_strength += 1
			if re.search('[a-z]', password) != None:
				password_strength += 1
			if re.search('[0-9]', password) != None:
				password_strength += 1
			if re.search('[\!\£\$\%\&\<\*\@]', password) != None:
				password_strength += 1
			
			if password_strength <= 2:
				print("Invalid password. Too weak.")
			elif password_strength <= 4:
				print("This password could be improved.")
				second = input("Want to try again? (y/n) ")
				if second == "n":
					valid_password = True
			elif password_strength == 5:
				print("This password is strong!")
				valid_password = True

		# print(index)
		del updated_list[index][1]
		updated_list[index].append(password)
		
		with open("database.csv", "w") as file:
			writer = csv.writer(file, delimiter="-")
			for row in updated_list:
				writer.writerow(row)

		print("\nPassword was successfully changed.")
		print("Press enter to return the menu.")
		to_end = input("...")


	else:
		print("\nThe username introduced doesn't exist.")
		to_exit = input("Press enter to return the menu.\n...")
	

def display_users():
	
	print("")
	to_display = []
	with open("database.csv", "r") as file:
		reader = csv.reader(file)
		for row in reader:
			to_display.append(row[0].split("-"))

	for index,item in enumerate(to_display, start=1):
		print(f'{index}. {item[0]}')
		
	print("\nPress enter to return the menu.")
	to_end = input("...")


def main():

	end = False
	while end == False:
		try:
			choice = menu()
			if choice == 1:
				create_user()
			elif choice == 2:
				change_password()
			elif choice == 3:
				display_users()
			elif choice == 4:
				end = True
		except ValueError:
			print("Input Error. Try again!\n")

main()
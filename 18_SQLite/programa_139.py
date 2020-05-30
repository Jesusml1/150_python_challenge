import sqlite3

# conection = sqlite3.Connection("dataBase_1")
# cursor = conection.cursor()

# parameters_1 = (1, 'Simon', 'Hollews', 123456789)
# parameters_2 = (2, 'calolina', 'Felipe', 12356789)
# parameters_3 = (3, 'Darren', 'Smith', 1234547789)
# parameters_4 = (4, 'Mark', 'Smith', 1226386789)
# parameters_5 = (4, 'John', 'Doe', 755256789)

# cursor.execute("""CREATE TABLE contactData  (
# 	ID integer,
# 	NAME text,
# 	SURNAME text,
# 	PHONE integer)""")


# cursor.execute("""INSERT INTO contactData VALUES (?, ?, ?, ?)""", parameters_1)
# cursor.execute("""INSERT INTO contactData VALUES (?, ?, ?, ?)""", parameters_2)
# cursor.execute("""INSERT INTO contactData VALUES (?, ?, ?, ?)""", parameters_3)
# cursor.execute("""INSERT INTO contactData VALUES (?, ?, ?, ?)""", parameters_4)
# cursor.execute("""INSERT INTO contactData VALUES (?, ?, ?, ?)""", parameters_5)

# conection.commit()

# conection.close()

def menu():
	goodChoice = False
	while goodChoice == False:
		print("\nMAIN MENU\n")
		print("1) View phone book")
		print("2) Add to phone book")
		print("3) Search for surname")
		print("4) Delete person from the surname")
		print("5) Exit")
		menuSelection = int(input("\nEnter a menu option..."))
		if menuSelection < 1 or menuSelection > 5:
			print("\nInavlid option!")
		else:
			goodChoice = True
	return menuSelection

def view_phone_book():

	cursor.execute("SELECT * FROM dataBase_1")
	for i in cursor.fetchall():
		print(i)

	

def add_to_book():
	
	newid = int(input("Enter ID: "))
	newfname = input("Enter first name: ")
	newsname = input("Enter surname: ")
	newpnum = int(input("Enter phone number: "))
	
	cursor.execute("""INSERT INTO NAME 
		(ID, NAME, SURNAME, PHONE) VALUES (?, ?, ?, ?)""", 
		(newid, newfname, newsname, newpnum))

	conection.commit()

def search_for_surname():

	selectsurname = input("Enter a surname")
	cursor.execute("""SELECT * FROM NAME WHERE ID = ?""",
		[selectsurname])
	for i in cursor.fetchall():
		print(i)


def delete_person():
	selectid = int(input("Enter ID: "))
	cursor.execute("DELETE FROM NAME WHERE ID = ?",[selectid])
	cursor.execute("SELECT * FROM NAME")
	for i in cursor.fetchall():
		print(i)
	conection.commit()


with sqlite3.connect("dataBase_1") as conection:
	cursor = conection.cursor()


def main():
	end = False
	while end == False:
		try:
			choice = menu()
			if choice == 1:
				view_phone_book()
			elif choice == 2:
				add_to_book()
			elif choice == 3:
				search_for_surname()
			elif choice == 4:
				delete_person()
			else: 
				end = True
		except ValueError:
			print("Input Error. Try again!\n")


main()
conection.close()
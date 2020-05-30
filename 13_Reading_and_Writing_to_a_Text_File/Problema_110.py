file = open("Names.txt", "r")
print(file.read())

file = open("Names.txt", "r")
Name = str(input("Write a name from the list: "))
Name = Name + "\n"
for row in file:
	if row != Name:
		file = open("Name2.txt","a")
		file.write(row)
		file.close()
file.close()

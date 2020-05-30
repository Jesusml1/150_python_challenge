print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")
selection = int(input("Make a selection 1, 2 or 3: "))


if selection == 1:
	file = open("Subject.txt", "w")
	file.write(str(input("\nIntroduce a school subject: ")))
	file.close()
elif selection == 2:
	file = open("Subject.txt", "r")
	print("\n" + file.read() + "\n")
	file.close()
elif selection == 3:
	file = open("Subject.txt", "a")
	file.write("\n" + str(input("\nAdd a school subject: ")))
	file.close()
	file = open("Subject.txt", "r")
	print("\n" + file.read() + "\n")
	file.close()
else:
	print("The selection is not valid, run the programm again.")
file = open("Names.txt", "a")
file.write("\n" + str(input("Add a name to the list: ")))
file.close()

file = open("Names.txt", "r")
print(file.read())
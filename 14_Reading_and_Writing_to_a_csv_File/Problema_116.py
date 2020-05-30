import csv

# PARA GUARDAR LOS DATOS EN UNA LISTA, EN ESTE CASO, "bookList".
booksList = []
with open("Books.csv", "r") as file:
	reader = csv.reader(file)
	for index, line in enumerate(reader, start=1):
		print(index, line)
		booksList.append(line)
		
# PARA BORRAR UNA FILA DE LA LISTA
toRemove = int(input("Introduce the row number you want to remove: "))
del booksList[toRemove - 1]
for index, line in enumerate(booksList, start=1):
	print(index, line)
	
# PARA ELEGIR FILA A ALTERAR
rowToChange = int(input("Introduce the row number you want to alter: "))
bookToAlter = booksList[rowToChange - 1]
print(bookToAlter)

# PARA ALTERAR LOS DATOS DEL LIBRO
change = False
while change == False:
	dataToChange = int(input("What data you want to change?\n1) Title\n2) Author\n3) Year\n"))
	if dataToChange == 1:
		bookToAlter[0] = input("Introduce title: ")
		change = True
	elif dataToChange == 2:
		bookToAlter[1] = input("Introduce author: ")
		change = True
	elif dataToChange == 3:
		bookToAlter[2] = input("Introduce year: ")
		change = True
	else:
		print("Invalid option, try again.\n")

# PARA DEVOLVER LIBRO ALTERADO A LA LISTA
del booksList[rowToChange - 1]
booksList.append(bookToAlter)
print("List...")
for index, line in enumerate(booksList, start=1):
		print(index, line)

# PARA CONVERTIR LA LISTA EN UN ARCHIVO CSV

with open("Books.csv", "w") as file:
	writer = csv.writer(file)
	writer.writerows(booksList) #ESTA ES LA BUENA NOJODA
print("csv...")
with open("Books.csv", "r") as file:
	reader = csv.reader(file)
	for index, line in enumerate(reader, start=1):
		print(index, line)
print()

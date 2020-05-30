import sqlite3


conn = sqlite3.connect("Bookshop.db")
c = conn.cursor()

c.execute("""SELECT * FROM Authors""")
lista = c.fetchall()

print ("Authors and birthplaces\n")

for index, i in enumerate(lista, start=1):
	print(index, i[0] + ' - ' + i[1])

authorToSearch = input("\nEnter an author: ")

c.execute("""SELECT * FROM Books WHERE Books.Author = ?""", [authorToSearch])

lista = c.fetchall()

for i in lista:
	print(str(i[0]) + ' - ' + i[1] + ' - ' + i[2] + ' - ' + str(i[3]))


conn.close()

with open("textfile.txt", 'w') as file:
	for i in lista:
		file.write(str(i[0]) + ' - ' + i[1] + ' - ' + i[2] + ' - ' + str(i[3]) + "\n")

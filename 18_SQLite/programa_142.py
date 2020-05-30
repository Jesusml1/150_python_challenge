import sqlite3


conn = sqlite3.connect("Bookshop.db")
c = conn.cursor()

c.execute("""SELECT * FROM Authors""")
lista = c.fetchall()

print ("Authors and birthplaces\n")

for index, i in enumerate(lista, start=1):
	print(index, i[0] + ' - ' + i[1])

place = input("\nEnter a birplace: ")

c.execute("""SELECT Books.Title, Books.'Date Published', Books.Author FROM Authors,Books 
	WHERE Authors.Name=Books.Author AND Authors.Birthplace=?""", [place])

lista = c.fetchall()

for index, i in enumerate(lista, start=1):
	print(index, i[0] + ' - ' + i[1] + ' - ' + i[2])


conn.close()
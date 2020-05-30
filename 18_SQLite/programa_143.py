import sqlite3


conn = sqlite3.connect("Bookshop.db")
c = conn.cursor()



year = input("\nEnter a year to display the list: ")

c.execute("""SELECT Books.Title, Books.'Date Published', Books.Author FROM Books 
	WHERE Books.'Date Published' > ? ORDER BY Books.'Date Published'""", [year])

lista = c.fetchall()

for index, i in enumerate(lista, start=1):
	print(index, i[0] + ' - ' + i[1] + ' - ' + i[2])


conn.close()
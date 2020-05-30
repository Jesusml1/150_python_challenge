import sqlite3
from author import Author
from book import Book


conn = sqlite3.connect("Bookshop.db")
c = conn.cursor()

# c.execute("""CREATE TABLE Authors (
# 	Name text,
# 	Birthplace text)""")

# c.execute("""CREATE TABLE Books (
# 	ID integer primary key,
# 	Title text,
# 	Author text,
# 	'Date Published' text)""")

auth_1 = Author('Agatha Christie', 'Torquay')
auth_2 = Author('Cecelia Ahern', 'Dublin')
auth_3 = Author('J.K. Rowling', 'Bristol')
auth_4 = Author('Oscar Wilde', 'Dublin')

bk_1 = Book(1, 'De Proundis', 'Oscar Wilde', 1905)
bk_2 = Book(2, 'Harry Potter and the chamber of secrets', 'J.K. Rowling', 1905)
bk_3 = Book(3, 'Harry Potter and the prisoner of Azkaban', 'J.K. Rowling', 1999)
bk_4 = Book(4, 'Lyrebird', 'Cecelia Ahern', 2017)
bk_5 = Book(5, 'Murder on the Orient Express', 'Agatha Christie', 1934)
bk_6 = Book(6, 'Perfect', 'Cecelia Ahern', 2017)
bk_7 = Book(7, 'The marbel collector', 'Cecelia Ahern', 2016)
bk_8 = Book(8, 'The murder of the links', 'Agatha Christie', 1923)
bk_9 = Book(9, 'The picture of Dorian Grey', 'Oscar Wilde', 1890)
bk_10 = Book(10, 'The secret adversary', 'Agatha Christie', 1921)
bk_11 = Book(11, 'The seven dials mystery', 'Agatha Christie', 1929)
bk_12 = Book(12, 'The year I met you', 'Cecelia Ahern', 2014)




# c.execute("INSERT INTO Authors VALUES (:Name, :Birthplace)", {'Name': auth_1.name, 'Birthplace': auth_1.birthplace})
# c.execute("INSERT INTO Authors VALUES (:Name, :Birthplace)", {'Name': auth_2.name, 'Birthplace': auth_2.birthplace})
# c.execute("INSERT INTO Authors VALUES (:Name, :Birthplace)", {'Name': auth_3.name, 'Birthplace': auth_3.birthplace})
# c.execute("INSERT INTO Authors VALUES (:Name, :Birthplace)", {'Name': auth_4.name, 'Birthplace': auth_4.birthplace})


# c.execute("INSERT INTO Books VALUES (?, ?, ?, ?)", (bk_1.iden,  bk_1.title, bk_1.author, bk_1.date_published))
# c.execute("INSERT INTO Books VALUES (?, ?, ?, ?)", (bk_2.iden,  bk_2.title, bk_2.author, bk_2.date_published))
# c.execute("INSERT INTO Books VALUES (?, ?, ?, ?)", (bk_3.iden,  bk_3.title, bk_3.author, bk_3.date_published))
# c.execute("INSERT INTO Books VALUES (?, ?, ?, ?)", (bk_4.iden,  bk_4.title, bk_4.author, bk_4.date_published))
# c.execute("INSERT INTO Books VALUES (?, ?, ?, ?)", (bk_5.iden,  bk_5.title, bk_5.author, bk_5.date_published))
# c.execute("INSERT INTO Books VALUES (?, ?, ?, ?)", (bk_6.iden,  bk_6.title, bk_6.author, bk_6.date_published))
# c.execute("INSERT INTO Books VALUES (?, ?, ?, ?)", (bk_7.iden,  bk_7.title, bk_7.author, bk_7.date_published))
# c.execute("INSERT INTO Books VALUES (?, ?, ?, ?)", (bk_8.iden,  bk_8.title, bk_8.author, bk_8.date_published))
# c.execute("INSERT INTO Books VALUES (?, ?, ?, ?)", (bk_9.iden,  bk_9.title, bk_9.author, bk_9.date_published))
# c.execute("INSERT INTO Books VALUES (?, ?, ?, ?)", (bk_10.iden,  bk_10.title, bk_10.author, bk_10.date_published))
# c.execute("INSERT INTO Books VALUES (?, ?, ?, ?)", (bk_11.iden,  bk_11.title, bk_11.author, bk_11.date_published))
# c.execute("INSERT INTO Books VALUES (?, ?, ?, ?)", (bk_12.iden,  bk_12.title, bk_12.author, bk_12.date_published))



conn.commit()

conn.close()
tvShows = ["Bojack Horseman", "13 reason why", "The wire", "Game of Thrones"]
print()
for i in tvShows:
    print(i)
print()
newShow = str(input("Introduce a new show: "))
position = int(input("Introduce the index: "))

tvShows.insert(position, newShow)

print()
print("Here is the new list.")
for i in tvShows:
    print(i)
print()


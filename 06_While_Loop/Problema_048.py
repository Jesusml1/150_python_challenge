name = str(input("Who do you want to invite to the party?\n"))
print(name, "has been invited.")
count = 1
while str(input("Someone else? (y/n)")) == "y":
    name = str(input("Enter the name:\n"))
    print(name, "has been invited.")
    count = count + 1
print("You have invited", count, "people.")
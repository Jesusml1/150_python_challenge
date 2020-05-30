people = int(input("How many people do you want in the party?\n"))

if people < 10:
    for i in range(0, people):
        name = str(input("Enter a name: "))
        print(name, "has been invited")
else:
    print("Too many people")
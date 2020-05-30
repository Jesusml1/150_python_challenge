firstname = str(input("introduce your firstname: "))

if len(firstname) < 5:
    surname = str(input("Introduce your surname: "))
    name = firstname + surname
    print(name.upper())
else:
    print(firstname.lower())
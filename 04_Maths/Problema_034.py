selection = int(input("1) Square\n2) Triangle\n\nEnter a number: "))

if selection == 1:
    a = int(input("Enter the length side: "))
    print("The square area is: " + str(a ** 2))
elif selection == 2:
    b = int(input("Enter the base: "))
    c = int(input("Enter the height: "))
    print("The triangle area is: " + str((b * c) / 2))
else:
    print("Error, try again.")
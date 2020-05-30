num = int(input("introduce a number: "))
while num < 10 or num > 20:
    if num < 10:
        print("Too low, try again.")
    elif num > 20:
        print("Too high, try again.")
    num = int(input("introduce a number: "))
print("Thanks you!")
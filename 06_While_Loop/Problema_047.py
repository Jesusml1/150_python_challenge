num1 = int(input("Enter a number: "))
total = num1
while str(input("Do you want to add another number? (y/n) ")) == "y": 
    total = total + int(input("Enter another number: "))
print("Total is", total)
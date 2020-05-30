total = 0

for i in range(0, 5):
    num = int(input("Enter a number: "))
    ans = str(input("Want to add it? y/n "))
    if ans == "y":
        total = total + num

print("Total is:", total)
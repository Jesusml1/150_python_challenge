from array import array
import math

numbers = array('f', [52.45, 48.15, 74.69, 46.36, 48.12])
print(numbers)

check = False

while check == False:
    num = int(input("Enter a whole number between 2 and 5: "))
    if 2 < num < 5:
        for i in numbers:
            print(round(i / num, 2))
        check = True
    else:
        print("Off limits, try again.")
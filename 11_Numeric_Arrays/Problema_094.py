from array import array

numbers = array('i', [25,65,85,75,45])
check = False
print(numbers)
print()
while check == False:
    num = int(input("Choose a number within the array: "))
    if num in numbers:
        print("The index is:", numbers.index(num))
        check = True
    else:
        print("The number introduced it is not in the array, try again.")

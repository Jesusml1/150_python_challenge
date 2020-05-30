from array import array

numbersArray = array('i', [])

count = 0

for x in range(0, 5):
    while count < 5:
        toAdd = int(input("..."))
        if  10 < toAdd < 20:
            numbersArray.append(toAdd)
            count = count + 1
        else:
            print("Outside the range.") 

print("Thanks you! Here is the array.")

for i in numbersArray:
    print(i)
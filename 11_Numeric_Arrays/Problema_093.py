from array import array

numbers = array('i', [])
numbers2 = array('i', [])

while len(numbers) < 5:
    num = int(input("..."))
    numbers.append(num)

numbers = sorted(numbers)

print(numbers)

print("Pick one of the numbers in the array above: ")
toRemove = int(input("..."))
if toRemove in numbers:
    numbers.remove(toRemove)
    numbers2.append(toRemove)
    print(numbers, numbers2)
else:
    print("It is not in the array.")
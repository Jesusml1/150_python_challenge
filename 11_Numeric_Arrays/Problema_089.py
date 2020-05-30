from array import array
import random


numbers = array('i', [])

for x in range(0, 5):
    randomNumber = random.randint(1, 1000)
    numbers.append(randomNumber)

for i in numbers:
    print(i)

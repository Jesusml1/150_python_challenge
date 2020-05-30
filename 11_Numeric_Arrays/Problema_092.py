import random 
from array import array

numArray1 = array('i', [])
numArray2 = array('i', [])

for i in range(0, 5):
    randNum = random.randint(1, 1000)
    numArray1.append(randNum)

while len(numArray2) < 3:
    num = int(input("..."))
    numArray2.append(num)

totalArray = numArray1 + numArray2
sortArray = sorted(totalArray)

for i in sortArray:
    print(i)
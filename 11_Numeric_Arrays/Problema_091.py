from array import array
numArray = array('i', [45, 15, 45, 86, 64])
print(numArray)
numinput = int(input("Enter a number of the array: "))
print("The number apears", numArray.count(numinput), "times.")
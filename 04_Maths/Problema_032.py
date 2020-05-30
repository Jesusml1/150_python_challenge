import math
rad = int(input("Enter the radius: \n"))
depth = int(input("Enter the depth: \n"))
print("\nThe volume of the cilinder is: " + str(round(math.pi * pow(rad, 2) * depth, 3)))
import random
number = random.randint(1, 10)
while int(input("Pick a number: ")) != number:
    print("try again")
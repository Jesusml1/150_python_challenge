import random
number = random.randint(1, 10)
guess = 0
while guess != number:
    guess = int(input("Pick a number: "))
    if guess > number:
        print("Too high")
        print("try again")
    elif guess < number:
        print("Too low")
        print("try again")
    
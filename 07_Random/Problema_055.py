import random
number = random.randint(1,5)
guess = int(input("Pick a number between 1 and 5.\n"))
if guess == number:
    print("Well done!")
else:
    secondtry = int(input("Try again.\n"))
    if secondtry == number:
        print("You win!")
    else:
        print("You lose.")
#Color Guess game

import random
print("There are 5 colors:\n\nblue\nyellow\nred\norange\npurple\n")

color = random.choice(["blue","yellow","red","orange","purple"])
guessed = False
second = False

while guessed == False:
    guess = str(input("Guess which i like the most...\n"))
    if guess == color:
        print("Well Done!")
        guessed = True
    else:
        while second == False:
            print("\nThat's not it. Take a hint.\n")
            if color == "blue":
                print("I like to go to the sea often.\n")
            elif color == "yellow":
                print("I like the sunflowers so much.\n")
            elif color == "red":
                print("My favorite pizza toping is the sauce.\n")
            elif color == "orange":
                print("I like to drink orange juice in the morning.\n")
            elif color == "purple":
                print("Orquideas are really beautiful\n")
            guess = str(input("Guess which i like...\n"))
            if guess == color:
                print("Well Done!")
                second = True
                guessed = True
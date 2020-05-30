#Coin flip game

import random
coinside = random.choice(["h","t"])
choice = str(input("Heads or tails? (h/t)\n"))
if coinside == "h":
    print("You win.")
else:
    print("You lose.")
if coinside == "h":
    print("It was heads.")
else:
    print("It was tails.")
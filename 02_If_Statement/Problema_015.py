def checkColor(color):
    if color == "red":
        return "That is my favorite color too"
    else:
        return "I do not like " + color + ", i personally prefer red."

print("Which is your favorite color: \n")

color = input()
print(checkColor(color.lower()))
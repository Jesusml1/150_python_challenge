def checkIfBetween(num):
    if num >= 10 and num <= 20:
        return "Very good"
    else:
        return "Off limits, try again"


print("Enter a number between 10 and 20, please:\n")
num = int(input())
print(checkIfBetween(num))
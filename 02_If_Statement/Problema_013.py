print("Hi, please enter a number under 20")
num = int(input())

def checkNumber(num):
    if num >= 20 :
        return "Too high, try again!"
    else:
        return "Nice"

print(checkNumber(num))
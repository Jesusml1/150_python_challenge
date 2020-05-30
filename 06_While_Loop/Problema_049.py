compnum = 50
guess = 0
count = 0
while guess != compnum:
    guess = int(input("Guess the number: "))
    if guess > compnum:
        print ("To high")
    elif guess < compnum:
        print("Too low")
    count = count + 1
print("Well done, you took", count, "attempts.")
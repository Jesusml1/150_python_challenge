sel = str(input("Do you want to count up or down?\n"))

if sel == "up":
    top = int(input("Top number? "))
    for i in range(1, top + 1):
        print(i)
elif sel == "down":
    buttom = int(input("Gime a number below 20: "))
    for i in range(20, buttom - 1, -1):
        print(i)
else:
    print("I don't understand")
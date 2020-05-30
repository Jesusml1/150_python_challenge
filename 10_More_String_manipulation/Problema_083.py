text = ""
check = False

while check == False:
    text = str(input("Introduce the text: "))
    if text.isupper():
        print("In lowercase is better, try again.")
    else:
        print("Thank you!")
        check = True
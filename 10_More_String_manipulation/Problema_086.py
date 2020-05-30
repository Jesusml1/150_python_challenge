password = str(input("Introduce a new password: "))
confirmation = str(input("Introduce the new password again: "))

if password == confirmation:
    print("Thank you.")
elif password.lower() == confirmation.lower():
    print("There must be an error in casetype.")
else:
    print("The passwords don't match.")
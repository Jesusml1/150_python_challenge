invited_list = []

print("Enter three people you want to invited:")
for i in range(3):
    invited_list.insert(i, str(input("...")))

another = str(input("Do you want another in the list (y/n)? "))

while another == "y":
    invited_list.append(str(input("...")))
    another = str(input("Do you want another in the list (y/n)? "))

print()
print("Here are the people you invited:\n")

for i in invited_list:
    print(i)

print()

for_deleted = str(input("Do you want to check the list? If so, pick a name you want to delete\n"))

print("The index of the name choosed is", invited_list.index(for_deleted))
# indexToDelete = int(invited_list.index(for_deleted))
confirmation = str(input("Do you still want it on the party (y/n)? "))

if confirmation == "n":
    invited_list.remove(for_deleted)
    print()
    print("Here are the people you invited:\n")
    for i in invited_list:
        print(i)
    print()
else:
    print("OK, we are over here.")
    print()
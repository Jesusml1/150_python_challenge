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

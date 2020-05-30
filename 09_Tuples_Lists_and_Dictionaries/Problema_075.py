number_list = [100, 200, 300, 400]

for i in range(0, len(number_list)):
    print(number_list[i])

number_asked = int(input("Enter a 3-digits number: "))

if number_asked in number_list:
    print(number_list.index(number_asked))
else:
    print("That is not in the list.")
name = str(input("Introduce you name here: "))
name = name.lower()
vowels = 0

for letter in name:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowels = vowels + 1

print("The name introduced has", vowels, "vowels.")
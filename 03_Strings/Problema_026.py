word = str(input("Change into Pig Latin: "))

if word[0] == "a" or word[0] == "e" or word[0] == "i"or word[0] == "o"or word[0] == "u":
    pigLatin1 = word + "way"
    print(pigLatin1.lower())
else:
    fix = word.strip(word[0])
    pigLatin2 = fix + "".join(word[0]) + "ay"
    print(pigLatin2.lower())

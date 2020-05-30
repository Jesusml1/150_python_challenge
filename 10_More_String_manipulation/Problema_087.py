word = str(input("Type in a word: "))
#newword = word[::-1]
#for letter in newword:
#    print(letter)
length = len(word)
num = 1

for i in word:
    print(word[length - num])
    num = num + 1

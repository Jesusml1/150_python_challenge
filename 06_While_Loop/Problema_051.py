bottles = 10
count = 9
rest = 0
while bottles != 0:
    if bottles > 1:
        print("\nThere are", bottles, "green bottles hanging on the wall,\n" + str(bottles) + " green bottles hanging on the wall,\nand if 1 green bottle should accidentally fall,")
    else:
        print("\nThere is", bottles, "green bottle hanging on the wall,\n" + str(bottles) + " green bottle hanging on the wall,\nand if 1 green bottle should accidentally fall,")
    rest = int(input("how many green bottles will be hanging on the wall? "))
    if rest != count:
        print("\nTry again!")
    else:
        bottles = bottles - 1
        count = count - 1
print("\nThere are no more green bottles hanging on the wall.")
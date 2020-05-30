#Times tables - 1 to 12

num = int(input("Enter a number: "))
for i in range(0, 10):
    print(str(num) + "x" + str(i) + "=" + str(num * i))
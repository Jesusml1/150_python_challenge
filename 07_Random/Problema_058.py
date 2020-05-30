#Maths quiz
import random

question = 0 
ace = 0

print("Math test. Good luck!\n")

while question != 5:
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    ans = int(input(str(num1) + "+" + str(num2) + "="))
    question = question + 1
    if ans == num1 + num2:
        ace = ace + 1

print("\nEnd of the test, you score " + str(ace) + "/5.")
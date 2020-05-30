import csv
import random

q = 0 
ace = 0
questionsList = []
answersList = []
score = []

print("Math test")
name = input("Please, introduce you name: ")
print("Good luck!\n")

while q != 5:
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)

    ans = int(input(str(num1) + "+" + str(num2) + "=")) 
    q += 1
    if ans == num1 + num2:
    	ace += 1
    questionsList.append(str(num1) + "+" + str(num2))
    answersList.append(ans)


print("\nEnd of the test, you score " + str(ace) + "/5.")

score = str(ace) + "/5"
questions = ", ".join([str(elem) for elem in questionsList])
answers = ", ".join([str(elem) for elem in answersList])

test = []
test.append(name)
test.append(questions)
test.append(answers)
test.append(score)

print(test)


with open("MathTests.csv", "a") as file:
	writer = csv.writer(file, delimiter='\t')
	writer.writerow(str(elem) for elem in test)
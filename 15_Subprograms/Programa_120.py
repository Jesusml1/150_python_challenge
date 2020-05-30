import random

def menu_selection():
	print("1) Addition")
	print("2) Subtraction")
	rightChoice = False
	while rightChoice == False:
		menuChoice = int(input("Enter 1 or 2: "))
		if menuChoice != 1 and menuChoice != 2:
			print("Invalid option, try again.")
		else:
			rightChoice = True
	return menuChoice

def addition():
	num1 = random.randint(5, 20)
	num2 = random.randint(5, 20)
	correctAnswer = num1 + num2
	answer = int(input(f"{num1}+{num2}="))
	result = [correctAnswer, answer]
	return result

def subtraction():
	num1 = random.randint(25, 50)
	num2 = random.randint(1, 25)
	correctAnswer = num1 - num2
	answer = int(input(f"{num1}-{num2}="))
	result = [correctAnswer, answer]
	return result

def check(result):
	if result[0] == result[1]:
		print("Correct")
	else:
		print("Incorrect, the answer is",result[0])

def main():
	choice = menu_selection()
	if choice == 1:
		answers = addition()
	else:
		answers = subtraction()
	check(answers)

main()
import random

def pick_num():
	num1 = int(input("Introduce low limit: "))
	num2 = int(input("Introduce high limit: "))
	comp_num = random.randint(num1, num2)
	return comp_num


def first_guess():
	print("I am thinking of a number...")
	guess = int(input("Make a guess: "))
	return guess

def comparator(comp_num, guess):
	end = False
	while end == False:
		if comp_num == guess:
			print("Correct,you win.")
			end = True
		elif comp_num > guess:
			guess = int(input("Too low\n"))
		else:
			guess = int(input("Too high\n"))


def main():
	comp_num = pick_num()
	guess = first_guess()
	comparator(comp_num, guess)

main()



		
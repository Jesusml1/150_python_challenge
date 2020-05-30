def ask_number():
	num = int(input("Enter a number: "))
	return num

def count_to_num():
	for i in range(1, ask_number() + 1):
		print(i)

def main():
	count_to_num()

main()
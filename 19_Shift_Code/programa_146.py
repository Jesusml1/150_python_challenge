def menu_seection():
	goodChoice = False
	while goodChoice == False:
		print("1) Make a code")
		print("2) Decode a message")
		print("3) Quit")
		menuChoice = int(input("\nEnter the number of your selection: "))
		if menuChoice < 1 or menuChoice > 3:
			print("Invalid option")
		else:
			goodChoice = True
	return menuChoice


def coded():

	message = input("Enter message: ")
	key = int(input("Enter key number: "))
	
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
				'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
				'y', 'z', ' ']
	
	# alphabet = {1: 'a', 2: 'b',3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h',
	# 			9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p',
	# 			 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x',
	# 			  25: 'y', 26: 'z', 27: ' '}
	

	message = message.lower()
	charlist = list(message)

	def dephase():
		for i in charlist:
			poos = []
			pos[].append(alphabet.index(i))
			 
		return pos[]
		

	print(map(dephase(), charlist))	


		 

	



	



	







def decoded():
	message = input("Enter message: ")
	key = int(input("Enter key number: "))

def main():
	pass



import random

colors = {1: "blue", 2: "yellow", 3: "red", 4: "green", 5: "orange",
			6:"purple", 7:"grey", 8:"black", 9:"white", 10: "brown",
				11: "pink", 12: "clay", 13: "violet", 14: "beige", 15:"silver"}


random_colors = []

for i in range(0, 4):
	key = random.randint(1, 15)
	random_colors.append(colors[key])

# print(f"Estos son los colores random: {random_colors[0]}, {random_colors[1]}, {random_colors[2]}, {random_colors[3]}.")


endgame = False
guesses = 0

while endgame == False:
	print("Choose four colors:\n")
	for i in colors:
		print(colors[i])

	colors_picked = []
	for i in range(0, 4):
		add = input("\nIntroduce a color and press enter: ")
		colors_picked.append(add)

	guesses += 1
	print(colors_picked)
	# TO CHECK CORRECT COLOR IN THE CORRECT PLACE
	correct = 0
	for i in range(0, 4):
		if random_colors[i] == colors_picked[i]:
			correct += 1

	# TO CHECK IF COLOR EXIST
	existent = 0
	for i in range(0, 4):
		if colors_picked[i] in random_colors:
			existent += 1


	print(f"Correct colors in the correct position: {correct}")
	print(f"Correct colors but in the wrong position: {existent}")

	if correct == 4:
		endgame = True
		print(f"Number of guesses you tried: {guesses}")
	else: 
		print("Give another try!")
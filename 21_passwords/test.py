import csv


updated_list = []
with open("database.csv", "r") as file:
	reader = csv.reader(file)
	for row in reader:
		updated_list.append(row[0].split("-"))

print(updated_list)

# username = input("Enter the username: ")
# with open("database.csv", 'r') as file:
# 		reader = csv.reader(file, delimiter="-")
# 		for row in reader:
# 			if username in row:
# 				checked = True
# 				print(row)
# 			else:
# 				print("The username doesn't exist.")
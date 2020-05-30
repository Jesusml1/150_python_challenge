table = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
print(table)

row = int(input("Select a row: "))
print(table[row])

column = int(input("Select a column: "))
print(table[row][column])
to_change = str(input("Do you want to change the value? (y/n) "))
if to_change == "y":
	new_value = int(input("Enter a new value: "))
	table[row][column] = new_value
	print(table[row])
else:
	print(table[row])
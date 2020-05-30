table = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
print(table)

row = int(input("Select a row: "))

print(table[row])

newToRow = int(input("Enter a new value in the row: "))

table[row].append(newToRow)

print(table[row])
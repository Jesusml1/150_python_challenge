dic = {
"John": {"N":3056, "S":8463, "E":8441, "W":2694},
"Tom":  {"N":4832, "S":6786, "E":4737, "W":3612},
"Anne": {"N":5239, "S":4802, "E":5820, "W":1859},
"Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}
	}

for i in dic:
	print(i, dic[i])

name   = str(input("Introduce the name you want to check: "))
region = str(input("Introduce the region (N/S/E/W) "))

print(dic[name][region])
to_change = str(input("Do you want to change the value? (y/n)"))

if to_change == "y":
	new_value = int(input("Enter a new value: "))
	dic[name][region] = new_value
	print(dic[name])
else:
	print(dic[name])
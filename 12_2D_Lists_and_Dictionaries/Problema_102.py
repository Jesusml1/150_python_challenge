set_list = {}

for i in range(4):
	name = str(input("Insert name: "))
	age = int(input("Insert age: "))
	size = int(input("Insert shoe size: "))
	set_list[name] = {"Age":age, "Shoe size": size}
	print()

ask = str(input("Introduce a name: "))
print(set_list[ask])

set_list = {}

for i in range(4):
	name = str(input("Insert name: "))
	age = int(input("Insert age: "))
	size = int(input("Insert shoe size: "))
	set_list[name] = {"Age":age, "Shoe size": size}
	print()


for j in set_list:
	print(j, set_list[j]["Age"])


getRid = str(input("Insert a name to delete "))
print()
del set_list[getRid]

for j in set_list:
	print(j, set_list[j]["Age"])

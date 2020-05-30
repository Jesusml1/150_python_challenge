fav_food = {1:"first", 2:"second",3:"third",4:"fourth"}
for i in range(1, 5):
    fav_food[i] = str(input("Enter your " + str(i) + "th favorite food: "))
print(fav_food)
toDelete = int(input("Which number do you want to delete: "))
del fav_food[toDelete]
print(sorted(fav_food.values()))
print(fav_food)
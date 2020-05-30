countries = ("Germany", "England","France","US","China")

print(countries)

country = str(input("Choose one of the countries above: "))
print("The position of the country introduced is:", countries.index(country))

number = int(input("Introduce the index of one country: "))
print("Country index:",countries[number])
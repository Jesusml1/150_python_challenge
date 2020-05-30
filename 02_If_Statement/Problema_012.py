print("Hey, dame un numero.")
num1 = input()
print("Muy bien, ahora dame otro.")
num2 = input()

def OrdenaNumeros(num1, num2):
    if num1 > num2:
        return "\n" + num2 + "\n" + num1
    else:
        return "\n" + num1 + "\n" + num2

print("Mira, te los he ordenado:\n" , OrdenaNumeros(num1, num2))
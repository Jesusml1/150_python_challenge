def CompruebaLluvia(respuesta_1):
    if respuesta_1 == "si":
        return True
    elif respuesta_1 == "no":
        return False

def CompruebaViento(respeusta_2):
    if respuesta_2 == "si":
        return True
    elif respuesta_2 == "no":
        return False


respuesta_1 = str(input("Esta lloviendo afuera? "))
if CompruebaLluvia(respuesta_1.lower()) == True:
    respuesta_2 = str(input("Esta fuerte el viento? "))
    if CompruebaViento(respuesta_2.lower()) == True:
        print("Hace mucho viento para salir, el paraguas no te servira.")
    elif CompruebaViento(respuesta_2.lower()) == False:
        print("Toma una sombrilla.")
elif CompruebaLluvia(respuesta_1.lower()) == False:
    print("Disfruta tu dia.")



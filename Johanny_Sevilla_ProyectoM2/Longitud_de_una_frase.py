"""
Crear un programa para identificar la longitud de una palabra ingresada. La palabra correcta debe tener entre cuatro
y ocho letras. toma en cuenta las siguientes consideraciones:

Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, se debe imprimir un mensaje que indique
que la palabra es correcta

Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: Hacen falta letras. Solo tiene N letras
(siendo N el número de letras de la palabra)

Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: Sobran letras. Tiene N letras
((siendo N el número de letras de la palabra))
"""

# Se solicita al usuario una palabra.
palabra = input("Ingresa una palabra: ")

# Se evalua si la palabra tiene una longitud entre 4 y 8.
if 4 <= len(palabra) <= 8:
    print(f"La Palabra {palabra} es Correcta")
# Se evalua si la palabra tiene una longitud menor a 4.
elif len(palabra) < 4:
    print(f"Hacen falta letras. Solo tiene {len(palabra)} letras")
# Se ejecuta esta accion en el caso de que no se cumplan las condiciones anteriores
else:
    print(f"Sobran letras. Tiene {len(palabra)} letras")

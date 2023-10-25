"""
Autor: Johanny Alexix sevilla Ortega
Fecha: 25/10/2023
GitHub General: https://github.com/lonelyday01
Link del Repo: https://github.com/lonelyday01/UCAM_Python_Bootcam
"""
"""
Crear un programa que pida al usuario su nombre, apellido paterno, apellido materno, edad, peso y estatura, desplegarlos
en pantalla junto con su Índice de Masa Corporal (IMC).

El programa no puede permitir que ningún dato quede vacío, además de asegurarse de que en los campos de edad, peso 
y estatura el usuario introduzca una cifra. Todo esto antes de proceder con el cálculo del IMC siguiendo la fórmula:

Peso / estatura2   -> Peso sobre estatura al cuadrado

"""

# Bucle infinito para repetir el codigo cuando algun dato se ingrese vacio.
while True:
    # Creamos un Try para intentar hacer los casteos y captura de datos.
    try:
        nombre_completo = input("Ingresa nombre tu nombre completo: ")
        edad = int(input("Ingresa tu edad: "))
        peso = float(input("Ingresa tu peso: "))
        estatura = float(input("Ingresa tu estatura: "))
        nombre = nombre_completo.split()
        apellido_materno = nombre.pop()
        apellido_paterno = nombre.pop()
        nombre = " ".join(nombre)
        break
    # La excepcion muestra el mensaje y se manda llamar cuando no se puede realizar alguna accion dentro del try.
    except:
        print("No debe haber datos vacios, favor de ingresarlos nuevamente")
# Calculamos el indice de masa muscular.
imc = peso / estatura**2

# creamos una variable con todos los datos.
datos = f"Los datos obtenidos son: \n"\
        f"{nombre =}\n"\
        f"{apellido_paterno = }\n"\
        f"{apellido_materno =}\n"\
        f"{edad = }\n"\
        f"{peso = }\n"\
        f"{estatura = }\n"\
        f"{imc = }\n"

# Imprimimos los datos
print(datos)




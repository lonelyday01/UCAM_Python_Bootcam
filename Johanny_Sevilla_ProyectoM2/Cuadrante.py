"""
Crear un programa que en base a 2 números de entrada, coordenadas,
identifique en cuál de los 4 cuadrantes se encuentra el punto.
El programa debe verificar que ninguna coordenada sea 0.
"""

# Creamos un ciclo while infinito para evaluar las coordenadas ingresadas y evitar que se ingresen valores de 0
# Este while True podria funcionar como un "do-while"
while True:
    # Ingreso de coordenadas por el usuario, ademas de castear los inputs de "strings" a "int"
    x = int(input("Ingrese X: "))
    y = int(input("Ingrese Y: "))

    # Evaluamos que ninguno de los 2 valos ingresados sea igual a 0, si son diferentes de 0 se rompe el ciclo infinito
    if (x and y) != 0:
        break
    print("No puede haber coordenadas 0, por favor ingrese nuevamente las coordenadas")

# Declaramos una variable mensaje, para evitar escribirla repetidas veces
msj = "El punto se encuentra en el cuadrante:"

# Evaluamos si ambas coordenadas son positivas
if x > 0 < y:
    cuadrante = 1
    print(f"{msj} {cuadrante}")
# Evaluamos si "X" es positivo y "Y" negativo
elif x > 0 > y:
    cuadrante = 4
    print(f"{msj} {cuadrante}")
# Evaluamos si "X" es negativo y "Y" Positivo
elif x < 0 < y:
    cuadrante = 2
    print(f"{msj} {cuadrante}")

# Evaluamos al ultimo cuadrante.
else:
    cuadrante = 3
    print(f"{msj} {cuadrante}")

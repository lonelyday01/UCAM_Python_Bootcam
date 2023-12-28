"""
Las características de tu programa:
Será la simulación de una máquina de Galton de 3000 canicas.
En total tendrá 12 niveles de obstáculos -deberás decidir si va a caer a un lado o al otro 12 veces.
El resultado final será un histograma que represente la cantidad de canicas en cada contenedor, como el siguiente
-No olvides colocar nombre a los ejes y un título al gráfico.
Deberás emplear dos funciones, una para calcular los resultados de las canicas
y la segunda para la graficación del histograma.

Recuerda que NO es necesario hacer la animación de las canicas cayendo ni los obstáculos, solamente los contenedores
con los resultados de la simulación. NO debes usar la función normal().
"""
import random
from matplotlib import pyplot as plt


def maquina_galton(num_canicas=3000, num_niveles=12):
    diccionario_contenedores = {i: 0 for i in range(0, (num_niveles*2)+1, 2)}

    for _ in range(num_canicas):
        num_contenedor = calculo_resultados(num_niveles)
        diccionario_contenedores[num_contenedor] += 1
    return diccionario_contenedores


def calculo_resultados(num_niveles):
    # Declaracion de variables

    decisiones = ["Derecha", "Izquierda"]
    posicion_contenedor = 12

    for _ in range(num_niveles):
        if random.choice(decisiones) == "Derecha":
            posicion_contenedor += 1
        else:
            posicion_contenedor -= 1
    return posicion_contenedor


def mostrar_grafica(diccionario_contenedores):
    plt.bar(diccionario_contenedores.keys(), diccionario_contenedores.values(), color="Red")
    plt.title("Maquina de Galton")
    plt.xlabel("Distribucion de canicas")
    plt.ylabel("Cantidad de canicas")
    plt.show()


resultados = maquina_galton()
mostrar_grafica(resultados)

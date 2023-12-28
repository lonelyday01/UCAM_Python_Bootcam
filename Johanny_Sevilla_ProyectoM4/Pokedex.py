import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json
import sys
import os
import pdb

from Johanny_Sevilla_ProyectoM4.pokemon import Pokemon

path_actual = os.getcwd()

def print_datos(nombre, peso, tamano, movimientos, habilidades, tipos):
    print(f"Los datos de {nombre} son: ")
    print(f"Peso:{peso} \nTamaño:{tamano}")
    print(f"Movimientos de {pokemon}")
    [print(f'#{num_mov + 1} - {movimiento["move"]["name"]}') for num_mov, movimiento in enumerate(movimientos)]
    print(f"Habilidades de {pokemon}")
    [print(f'#{num_hab + 1} - {habilidad["ability"]["name"]}') for num_hab, habilidad in enumerate(habilidades)]
    print(f"{pokemon} es de tipo: ")
    [print(f'#{num_tipo} - {tipo["type"]["name"]}') for num_tipo, tipo in enumerate(tipos)]


def cargar_pokedex(pokemon):
    archivo_pokedex = "pokedex.json"
    path_archivo_pokedex = os.path.join(path_actual, archivo_pokedex)

    try:
        with open(path_archivo_pokedex, "r") as file:
            datos_actuales = json.load(file)
    except FileNotFoundError:
        datos_actuales = {}
    datos_actuales.update(pokemon.convertir_datos_pokemon())
    with open(path_archivo_pokedex, "w") as file:
        json.dump(datos_actuales, file, indent=4)


def cargar_pokemon_json(pokemon):
    carpeta_pokedex = "Pokedex"
    carpeta_pokemon = os.path.join(path_actual, carpeta_pokedex)
    pokemon_json_name = f"{pokemon.nombre}.json"
    path_pokemon_json = os.path.join(carpeta_pokemon, pokemon_json_name)
    if not os.path.isdir(carpeta_pokedex):
        os.mkdir(carpeta_pokedex)
    datos_pokemon = pokemon.convertir_datos_pokemon()
    with open(path_pokemon_json, "w") as file:
        json.dump(datos_pokemon, file, indent=4)


while True:
    pokemon = input("Ingresa el nombre de un pokemon: ").lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    respuesta = requests.get(url)
    if pokemon == "salir":
        exit()
    elif respuesta.status_code == 404:
        print(f"El Pokemon {pokemon} ingresado no fue encontado")

    elif respuesta.status_code != 200:
        print("No se completo la conexion con la API")

    elif pokemon == "":
        print("No se ingreso nada")

    else:
        datos = respuesta.json()
        try:
            objPokemon = Pokemon()
            objPokemon.nombre = pokemon
            objPokemon.imagen = url_imagen = datos["sprites"]["front_default"]
            imagen = Image.open(urlopen(url_imagen))
            objPokemon.peso = datos["weight"]
            objPokemon.tamano = datos["height"]
            movimientos = datos["moves"]
            [objPokemon.movimientos.append(movimiento["move"]["name"]) for movimiento in movimientos]
            habilidades = datos["abilities"]
            [objPokemon.habilidades.append(habilidad["ability"]["name"]) for habilidad in habilidades]
            tipos = datos["types"]
            [objPokemon.tipos.append(tipo["type"]["name"]) for tipo in tipos]
            print_datos(pokemon, objPokemon.peso, objPokemon.tamano, movimientos, habilidades, tipos)

            cargar_pokedex(objPokemon)
            cargar_pokemon_json(objPokemon)

        except ZeroDivisionError:
            print("No se encontro la imagen del pokemon")
            break

        plt.title(pokemon)
        imgplot = plt.imshow(imagen)
        plt.show()

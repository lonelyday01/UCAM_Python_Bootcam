class Pokemon:

    def __init__(self, nombre="", peso=0, tamano=0, movimientos=None, habilidades=None, tipos=None, imagen=""):
        self.nombre = nombre
        self.peso = peso
        self.tamano = tamano
        self.movimientos = movimientos or []
        self.habilidades = habilidades or []
        self.tipos = tipos or []
        self.imagen = imagen

    def convertir_datos_pokemon(self):
        datos_pokemon = {
            self.nombre:
            {
                "Nombre": self.nombre,
                "Peso": self.peso,
                "Tamano": self.tamano,
                "Movimientos": self.movimientos,
                "Habilidades": self.habilidades,
                "Tipos": self.tipos,
                "Imagen": self.imagen
            }
        }
        return datos_pokemon

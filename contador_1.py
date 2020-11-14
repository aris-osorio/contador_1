import re
from unidecode import unidecode

def crear_lista(cadena):
    cadena = cadena.replace("\n" , " ")
    cadena = re.sub(r"[^A-Za-z0-9áéíóúüñÁÉÍÓÚÜÑ]+", " ", cadena)
    cadena = unidecode(cadena)
    cadena = cadena.lower()
    lista = cadena.split(" ")
    return lista


def obtener_cadena():
    nombre = input("nombre o direccion de libro: ")
    archivo = open(nombre,  encoding="utf8")
    cadena = archivo.read()
    archivo.close()
    return cadena

def main():
    cadena = obtener_cadena()
    lista = crear_lista(cadena)
    print(lista)


if __name__ == "__main__":
    main()
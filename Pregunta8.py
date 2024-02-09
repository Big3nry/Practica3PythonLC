import random
def generar_numeros_aleatorios(cantidad=20, rango=(0, 100)):
    return [random.randint(rango[0], rango[1]) for _ in range(cantidad)]
def mostrar_lista(lista):
    print("Lista generada:", lista)
def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)

if __name__ == "__main__":
    numeros_aleatorios = generar_numeros_aleatorios()
    mostrar_lista(numeros_aleatorios)
    ordenar_y_mostrar(numeros_aleatorios)

import mi_modulo
numeros_aleatorios = mi_modulo.generar_numeros_aleatorios()
mi_modulo.mostrar_lista(numeros_aleatorios)
mi_modulo.ordenar_y_mostrar(numeros_aleatorios)


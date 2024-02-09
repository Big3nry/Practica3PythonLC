from clases_geometricas import Circulo, Rectangulo, Cuadrado

def mostrar_menu():
    print("Menú:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = Circulo(radio)
    area = circulo.calcular_area()
    print(f"El área del círculo es: {area}")

def calcular_area_rectangulo():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    rectangulo = Rectangulo(base, altura)
    area = rectangulo.calcular_area()
    print(f"El área del rectángulo es: {area}")

def calcular_area_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    cuadrado = Cuadrado(lado)
    area = cuadrado.calcular_area()
    print(f"El área del cuadrado es: {area}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            calcular_area_circulo()
        elif opcion == '2':
            calcular_area_rectangulo()
        elif opcion == '3':
            calcular_area_cuadrado()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

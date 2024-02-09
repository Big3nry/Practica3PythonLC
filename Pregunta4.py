class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

mi_rectangulo = Rectangulo(5, 3)
print("El área del rectángulo es:", mi_rectangulo.calcular_area())

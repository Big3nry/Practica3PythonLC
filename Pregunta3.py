class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2
        
mi_circulo = Circulo(5)
print("El área del círculo es:", mi_circulo.calcular_area())

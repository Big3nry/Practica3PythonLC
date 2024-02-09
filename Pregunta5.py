class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de Registro:", self.numero_registro)
        print("Edad:", self.edad)
        print("Notas:", self.notas)

    def set_age(self, edad):
        self.edad = edad

    def set_nota(self, nota):
        self.notas.append(nota)


alumno1 = Alumno("Juan Perez", "12345")
alumno1.set_age(20)
alumno1.set_nota(85)
alumno1.set_nota(90)

alumno1.display()
class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Año: {self.año}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        for producto in productos_filtrados:
            print(producto)

catalogo = Catalogo()
producto1 = Producto("Llanta", 100, 2022)
producto2 = Producto("Batería", 150, 2021)
catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)

print("Lista de Productos:")
catalogo.mostrar_productos()

print("\nProductos del 2022:")
catalogo.filtrar_por_año(2022)
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Asegurarse de que el ID sea único
        for prod in self.productos:
            if prod.get_id() == producto.get_id():
                print("Error: El ID ya existe.")
                return
        self.productos.append(producto)

    def eliminar_producto(self, id):
        self.productos = [prod for prod in self.productos if prod.get_id() != id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for prod in self.productos:
            if prod.get_id() == id:
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                return
        print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        for prod in self.productos:
            print(prod)

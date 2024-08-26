from producto import Producto

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """Cargar productos desde el archivo."""
        try:
            with open(self.archivo, 'r') as file:
                for line in file:
                    id, nombre, cantidad, precio = line.strip().split('|')
                    producto = Producto(int(id), nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
        except FileNotFoundError:
            # El archivo no existe, crearemos uno nuevo
            open(self.archivo, 'w').close()
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guardar productos en el archivo."""
        try:
            with open(self.archivo, 'w') as file:
                for prod in self.productos:
                    file.write(f"{prod.get_id()}|{prod.get_nombre()}|{prod.get_cantidad()}|{prod.get_precio()}\n")
        except PermissionError:
            print("Error: No tienes permiso para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        # Asegurarse de que el ID sea único
        if any(prod.get_id() == producto.get_id() for prod in self.productos):
            print("Error: El ID ya existe.")
            return
        self.productos.append(producto)
        self.guardar_inventario()

    def eliminar_producto(self, id):
        self.productos = [prod for prod in self.productos if prod.get_id() != id]
        self.guardar_inventario()

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for prod in self.productos:
            if prod.get_id() == id:
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                self.guardar_inventario()
                return
        print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        for prod in self.productos:
            print(prod)

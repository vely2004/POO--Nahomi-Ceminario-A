import pickle  # Para guardar y cargar el inventario en archivos


class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos (ID -> Producto)

    # Método para agregar un producto
    def agregar_producto(self, producto):
        self.productos[producto.obtener_id()] = producto

    # Método para eliminar un producto por ID
    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            del self.productos[producto_id]
            print(f"Producto con ID {producto_id} ha sido eliminado.")
        else:
            print(f"No se encontró el producto con ID {producto_id}.")

    # Método para actualizar cantidad o precio
    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)
            print(f"Producto con ID {producto_id} ha sido actualizado.")
        else:
            print(f"No se encontró el producto con ID {producto_id}.")

    # Método para buscar producto por nombre
    def buscar_producto(self, nombre):
        encontrados = [producto for producto in self.productos.values() if
                       nombre.lower() in producto.obtener_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    # Método para mostrar todos los productos en inventario
    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    # Guardar el inventario en un archivo
    def guardar_inventario(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)
        print("Inventario guardado en el archivo.")

    # Cargar el inventario desde un archivo
    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'rb') as f:
                self.productos = pickle.load(f)
            print("Inventario cargado desde el archivo.")
        except FileNotFoundError:
            print("El archivo no existe. Cargando inventario vacío.")


class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.producto_id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def _producto_existente(self, producto_id):
        return any(producto.producto_id == producto_id for producto in self.productos)

    def añadir_producto(self, producto_id, nombre, cantidad, precio):
        if self._producto_existente(producto_id):
            print(f"Error: Ya existe un producto con el ID {producto_id}.")
        else:
            nuevo_producto = Producto(producto_id, nombre, cantidad, precio)
            self.productos.append(nuevo_producto)
            print(f"Producto {nombre} añadido exitosamente.")

    def eliminar_producto(self, producto_id):
        for producto in self.productos:
            if producto.producto_id == producto_id:
                self.productos.remove(producto)
                print(f"Producto con ID {producto_id} eliminado exitosamente.")
                return
        print(f"Error: No se encontró el producto con ID {producto_id}.")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.producto_id == producto_id:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print(f"Producto con ID {producto_id} actualizado exitosamente.")
                return
        print(f"Error: No se encontró el producto con ID {producto_id}.")

    def buscar_producto(self, nombre):
        productos_encontrados = [producto for producto in self.productos if nombre.lower() in producto.nombre.lower()]
        if productos_encontrados:
            print("Productos encontrados:")
            for producto in productos_encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            print("Productos en inventario:")
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")


# Ejemplo de uso de la clase Inventario
if __name__ == "__main__":
    inventario = Inventario()

    # Añadir productos
    inventario.añadir_producto(1, "Laptop", 10, 800)
    inventario.añadir_producto(2, "Smartphone", 15, 500)

    # Mostrar todos los productos
    inventario.mostrar_todos_los_productos()

    # Actualizar cantidad o precio
    inventario.actualizar_producto(1, cantidad=12)

    # Buscar productos por nombre
    inventario.buscar_producto("laptop")

    # Eliminar producto por ID
    inventario.eliminar_producto(2)

    # Mostrar todos los productos después de eliminación
    inventario.mostrar_todos_los_productos()
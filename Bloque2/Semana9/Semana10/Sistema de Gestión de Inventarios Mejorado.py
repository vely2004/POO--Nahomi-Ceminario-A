import os
import json


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde el archivo si existe."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r", encoding="utf-8") as f:
                    self.productos = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                print("Error: No se pudo leer el archivo. Se iniciará un nuevo inventario.")
                self.productos = {}
        else:
            self.guardar_inventario()

    def guardar_inventario(self):
        """Guarda el inventario en un archivo."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(self.productos, f, indent=4)
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un producto al inventario y lo guarda en el archivo."""
        if nombre in self.productos:
            print("El producto ya existe. Usa actualizar_producto en su lugar.")
        else:
            self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
            self.guardar_inventario()
            print(f"Producto {nombre} agregado exitosamente.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        """Actualiza la cantidad o precio de un producto."""
        if nombre in self.productos:
            if cantidad is not None:
                self.productos[nombre]["cantidad"] = cantidad
            if precio is not None:
                self.productos[nombre]["precio"] = precio
            self.guardar_inventario()
            print(f"Producto {nombre} actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario y lo guarda en el archivo."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto {nombre} eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            for nombre, datos in self.productos.items():
                print(f"{nombre}: Cantidad {datos['cantidad']}, Precio ${datos['precio']:.2f}")
        else:
            print("El inventario está vacío.")


if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para mantener actual): ")
            precio = input("Nuevo precio (dejar en blanco para mantener actual): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(nombre, cantidad, precio)
        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del sistema de inventario.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
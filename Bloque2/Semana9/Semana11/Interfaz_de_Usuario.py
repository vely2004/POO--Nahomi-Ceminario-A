from Inventario import Inventario
from Producto import Producto
def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")

def ejecutar():
    inventario = Inventario()
    archivo_inventario = 'inventario.dat'

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            producto_id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: $"))
            producto = Producto(producto_id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            producto_id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(producto_id)

        elif opcion == '3':
            producto_id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Nuevo precio (deje en blanco para no cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(producto_id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            inventario.guardar_inventario(archivo_inventario)

        elif opcion == '7':
            inventario.cargar_inventario(archivo_inventario)

        elif opcion == '8':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    ejecutar()


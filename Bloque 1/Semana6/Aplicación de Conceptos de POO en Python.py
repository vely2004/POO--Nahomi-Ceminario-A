# Clase base para Producto
class Producto:
    def __init__(self, nombre, precio, marca):
        self._nombre = nombre  # Atributo protegido
        self._precio = precio  # Atributo protegido
        self._marca = marca  # Atributo protegido

    def descripcion(self):
        return f"Producto: {self._nombre}, Precio: ${self._precio:.2f}, Marca: {self._marca}"

    def comprar(self):
        return "Has comprado este producto."

# Clase derivada para Smartphones
class Smartphone(Producto):
    def __init__(self, nombre, precio, marca, capacidad):
        super().__init__(nombre, precio, marca)
        self.__capacidad = capacidad  # Atributo privado

    def descripcion(self):
        return f"Smartphone: {self._nombre}, Precio: ${self._precio:.2f}, Marca: {self._marca}, Capacidad: {self.__capacidad}GB"

    def comprar(self):
        return f"Has comprado el smartphone {self._nombre}."

# Clase derivada para Accesorios
class Accesorio(Producto):
    def __init__(self, nombre, precio, marca, tipo):
        super().__init__(nombre, precio, marca)
        self.__tipo = tipo  # Atributo privado

    def descripcion(self):
        return f"Accesorio: {self._nombre}, Precio: ${self._precio:.2f}, Marca: {self._marca}, Tipo: {self.__tipo}"

    def comprar(self):
        return f"Has comprado el accesorio {self._nombre}."

# Implementación y demostración
if __name__ == "__main__":
    # Instancia de la clase base
    producto_generico = Producto("Producto genérico", 10.99, "Marca X")
    print(producto_generico.descripcion())
    print(producto_generico.comprar())

    # Instancia de la clase derivada Smartphone
    mi_smartphone = Smartphone("Galaxy S21", 799.99, "Samsung", 128)
    print(mi_smartphone.descripcion())
    print(mi_smartphone.comprar())

    # Instancia de la clase derivada Accesorio
    mi_accesorio = Accesorio("Cargador Rápido", 29.99, "Anker", "Cargador")
    print(mi_accesorio.descripcion())
    print(mi_accesorio.comprar())

    # Ejemplo de polimorfismo
    productos = [producto_generico, mi_smartphone, mi_accesorio]
    for producto in productos:
        print(producto.comprar())
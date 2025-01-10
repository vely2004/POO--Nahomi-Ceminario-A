# Programación Orientada a Objetos (POO)
# Ejemplo: Simulación de compra de ropa

class Ropa:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo
        self.carrito = []

    def agregar_al_carrito(self, prenda):
        self.carrito.append(prenda)

    def quitar_del_carrito(self, prenda):
        if prenda in self.carrito:
            self.carrito.remove(prenda)

    def ver_carrito(self):
        print(f"Carrito de {self.nombre}:")
        if not self.carrito:
            print("El carrito está vacío.")
        else:
            for prenda in self.carrito:
                print(prenda)

    def realizar_pago(self):
        total = sum([prenda.precio for prenda in self.carrito])
        if total <= self.saldo:
            self.saldo -= total
            self.carrito = []  # Vaciar el carrito después de la compra
            print(f"Compra realizada con éxito. Total: ${total}. Saldo restante: ${self.saldo}")
        else:
            print(f"Saldo insuficiente para realizar la compra. Necesitas ${total - self.saldo} más.")


# Crear instancias de ropa
camisa = Ropa("Camisa de Algodón", 25)
pantalon = Ropa("Pantalón de Mezclilla", 40)
chaqueta = Ropa("Chaqueta de Cuero", 80)

# Crear una instancia de cliente
cliente = Cliente("Ana", 100)

# Agregar prendas al carrito
cliente.agregar_al_carrito(camisa)
cliente.agregar_al_carrito(pantalon)
cliente.ver_carrito()

# Realizar el pago
cliente.realizar_pago()

# Mostrar saldo después de la compra
print(f"Saldo final de {cliente.nombre}: ${cliente.saldo}")
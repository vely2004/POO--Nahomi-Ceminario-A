class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id  # ID único
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad en inventario
        self.precio = precio  # Precio del producto

    # Métodos para obtener y establecer atributos
    def obtener_id(self):
        return self.producto_id

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} (ID: {self.producto_id}) - Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


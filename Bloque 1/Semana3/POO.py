class Climad:
    """Clase para gestionar las temperaturas diarias y calcular el promedio semanal."""

    def __init__(self):
        self.temperaturas = []  # Lista para almacenar las temperaturas diarias

    def ingresar_temperaturas(self, num_dias):
        """Solicita al usuario las temperaturas diarias y las guarda."""
        for i in range(num_dias):
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                    self.temperaturas.append(temp)
                    break  # Salir del bucle si la entrada es válida
                except ValueError:
                    print("Error: Por favor, ingrese un número válido.")

    def calcular_promedio(self):
        """Calcula y devuelve el promedio semanal de las temperaturas."""
        if not self.temperaturas:
            raise ValueError("No se han ingresado temperaturas.")
        return sum(self.temperaturas) / len(self.temperaturas)


# Programa principal
if __name__ == "__main__":
    print("-- Cálculo de Promedio Semanal de Temperaturas (POO) --")
    dias_semana = 7
    clima = Climad()  # Instancia de la clase
    clima.ingresar_temperaturas(dias_semana)
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")

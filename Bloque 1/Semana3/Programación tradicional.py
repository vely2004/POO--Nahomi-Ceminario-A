#Programación tradicional
#Solución para ingresar datos y calcular promedio semanal
def ingresa_temperaturas(num_dias):
    """"Solicita las temperaturas diarias al usuario y las almacena en una lista."""
    temperaturas = []
    for i in range(num_dias):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """Calcula el promedio de las temperaturas ingresadas."""
    return sum(temperaturas) / len(temperaturas)

    # Programa principal

if __name__ == "__main__":
    print("-- Cálculo de Promedio Semanal de Temperaturas (Programación Tradicional) --")
    dias_semana = 7
    temperaturas_semanales = ingresa_temperaturas(dias_semana)
    promedio = calcular_promedio(temperaturas_semanales)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")
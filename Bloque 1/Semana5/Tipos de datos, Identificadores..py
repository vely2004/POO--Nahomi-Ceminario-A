def convertir_metros_a_kilometros(metros):
    """Convierte metros a kilómetros."""
    kilometros = metros / 1000
    return kilometros

def convertir_gramos_a_kilogramos(gramos):
    """Convierte gramos a kilogramos."""
    kilogramos = gramos / 1000
    return kilogramos

def convertir_litros_a_mililitros(litros):
    """Convierte litros a mililitros."""
    mililitros = litros * 1000
    return mililitros

def mostrar_menu():
    """Muestra el menú de opciones para el usuario."""
    print("Seleccione la conversión que desea realizar:")
    print("1. Metros a Kilómetros")
    print("2. Gramos a Kilogramos")
    print("3. Litros a Mililitros")
    print("4. Salir")

def obtener_opcion_usuario():
    """Obtiene la opción seleccionada por el usuario."""
    while True:
        try:
            opcion = int(input("Ingrese el número de opción: "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Opción no válida, por favor ingrese un número entre 1 y 4.")
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número entero.")

def main():
    """Función principal que ejecuta el programa."""
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = obtener_opcion_usuario()

        if opcion == 1:
            metros = float(input("Ingrese la cantidad de metros: "))
            kilometros = convertir_metros_a_kilometros(metros)
            print(f"{metros} metros equivalen a {kilometros:.2f} kilómetros.")
        elif opcion == 2:
            gramos = float(input("Ingrese la cantidad de gramos: "))
            kilogramos = convertir_gramos_a_kilogramos(gramos)
            print(f"{gramos} gramos equivalen a {kilogramos:.2f} kilogramos.")
        elif opcion == 3:
            litros = float(input("Ingrese la cantidad de litros: "))
            mililitros = convertir_litros_a_mililitros(litros)
            print(f"{litros} litros equivalen a {mililitros:.2f} mililitros.")
        elif opcion == 4:
            print("¡Hasta luego!")
            continuar = False

if __name__ == "__main__":
    main()
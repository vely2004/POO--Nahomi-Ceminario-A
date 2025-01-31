import os
import subprocess

# Colores para la terminal
class Colores:
    ROJO = '\033[91m'         # Rojo para errores
    ROSA = '\033[35m'         # Rosa para éxito
    CELESTE = '\033[96m'      # Celeste para títulos
    FUCSIA = '\033[95m'       # Fucsia para instrucciones
    RESET = '\033[0m'         # Reset para restaurar el color por defecto

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n{Colores.CELESTE}--- Código de {ruta_script} ---{Colores.RESET}\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(f"{Colores.ROJO}El archivo no se encontró.{Colores.RESET}")
        return None
    except Exception as e:
        print(f"{Colores.ROJO}Ocurrió un error al leer el archivo: {e}{Colores.RESET}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"{Colores.ROJO}Ocurrió un error al ejecutar el código: {e}{Colores.RESET}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print(f"\n{Colores.CELESTE}Menu Principal - Dashboard{Colores.RESET}")
        # Imprime las opciones del menú principal
        for key in unidades:
            print(f"{Colores.CELESTE}{key} - {unidades[key]}{Colores.RESET}")
        print(f"{Colores.ROJO}0 - Salir{Colores.RESET}")

        eleccion_unidad = input(f"{Colores.FUCSIA}Elige una unidad o '0' para salir: {Colores.RESET}")
        if eleccion_unidad == '0':
            print(f"{Colores.ROSA}Saliendo del programa.{Colores.RESET}")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print(f"{Colores.ROJO}Opción no válida. Por favor, intenta de nuevo.{Colores.RESET}")

def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = sorted([f.name for f in os.scandir(ruta_unidad) if f.is_dir()])

    while True:
        print(f"\n{Colores.CELESTE}Submenú - Selecciona una subcarpeta{Colores.RESET}")
        # Imprime las subcarpetas
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{Colores.CELESTE}{i} - {carpeta}{Colores.RESET}")
        print(f"{Colores.ROJO}")

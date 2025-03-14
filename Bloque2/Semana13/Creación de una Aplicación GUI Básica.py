import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_info():
    info = entrada.get()  # Obtiene el texto ingresado en el campo de entrada
    if info:  # Si el campo no está vacío
        lista.insert(tk.END, info)  # Inserta el texto en la lista
        entrada.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa algo antes de agregar.")

# Función para limpiar el campo de entrada y la lista
def limpiar():
    entrada.delete(0, tk.END)  # Limpia el campo de entrada
    lista.delete(0, tk.END)  # Limpia la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Información")
ventana.geometry("400x350")

# Etiqueta de título
titulo = tk.Label(ventana, text="Ingrese la información:", font=("Arial", 14))
titulo.pack(pady=10)

# Campo de entrada de texto
entrada = tk.Entry(ventana, font=("Arial", 12), width=30)
entrada.pack(pady=10)

# Botón para agregar la información
boton_agregar = tk.Button(ventana, text="Agregar", font=("Arial", 12), command=agregar_info)
boton_agregar.pack(pady=5)

# Lista para mostrar la información agregada
lista = tk.Listbox(ventana, font=("Arial", 12), width=40, height=10)
lista.pack(pady=10)

# Botón para limpiar la entrada y la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", font=("Arial", 12), command=limpiar)
boton_limpiar.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()


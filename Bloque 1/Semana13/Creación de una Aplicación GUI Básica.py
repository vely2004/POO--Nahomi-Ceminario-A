import tkinter as tk
from tkinter import ttk

# Función para agregar números y operadores a la entrada
def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

def calcular(*args):
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
        log.config(text=f"Expresión: {expresion}")
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

# Función para borrar el contenido de entrada
def limpiar():
    entrada.delete(0, tk.END)
    log.config(text="")

# Generar la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Velsh")
ventana.geometry("400x350")

# Centrar la ventana en la pantalla
ventana.update_idletasks()
anchura = 400
altura = 350
pantalla_ancho = ventana.winfo_screenwidth()
pantalla_alto = ventana.winfo_screenheight()
x = (pantalla_ancho // 2) - (anchura // 2)
y = (pantalla_alto // 2) - (altura // 2)
ventana.geometry(f"{anchura}x{altura}+{x}+{y}")

# Crear menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Limpiar", command=limpiar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Crear un campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 18), justify='right', bd=10, relief=tk.RIDGE)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
entrada.bind("<Return>", calcular)
entrada.bind("<Escape>", lambda event: limpiar())

# Crear un label para visualizar las operaciones
log = tk.Label(ventana, text="", font=("Arial", 12), fg="pink")
log.grid(row=1, column=0, columnspan=4)

# Botones de la calculadora
botones = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 3)
]

def crear_boton(texto, fila, columna):
    return tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 14), command=lambda: agregar_caracter(texto))\
        .grid(row=fila, column=columna, padx=5, pady=5)

# Ahora se vincula el "=" con la función de cálculo
tk.Button(ventana, text="=", width=5, height=2, font=("Arial", 14), command=calcular).grid(row=5, column=2, padx=5, pady=5)

# Crear los botones de la calculadora
for (text, fila, columna) in botones:
    crear_boton(texto=text, fila=fila, columna=columna)

ventana.mainloop()

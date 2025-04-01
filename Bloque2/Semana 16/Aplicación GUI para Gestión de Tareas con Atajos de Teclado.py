import tkinter as tk
from tkinter import messagebox

def agregar_tarea(event=None):
    tarea= entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía")
def marcar_completada(evento=None):
    try:
        seleccion= lista_tareas.curselection()[0]
        tarea= lista_tareas.get(seleccion)
        lista_tareas.delete(seleccion)
        lista_tareas.insert(seleccion, f"✔ {tarea}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completa. ")
def eliminar_tarea(event=None):
    try:
        seleccion= lista_tareas.curselection()[0]
        lista_tareas.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")
def cerrar_app(event=None):
    ventana.quit()

#Crear ventana principal
ventana=tk.Tk()
ventana.title("Gestión de Tareas")
ventana.geometry("300x300")
ventana.configure(bg="#FFC0CB") #Aplicamos un fondo rosa
#Entrada de texto paera agg tareas
entrada_tarea= tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_tarea)#Atajo de teclado de Enter
# Lista de tareas
lista_tareas= tk.Listbox(ventana, width=40, height=10, bg="#FF6994") #Color de fondo
lista_tareas.pack(pady=10)

#Botones
frame_botones= tk.Frame(ventana, bg="#FFC0CB") #Fondo de color
frame_botones.pack()

btn_agregar=tk.Button(frame_botones, text="Añadir", command=agregar_tarea, bg="#FF69B4")
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar=tk.Button(frame_botones, text="completa", command=marcar_completada, bg="#FF6994")
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="eliminar", command=eliminar_tarea, bg="#FF6994")
btn_eliminar.grid(row=0, column=2, padx=5)
#Atajos de teclado
ventana.bind("<plus>", marcar_completada)
ventana.bind("<KP_Add>", marcar_completada)
ventana.bind("<minus>", eliminar_tarea)
ventana.bind("<KP_Subtract>", eliminar_tarea)  # Para el teclado numérico

ventana.mainloop()


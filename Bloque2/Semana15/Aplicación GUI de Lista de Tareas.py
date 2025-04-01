import tkinter as tk
from tkinter import messagebox

class ListaTareas(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.tareas = []  # Lista que almacena las tareas

        # Escoger los colores de fondo de la lista de tarea
        rosa_claro = "#FAD0C9"
        rosa_oscuro = "#F287A3"
        rosa_medio = "#F5A7C0"

        # Campo de entrada para escribir nuevas tareas con fondo rosado claro
        self.entry_tarea = tk.Entry(self.root, width=40, bg=rosa_claro, fg="black", font=("Arial", 12))
        self.entry_tarea.grid(row=0, column=0, pady=10)

        # Botón para añadir tarea
        self.boton_anadir = tk.Button(self.root, text="Añadir tarea", width=20, bg=rosa_oscuro, fg="black", font=("Arial", 12), command=self.anadir_tarea)
        self.boton_anadir.grid(row=1, column=0, padx=10, pady=10)

        # Botón para marcar tarea como completada
        self.boton_completar = tk.Button(self.root, text="Marcar como completada", width=20, bg=rosa_oscuro, fg="black", font=("Arial", 12), command=self.marcar_completada)
        self.boton_completar.grid(row=2, column=0, padx=10, pady=10)

        # Botón para eliminar tarea
        self.boton_eliminar = tk.Button(self.root, text="Eliminar tarea", width=20, bg=rosa_medio, fg="black", font=("Arial", 12), command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=3, column=0, padx=10, pady=10)

        # Listbox para mostrar las tareas
        self.listbox_tareas = tk.Listbox(self.root, width=40, height=10, bg=rosa_claro, fg="black", font=("Arial", 12))
        self.listbox_tareas.grid(row=4, column=0, padx=10, pady=10)

        # Eventos
        self.entry_tarea.bind("<Return>", self.anadir_tarea_con_tecla)

    def anadir_tarea(self):
        tarea = self.entry_tarea.get().strip()
        if tarea != "":
            self.tareas.append(tarea)
            self.actualizar_lista_tareas()
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

    def anadir_tarea_con_tecla(self, event=None):
        self.anadir_tarea()

    def actualizar_lista_tareas(self):
        # Limpiar la lista y mostrar las tareas actuales
        self.listbox_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            self.listbox_tareas.insert(tk.END, tarea)

    def marcar_completada(self):
        try:
            indice = self.listbox_tareas.curselection()[0]
            tarea = self.tareas[indice]
            self.tareas[indice] = tarea + " (Completada)"
            self.actualizar_lista_tareas()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para marcar como completada.")

    def eliminar_tarea(self):
        try:
            indice = self.listbox_tareas.curselection()[0]
            del self.tareas[indice]
            self.actualizar_lista_tareas()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareas(root)
    root.mainloop()

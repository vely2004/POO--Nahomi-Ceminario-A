import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Frame de entrada de datos
        self.frame_input = tk.Frame(self.root)
        self.frame_input.pack(pady=10)

        tk.Label(self.frame_input, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame_input, width=12, background='darkblue', foreground='white',
                                    borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_input, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(self.frame_input, width=15)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_input, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(self.frame_input, width=30)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones
        self.btn_add = tk.Button(self.frame_input, text="Agregar Evento", command=self.add_event)
        self.btn_add.grid(row=3, column=0, columnspan=2, pady=10)

        # Frame de visualización
        self.frame_view = tk.Frame(self.root)
        self.frame_view.pack()

        self.tree = ttk.Treeview(self.frame_view, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Botón de eliminación
        self.btn_delete = tk.Button(self.root, text="Eliminar Evento", command=self.delete_event)
        self.btn_delete.pack(pady=5)

        # Botón de salida
        self.btn_exit = tk.Button(self.root, text="Salir", command=self.root.quit)
        self.btn_exit.pack(pady=5)

    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        desc = self.desc_entry.get()
        if date and time and desc:
            self.tree.insert("", "end", values=(date, time, desc))
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

    def delete_event(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")
            return
        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el evento seleccionado?")
        if confirm:
            for item in selected_item:
                self.tree.delete(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
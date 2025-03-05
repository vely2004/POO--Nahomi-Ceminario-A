class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.detalles = (autor, titulo)  # Tupla inmutable

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}, Categoría: {self.categoria})"

class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"

class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario {ISBN: Libro}
        self.usuarios = set()  # Conjunto de IDs de usuarios
        self.prestamos = {}  # Diccionario {user_id: lista de libros prestados}

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
        else:
            print("El libro ya existe en la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado de la biblioteca.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios:
            self.usuarios.add(usuario.user_id)
            self.prestamos[usuario.user_id] = []
            print(f"Usuario '{usuario.nombre}' registrado.")
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            if not self.prestamos[user_id]:  # Asegurar que no tenga libros prestados
                self.usuarios.remove(user_id)
                del self.prestamos[user_id]
                print("Usuario eliminado.")
            else:
                print("No se puede eliminar, tiene libros pendientes.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            if isbn not in self.prestamos[user_id]:
                self.prestamos[user_id].append(isbn)
                print("Libro prestado correctamente.")
            else:
                print("El usuario ya tiene este libro prestado.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.prestamos[user_id]:
            self.prestamos[user_id].remove(isbn)
            print("Libro devuelto correctamente.")
        else:
            print("No se encontró el préstamo de este libro.")

    def buscar_libro(self, **criterios):
        resultado = []
        for libro in self.libros.values():
            if all(getattr(libro, clave) == valor for clave, valor in criterios.items()):
                resultado.append(libro)
        return resultado

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            libros_prestados = [self.libros[isbn] for isbn in self.prestamos[user_id]]
            return libros_prestados
        return []

# Pruebas del sistema
biblio = Biblioteca()

libro1 = Libro("1984", "George Orwell", "Ficción", "12345")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "67890")
usuario1 = Usuario("Ana", "U001")

biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)
biblio.registrar_usuario(usuario1)
biblio.prestar_libro("U001", "12345")
print("Libros prestados:", [str(lib) for lib in biblio.listar_libros_prestados("U001")])
biblio.devolver_libro("U001", "12345")
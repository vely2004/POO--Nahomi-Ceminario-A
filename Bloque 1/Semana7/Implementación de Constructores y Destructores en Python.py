class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        ''' Constructor: Inicializa los atributos del objeto.
        :param titulo: Título del libro.
        :param autor: Autor del libro.
        :param anio_publicacion: Año de publicación del libro.'''
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        print(f"Libro '{self.titulo}' creado.")  # Esto se ejecuta cuando el objeto es creado

    def mostrar_info(self):
        '''Sirve para mostrar la información del libro.'''
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")

    def __del__(self):
        ''' Destructor: Simula la limpieza de recursos al eliminar el objeto.'''
        print(f"Libro '{self.titulo}' ha sido destruido.")  # Esto se ejecuta cuando el objeto es destruido

# Crear una instancia del objeto
mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)

# Mostrar la información del libro
mi_libro.mostrar_info()

# Eliminar el objeto para activar el destructor
del mi_libro
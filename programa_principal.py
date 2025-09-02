class Usuario:
    def __init__(self, nombre, rol, id):
        super().__init__()
        self.__nombre = nombre
        self.__rol = rol
        self.__id = id

class Estudiante(Usuario):
    def __init__(self, nombre, rol, id, carrera, cursos):
        super().__init__(nombre, rol, id)
        self.__carrera = carrera
        self.__cursos = cursos

class Instructor(Usuario):
    def __init__(self, nombre, rol, id, facultad, cursos):
        super().__init__(nombre, rol, id)
        self.__facultad = facultad
        self.cursos = cursos


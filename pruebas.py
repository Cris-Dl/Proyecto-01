class Usuario:
    def __init__(self, nombre, rol, id):
        self.__nombre = nombre
        self.__rol = rol
        self.__id = id

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre


class Estudiante(Usuario):
    def __init__(self, nombre, rol, id, carrera):
        super().__init__(nombre, rol, id)
        self.__carrera = carrera
        self.__cursos = {}

    def inscribir_curso(self, curso):
        if curso not in self.__cursos:
            self.__cursos[curso] = None

    def consultar_notas(self):
        return self.__cursos

    def consultar_cursos(self):
        print(f"Cursos inscritos de {self.nombre}:")
        for curso in self.__cursos:
            print(f"- {curso}")


class Instructor(Usuario):
    def __init__(self, nombre, rol, id, facultad):
        super().__init__(nombre, rol, id)
        self.__facultad = facultad
        self.__cursos = []

    def asignar_curso(self, curso):
        self.__cursos.append(curso)

    def registrar_nota_estudiante(self, estudiante, curso, nota):
        if curso in self.__cursos and curso in estudiante._Estudiante__cursos:
            estudiante._Estudiante__cursos[curso] = nota
            print(f"Nota registrada para {estudiante.nombre} en {curso}: {nota}")
        else:
            print("Error, inténtelo de nuevo")


class FuncionPrograma:
    def __init__(self):
        self.diccionario = {}

    def mostrar_notas(self, estudiante):
        print(f"Notas de {estudiante.nombre}:")
        cursos = estudiante.consultar_notas()
        for curso, nota in cursos.items():
            if nota is not None:
                print(f"{curso}: {nota}")
            else:
                print(f"{curso}: No registrada")


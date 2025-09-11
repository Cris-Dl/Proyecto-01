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

class Curso:
    def __init__(self, nombre, id):
        self.__nombre = nombre
        self.__id = id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre:
            self.__nombre = nuevo_nombre
        else:
            print("El campo no puede estar vacio")

class Informacion:
    def __init__(self):
        super().__init__()
        self.cursos = {}

    def guardar_cursos(self, nombre_curso, datos):
        self.cursos[nombre_curso] = datos

class CrearCurso(Informacion):
    def __init__(self):
        super().__init__()

    def registrar_curso(self):
        nombre_curso = input("Ingrese el nombre del curso: ")
        id_curso = input("Ingresee el ID del curso: ")
        datos_curso = {'nombre': nombre_curso,'ID': id_curso}
        self.guardar_cursos(nombre_curso, datos_curso)
        print(f"Curso '{nombre_curso}' con ID '{id_curso}' ha sido creado exitosamente.")

crear_curso = CrearCurso()
while True:
    print("---- Menú ----")
    print("1. Crear Curso")
    print("2. Administrar Curso")
    print("3. Registrar Usuario (Estudiante/Instructor)")#Realizar sub-menú
    print("4. Asignar Curso Estudiante")
    print("5. Crear Tarea o Evaluación")
    print("6. Registrar nota (Tarea/Evaluación)") #Realizar sub-menú
    print("7. Consultar Curso")
    print("8. Consultar Estudiantes Inscritos")
    print("9. Consultar Tarea o Evaluación") #Realizar sub-menú
    print("10. Consultar Calificaciones")
    print("11. Generar reporte")
    print("12. Salir del programa")
    menu_option = input("Ingrese el número de la opción que quiera ingresar: ")
    print()
    match menu_option:
        case "1":
            print("Crear Curso")
            crear_curso.registrar_curso()
            print()
        case "2":
            print()
        case "3":
            print()
        case "4":
            print()
        case "5":
            print()
        case "6":
            print()
        case "7":
            print()
        case "8":
            print()
        case "9":
            print()
        case "10":
            print()
        case "11":
            print()
        case "12":
            print("Gracias por usar el programa.")
            break
        case _:
            print("Valor invalido. Vuelva a intentar")
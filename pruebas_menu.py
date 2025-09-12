class Usuario:
    def __init__(self, nombre, rol, id):
        super().__init__()
        self.__nombre = nombre
        self.__rol = rol
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

    @property
    def rol(self):
        return self.__rol

    @rol.setter
    def rol(self, nuevo_rol):
        if nuevo_rol:
            self.__rol = nuevo_rol
        else:
            print("El campo no puede estar vacio")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nuevo_id):
        if nuevo_id:
            self.__id = nuevo_id
        else:
            print("El campo no puede estar vacio")

class Estudiante(Usuario):
    def __init__(self, nombre, rol, id, carrera, cursos):
        super().__init__(nombre, rol, id)
        self.__carrera = carrera
        self.__cursos = cursos

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, nueva_carrera):
        if nueva_carrera:
            self.__carrera = nueva_carrera
        else:
            print("El campo no puede estar vacio")

    @property
    def cursos(self):
        return self.__cursos

    @cursos.setter
    def cursos(self, nuevos_cursos):
        if nuevos_cursos:
            self.__cursos = nuevos_cursos
        else:
            print("El campo no puede estar vacio")

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
        self.usuarios = {}

    def guardar_cursos(self, nombre_curso, datos):
        self.cursos[nombre_curso] = datos

    def guardar_usuarios(self, id, datos):
        self.usuarios[id] = datos

class CrearCurso(Informacion):
    def __init__(self, manejo):
        super().__init__()
        self.manejo = manejo

    def registrar_curso(self):
        nombre_curso = input("Ingrese el nombre del curso: ")
        id_curso = input("Ingresee el ID del curso: ")
        datos_curso = {'nombre': nombre_curso,'ID': id_curso}
        self.manejo.guardar_cursos(nombre_curso, datos_curso)
        print(f"Curso '{nombre_curso}' con ID '{id_curso}' ha sido creado exitosamente.")

class CrearUsuario:
    def __init__(self, manejo):
        super().__init__()
        self.manejo = manejo

    def registrar_estudiante(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        rol = "Estudiante"
        id = input("Ingrese el carnet del estudiante: ")
        carrera = input("Ingrese la carrera que pertenece el estudiante: ")
        cursos_inscritos = []
        nuevo_estudiante = Estudiante(nombre, rol, id, carrera, cursos_inscritos)
        self.manejo.guardar_usuarios(id, {'nombre': nuevo_estudiante.id,'rol': nuevo_estudiante.rol,'carrera': nuevo_estudiante.carrera,'cursos': nuevo_estudiante.cursos})
        print(f"\nEstudiante '{nombre}' registrado con éxito.")

    def registrar_instructor(self):


manejo = Informacion()
crear_curso = CrearCurso(manejo)
crear_usuario = CrearUsuario(manejo)
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
            print("Registrar Usuario")
            print("1. Registrar Estudiante")
            print("2. Registrar Instructor")
            print("3. Cancelar Registro")
            menu_option2 = input("Ingrese el número de la opción que quiera reealizar: ")
            print()
            match menu_option2:
                case "1":
                    print("Registrar Estudiante")
                    crear_usuario.registrar_estudiante()
                    print()
                case "2":
                    print("Registrar Instructor")
                case "3":
                    print("Se ha cancelado el registro")
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
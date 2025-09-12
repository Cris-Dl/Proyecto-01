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
        self.__cursos = cursos

    @property
    def facultad(self):
        return self.__facultad

    @facultad.setter
    def facultad(self, nueva_facultad):
        if nueva_facultad:
            self.__facultad = nueva_facultad
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
        self.actividades = {}

    def guardar_cursos(self, nombre_curso, datos):
        self.cursos[nombre_curso] = datos

    def guardar_usuarios(self, id, datos):
        self.usuarios[id] = datos

    def guardar_actividades(self, nombre, datos):
        self.actividades[nombre] = datos

class CrearCurso:
    def __init__(self, manejo):
        super().__init__()
        self.manejo = manejo

    def registrar_curso(self):
        while True:
            try:
                nombre_curso = input("Ingrese el nombre del curso: ")
                if not nombre_curso.strip():
                    raise ValueError ("El nombre no puede quedar vacio \n")
            except ValueError as e:
                print(f"Error: {e}")
            else:
                break
        while True:
            try:
                id_curso = input("Ingresee el ID del curso: ")
                if not  id_curso.strip():
                    raise  ValueError ("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}")
            else:
                break
        datos_curso = {'nombre': nombre_curso, 'ID': id_curso}
        self.manejo.guardar_cursos(id_curso, datos_curso)
class CrearUsuario:
    def __init__(self, manejo):
        super().__init__()
        self.manejo = manejo

    def registrar_estudiante(self):
        while True:
            try:
                nombre = input("Ingrese el nombre del estudiante: ")
                if not nombre.strip():
                    raise ValueError("El nombre no puede quedar vacio \n")
            except ValueError as e:
                print(f"Error: {e}")
            else:
                break
        rol = "Estudiante"
        while True:
            try:
                id = input("Ingrese el carnet del estudiante: ")
                if not id.strip():
                    raise ValueError("El id no puede quedar vacio \n")
            except ValueError as e:
                print(f"Error: {e}")
            else:
                break
        while True:
            try:
                carrera = input("Ingrese la carrera que pertenece el estudiante: ")
                if not carrera.strip():
                    raise ValueError ("La carrera no puede quedar vacia \n")
            except ValueError as e:
                print(f"Error: {e}")
            else:
                break
        cursos_inscritos = []
        nuevo_estudiante = Estudiante(nombre, rol, id, carrera, cursos_inscritos)
        self.manejo.guardar_usuarios(id, {'nombre': nuevo_estudiante.nombre,'rol': nuevo_estudiante.rol,'carrera': nuevo_estudiante.carrera,'cursos': nuevo_estudiante.cursos})
        print(f"\nEstudiante '{nombre}' registrado con éxito.")

    def registrar_instructor(self):
        nombre = input("Ingrese el nombre del instructor: ")
        rol = "Instructor"
        id = input("Ingrese el ID del instructor: ")
        facultad = input("Ingrese el nombre de la facultad que pertenece el instructor: ")
        cursos_asignados = []
        nuevo_instructor = Instructor(nombre, rol, id, facultad, cursos_asignados)
        self.manejo.guardar_usuarios(id, {'nombre': nuevo_instructor.nombre,'rol': nuevo_instructor.rol,'facultad': nuevo_instructor.facultad,'cursos':nuevo_instructor.cursos})
        print(f"\nInstructor '{nombre}' registrado con éxito.")

class AsignarCurso:
    def __init__(self, manejo):
        self.manejo = manejo

    def asignar_curso(self):
        id_busqueda = input("Ingrese el carnet del estudiante a asignar: ")
        if id_busqueda not in self.manejo.usuarios:
            print("Error: El estudiante con ese carnet no existe.")
            return
        print("\nCursos disponibles:")
        if not self.manejo.cursos:
            print("No hay cursos disponibles para asignar.")
            return
        for curso_id, curso_info in self.manejo.cursos.items():
            print(f"- ID: {curso_id} | Nombre: {curso_info['nombre']}")
        curso_ids_str = input("\nIngrese los IDs de los cursos a asignar (separados por comas): ")
        cursos = [id.strip() for id in curso_ids_str.split(',') if id.strip()]
        estudiante = self.manejo.usuarios[id_busqueda]
        cursos_asignados = []
        for curso_id in cursos:
            if curso_id in self.manejo.cursos:
                if curso_id not in estudiante['cursos']:
                    estudiante['cursos'].append(curso_id)
                    cursos_asignados.append(self.manejo.cursos[curso_id]['nombre'])
                else:
                    print(f"Advertencia: El estudiante ya está inscrito en el curso con ID {curso_id}.")
            else:
                print(f"Error: El curso con ID {curso_id} no existe.")
        print(f"\nSe han asignado {len(cursos_asignados)} curso(s) exitosamente a {estudiante['nombre']}.")
        if cursos_asignados:
            print(f"Cursos asignados: {', '.join(cursos_asignados)}")

class CrearActividad:
    def __init__(self, manejo):
        self.manejo = manejo

    def crear_tarea(self):
        print("Cursos disponibles:")
        if not self.manejo.cursos:
            print("No hay cursos para asignar tareas.")
            return
        for id, curso in self.manejo.cursos.items():
            print(f"- ID: {id} | Nombre: {curso['nombre']}")
        curso_id = input("\nIngrese el ID del curso al que pertenece la tarea: ")
        if curso_id not in self.manejo.cursos:
            print(f"Error: El curso con ID {curso_id} no existe.")
            return
        nombre_tarea = input("Ingrese el nombre de la tarea: ")
        descripcion_tarea = input("Describa el contenido de la tarea: ")
        tarea_info = {'nombre': nombre_tarea, 'descripcion': descripcion_tarea, 'curso_id': curso_id}
        clave_actividad = f"{curso_id}-{nombre_tarea}"
        self.manejo.guardar_actividades(clave_actividad, tarea_info)
        print(f"\nTarea '{nombre_tarea}' creada exitosamente y asignada al curso '{self.manejo.cursos[curso_id]['nombre']}'.")

manejo = Informacion()
crear_curso = CrearCurso(manejo)
crear_usuario = CrearUsuario(manejo)
asignar_curso = AsignarCurso(manejo)
asignar_actividad = CrearActividad(manejo)
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
                    crear_usuario.registrar_instructor()
                    print()
                case "3":
                    print("Se ha cancelado el registro")
                    print()
        case "4":
            print("Asignar Curso")
            asignar_curso.asignar_curso()
            print()
        case "5":
            print("Crear Tarea o Evaluación")
            print("1. Crear Tarea")
            print("2. Crear Evaluación")
            print("3. Cancelar Creación")
            menu_option3 = input("Ingrese el número de la opción que quiera realizar: ")
            print()
            match menu_option3:
                case "1":
                    print("Crear Tarea")
                    asignar_actividad.crear_tarea()
                    print()
                case "2":
                    print("Crear Evaluación")
                case "3":
                    print("Cancelando creación de actividad")
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
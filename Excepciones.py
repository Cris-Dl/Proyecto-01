import datetime
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
    def __init__(self, nombre, rol, id, carrera, cursos, reportes):
        super().__init__(nombre, rol, id)
        self.__carrera = carrera
        self.__cursos = cursos
        self.__reporte = reportes

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

    @property
    def reportes(self):
        return self.__reporte

    @reportes.setter
    def reportes(self, nuevo_reporte):
        if nuevo_reporte:
            self.__reporte = nuevo_reporte
        else:
            print("El campo no puede estar vacio")

    def mostrar_info(self):
        print(f"Nombre del estudiante: {self.nombre}")
        print(f"Carnet: {self.id}")
        print(f"Carrera: {self.carrera}")
        print(f"Cursos: {self.cursos}")
        print(f"Reportes: {self.reportes}")

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

    def mostrar_info(self):
        print(f"Nombre del Instructor: {self.nombre}")
        print(f"Cargo: {self.rol}")
        print(f"ID: {self.id}")
        print(f"Facultad: {self.facultad}")
        print(f"Cursos acargos: {self.cursos}")


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
        self.notas = {}

    def guardar_cursos(self, nombre_curso, datos):
        self.cursos[nombre_curso] = datos

    def guardar_usuarios(self, id, datos):
        self.usuarios[id] = datos

    def guardar_actividades(self, nombre, datos):
        self.actividades[nombre] = datos

    def guardar_notas(self, clave, datos):
        self.notas[clave] = datos

class CrearCurso:
    def __init__(self, manejo):
        super().__init__()
        self.manejo = manejo

    def registrar_curso(self):
        while True:
            try:
                nombre_curso = input("Ingrese el nombre del curso: ")
                if not nombre_curso.strip():
                    raise ValueError("El nombre no puede quedar vacio")
            except ValueError as e:
                print(f"Erro: {e}")
            else:
                break
        while True:
            try:
                id_curso = input("Ingresee el ID del curso: ")
                if not id_curso.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Erro: {e}")
            else:
                break
        datos_curso = {'nombre': nombre_curso, 'ID': id_curso}
        self.manejo.guardar_cursos(id_curso, datos_curso)
        print(f"Curso '{nombre_curso}' con ID '{id_curso}' ha sido creado exitosamente.")


class AdministrarCurso:
    def __init__(self, manejo):
        self.manejo = manejo

    def eliminar_usuario(self):
        print("Cursos disponibles:")
        if not self.manejo.cursos:
            print("No hay cursos creados.")
            return
        for id, curso in self.manejo.cursos.items():
            print(f"- ID: {id} | Nombre: {curso['nombre']}")
        id_curso = input("\nIngrese el ID del curso del que desea eliminar a un usuario: ")

        if id_curso not in self.manejo.cursos:
            print("Error: El curso con ese ID no existe.")
            return
        print("\nUsuarios inscritos en el curso:")
        usuarios_en_curso = []
        for id_usuario, info_usuario in self.manejo.usuarios.items():
            if id_curso in info_usuario['cursos']:
                usuarios_en_curso.append((id_usuario, info_usuario['nombre']))
        if not usuarios_en_curso:
            print("No hay usuarios inscritos en este curso.")
            return
        for id_usuario, nombre_usuario in usuarios_en_curso:
            print(f"- {nombre_usuario} (ID: {id_usuario})")
        id_usuario = input("\nIngrese el ID del usuario que desea eliminar del curso: ")
        if id_usuario not in self.manejo.usuarios:
            print("Error: El usuario con ese ID no existe.")
            return
        if id_curso in self.manejo.usuarios[id_usuario]['cursos']:
            self.manejo.usuarios[id_usuario]['cursos'].remove(id_curso)
            print(
                f"El usuario '{self.manejo.usuarios[id_usuario]['nombre']}' ha sido eliminado del curso '{self.manejo.cursos[id_curso]['nombre']}' exitosamente.")
        else:
            print("Error: El usuario no está inscrito en este curso.")

    def cambiar_nombre(self):
        print("Cursos disponibles:")
        if not self.manejo.cursos:
            print("No hay cursos creados.")
            return
        for id, curso in self.manejo.cursos.items():
            print(f"- ID: {id} | Nombre: {curso['nombre']}")
        id_curso = input("\nIngrese el ID del curso al que desea cambiar el nombre: ")
        if id_curso not in self.manejo.cursos:
            print("Error: El curso con ese ID no existe.")
            return
        nuevo_nombre = input("Ingrese el nuevo nombre para el curso: ")
        self.manejo.cursos[id_curso]['nombre'] = nuevo_nombre
        print(f"El nombre del curso con ID '{id_curso}' ha sido cambiado a '{nuevo_nombre}' exitosamente.")

    def cambiar_id(self):
        print("Cursos disponibles:")
        if not self.manejo.cursos:
            print("No hay cursos creados.")
            return
        for id, curso in self.manejo.cursos.items():
            print(f"- ID: {id} | Nombre: {curso['nombre']}")
        id_actual = input("\nIngrese el ID actual del curso: ")
        if id_actual not in self.manejo.cursos:
            print("Error: El curso con ese ID no existe.")
            return
        nuevo_id = input("Ingrese el nuevo ID para el curso: ")
        if nuevo_id in self.manejo.cursos:
            print("Error: Ya existe un curso con ese ID.")
            return
        curso_datos = self.manejo.cursos[id_actual].copy()
        curso_datos['ID'] = nuevo_id
        self.manejo.cursos[nuevo_id] = curso_datos
        for usuario in self.manejo.usuarios.values():
            if id_actual in usuario['cursos']:
                usuario['cursos'].remove(id_actual)
                usuario['cursos'].append(nuevo_id)
        for actividad in self.manejo.actividades.values():
            if actividad['curso_id'] == id_actual:
                actividad['curso_id'] = nuevo_id
        actividades_a_cambiar = {}
        for clave, actividad in self.manejo.actividades.items():
            partes = clave.split("-", 1)  # Divide en máximo 2 partes
            if len(partes) == 2 and partes[0] == id_actual:
                nueva_clave = nuevo_id + "-" + partes[1]
                actividades_a_cambiar[clave] = nueva_clave
        for clave_vieja, clave_nueva in actividades_a_cambiar.items():
            self.manejo.actividades[clave_nueva] = self.manejo.actividades[clave_vieja]
            del self.manejo.actividades[clave_vieja]
        del self.manejo.cursos[id_actual]
        print(f"El ID del curso ha sido cambiado de '{id_actual}' a '{nuevo_id}' exitosamente.")

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
        reportes = []
        nuevo_estudiante = Estudiante(nombre, rol, id, carrera, cursos_inscritos, reportes)
        self.manejo.guardar_usuarios(id, {'nombre': nuevo_estudiante.nombre,'rol': nuevo_estudiante.rol,'carrera': nuevo_estudiante.carrera,'cursos': nuevo_estudiante.cursos,'reportes': nuevo_estudiante.reportes})
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
        id_busqueda = input("Ingrese el carnet del (Estudiante/Instructor) a asignar: ")
        if id_busqueda not in self.manejo.usuarios:
            print("Error: El usuario con ese carnet no existe.")
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
                    print(f"Advertencia: El usuario ya está inscrito en el curso con ID {curso_id}.")
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
        nombre_tarea = input("Ingrese el nombre de la tarea: ").upper()
        descripcion_tarea = input("Describa el contenido de la tarea: ")
        tarea_info = {'nombre': nombre_tarea, 'descripcion': descripcion_tarea, 'curso_id': curso_id}
        clave_actividad = f"{curso_id}-{nombre_tarea}"
        self.manejo.guardar_actividades(clave_actividad, tarea_info)
        print(f"\nTarea '{nombre_tarea}' creada exitosamente y asignada al curso '{self.manejo.cursos[curso_id]['nombre']}'.")

    def crear_evaluacion(self):
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
        nombre_evaluacion = input("Ingrese el nombre del tipo de evaluación: ").upper()
        descripcion_evaluacion = input("Describa el contenido de la evalución: ")
        tarea_info = {'nombre': nombre_evaluacion, 'descripcion': descripcion_evaluacion, 'curso_id': curso_id}
        clave_actividad = f"{curso_id}-{nombre_evaluacion}"
        self.manejo.guardar_actividades(clave_actividad, tarea_info)
        print(
            f"\nTarea '{nombre_evaluacion}' creada exitosamente y asignada al curso '{self.manejo.cursos[curso_id]['nombre']}'.")

class AsignarNota:
    def __init__(self, manejo):
        self.manejo = manejo

    def asignar_nota(self):
        print("Cursos disponibles:")
        if not self.manejo.cursos:
            print("No hay cursos creados para asignar notas.")
            return
        for id, curso in self.manejo.cursos.items():
            print(f"- ID: {id} | Nombre: {curso['nombre']}")
        id_curso = input("\nIngrese el ID del curso: ")
        if id_curso not in self.manejo.cursos:
            print("Error: El curso no existe.")
            return
        actividades = [info for info in self.manejo.actividades.values() if info['curso_id'] == id_curso]
        if not actividades:
            print("No hay tareas o evaluaciones creadas para este curso.")
            return
        print("\nActividades disponibles en el curso:")
        for actividad in actividades:
            print(f"- {actividad['nombre']} ({actividad['descripcion']})")
        nombre_actividad = input("\nIngrese el nombre de la actividad a calificar: ").upper()
        clave = f"{id_curso}-{nombre_actividad}"
        if clave not in self.manejo.actividades:
            print("Error: La actividad no se encontró en este curso.")
            return
        estudiantes_inscritos = [estudiante_info for estudiante_info in self.manejo.usuarios.values()  if estudiante_info['rol'] == 'Estudiante' and id_curso in estudiante_info['cursos']]
        if not estudiantes_inscritos:
            print("No hay estudiantes inscritos en este curso.")
            return
        print(f"\nAsignando notas para la actividad '{nombre_actividad}':")
        for estudiante in estudiantes_inscritos:
            try:
                id_estudiante = None
                for clave, valor in self.manejo.usuarios.items():
                    if valor == estudiante:
                        id_estudiante = clave
                        break
                nota = float(input(f"  > Ingrese la nota para {estudiante['nombre']}: "))
                clave_nota = f"{id_estudiante}-{clave}"
                self.manejo.guardar_notas(clave_nota, {'nota': nota, 'id_estudiante': id_estudiante,'nombre_actividad': nombre_actividad})
                print(f"Nota de {nota} registrada para {estudiante['nombre']}.")
            except ValueError:
                print("Error: La nota debe ser un número. Saltando a la siguiente nota.")

class ConsultarCurso:
    def __init__(self, manejo):
        self.manejo = manejo

    def consultar_curso(self):
        print("Cursos disponibles:")
        if not self.manejo.cursos:
            print("No hay cursos registrados.")
            return
        for id, curso in self.manejo.cursos.items():
            print(f"- ID: {id} | Nombre: {curso['nombre']}")
        id_curso = input("\nIngrese el ID del curso que desea consultar: ")
        if id_curso not in self.manejo.cursos:
            print("Error: El curso con ese ID no existe.")
            return
        print(f"\n--- Información del Curso: {self.manejo.cursos[id_curso]['nombre']} ---")
        instructor_encontrado = None
        for usuario_id, usuario_info in self.manejo.usuarios.items():
            if usuario_info['rol'] == 'Instructor' and id_curso in usuario_info['cursos']:
                instructor_encontrado = usuario_info
                break
        if instructor_encontrado:
            print(f"Instructor: {instructor_encontrado['nombre']}")
        else:
            print("Instructor: Aún no se ha asignado un instructor a este curso.")
        estudiantes_inscritos = [
            usuario_info['nombre']
            for usuario_info in self.manejo.usuarios.values()
            if usuario_info['rol'] == 'Estudiante' and id_curso in usuario_info['cursos']]
        print("\nEstudiantes inscritos:")
        if estudiantes_inscritos:
            for estudiante in estudiantes_inscritos:
                print(f"- {estudiante}")
        else:
            print("No hay estudiantes inscritos en este curso.")


class ConsultarEstudiantes:
    def __init__(self, manejo):
        self.manejo = manejo

    def consultar_estudiantes(self):
        print("Cursos disponibles:")
        if not self.manejo.cursos:
            print("No hay cursos registrados.")
            return

        for id, curso in self.manejo.cursos.items():
            print(f"- ID: {id} | Nombre: {curso['nombre']}")

        id_curso = input("\nIngrese el ID del curso para ver los estudiantes inscritos: ")
        if id_curso not in self.manejo.cursos:
            print("Error: El curso con ese ID no existe.")
            return

        estudiantes = []
        for id, datos in self.manejo.usuarios.items():
            if datos['rol'] == 'Estudiante' and id_curso in datos['cursos']:
                estudiantes.append((id, datos['nombre']))

        print(f"\n--- Estudiantes inscritos en el curso '{self.manejo.cursos[id_curso]['nombre']}' ---")
        if estudiantes:
            for carnet, nombre in estudiantes:
                print(f"- {nombre} (Carnet: {carnet})")
        else:
            print("No hay estudiantes inscritos en este curso.")

class ConsultarCalificaciones:
    def __init__(self, manejo):
        self.manejo = manejo

    def consultar_calificaciones(self):
        estudiantes = []
        for id, datos in self.manejo.usuarios.items():
            if datos['rol'] == 'Estudiante':
                estudiantes.append((id, datos['nombre']))
        if not estudiantes:
            print("No hay estudiantes registrados.")
            return

        print("Estudiantes registrados:")
        for id, nombre in estudiantes:
            print(f"- {nombre} (Carnet: {id})")

        id_estudiante = input("\nIngrese el carnet del estudiante: ")
        if id_estudiante not in self.manejo.usuarios or self.manejo.usuarios[id_estudiante]['rol'] != 'Estudiante':
            print("Estudiante no encontrado.")
            return

        print(f"\n--- Calificaciones de {self.manejo.usuarios[id_estudiante]['nombre']} ---")
        notas_encontradas = False
        for clave, datos_nota in self.manejo.notas.items():
            if datos_nota['id_estudiante'] == id_estudiante:
                print(f"{datos_nota['nombre_actividad']}: {datos_nota['nota']}")
                notas_encontradas = True

        if not notas_encontradas:
            print("No hay calificaciones registradas para este estudiante.")

class ConsultarActividad:
    def __init__(self, manejo):
        self.manejo = manejo

    def consultar_actividad(self):
        print("Cursos disponibles:")
        if not self.manejo.cursos:
            print("No hay cursos registrados.")
            return
        for id, curso in self.manejo.cursos.items():
            print(f"- ID: {id} | Nombre: {curso['nombre']}")
        id_curso = input("\nIngrese el ID del curso para ver sus actividades: ")
        if id_curso not in self.manejo.cursos:
            print("Error: El curso con ese ID no existe.")
            return
        actividades_encontradas = [actividad for actividad in self.manejo.actividades.values() if actividad['curso_id'] == id_curso]
        print(f"\n--- Actividades del curso '{self.manejo.cursos[id_curso]['nombre']}' ---")
        if actividades_encontradas:
            for actividad in actividades_encontradas:
                print(f"  - Nombre: {actividad['nombre']}")
                print(f"    Descripción: {actividad['descripcion']}")
        else:
            print("No hay actividades registradas para este curso.")

class Reportes:
    def __init__(self, manejo):
        self.manejo = manejo

    def registrar_reporte(self):
        estudiantes = []
        for id, datos in self.manejo.usuarios.items():
            if datos['rol'] == 'Estudiante':
                estudiantes.append((id, datos['nombre']))
        if not estudiantes:
            print("No hay estudiantes registrados.")
            return
        print("\nEstudiantes disponibles:")
        for id, nombre in estudiantes:
            print(f"- {nombre} (Carnet: {id})")
        id_estudiante = input("\nIngrese el carnet del estudiante para generar el reporte: ")
        if id_estudiante not in self.manejo.usuarios or self.manejo.usuarios[id_estudiante]['rol'] != 'Estudiante':
            print("Error: Estudiante no encontrado.")
            return
        estudiante_info = self.manejo.usuarios[id_estudiante]
        print("\n--- Generando Reporte Descriptivo para el Estudiante ---")
        print(f"Nombre: {estudiante_info['nombre']}")
        print(f"ID/Carnet: {id_estudiante}")
        print(f"Carrera: {estudiante_info['carrera']}")
        print("\nCursos Inscritos:")
        if estudiante_info['cursos']:
            for curso_id in estudiante_info['cursos']:
                nombre_curso = self.manejo.cursos[curso_id]['nombre']
                print(f"  - {nombre_curso} (ID: {curso_id})")
        else:
            print("  No está inscrito en ningún curso.")
        descripcion_reporte = input("\nPor favor, ingrese una descripción del desempeño del estudiante:\n")
        reporte_guardar = {'fecha': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'descripcion': descripcion_reporte}
        estudiante_info['reportes'].append(reporte_guardar)
        print("\nReporte descriptivo generado y guardado con éxito.")

class VerInfo:
    def __init__(self, manejo):
        self.manejo = manejo

    def ver_informacion(self):
        id_busqueda = input("Ingrese el ID o carnet del usuario a consultar: ")
        if id_busqueda not in self.manejo.usuarios:
            print("Error: El usuario no existe en la base de datos.")
            return
        usuario_info = self.manejo.usuarios[id_busqueda]
        nombre = usuario_info['nombre']
        rol = usuario_info['rol']
        if rol == "Estudiante":
            carrera = usuario_info['carrera']
            cursos = usuario_info['cursos']
            reportes = usuario_info['reportes']
            estudiante = Estudiante(nombre, rol, id_busqueda, carrera, cursos, reportes)
            estudiante.mostrar_info()
        elif rol == "Instructor":
            facultad = usuario_info['facultad']
            cursos = usuario_info['cursos']
            instructor = Instructor(nombre, rol, id_busqueda, facultad, cursos)
            instructor.mostrar_info()
        else:
            print("Rol de usuario no reconocido.")

manejo = Informacion()
crear_curso = CrearCurso(manejo)
crear_usuario = CrearUsuario(manejo)
asignar_curso = AsignarCurso(manejo)
asignar_actividad = CrearActividad(manejo)
asignar_nota = AsignarNota(manejo)
consultar_curso = ConsultarCurso(manejo)
consultar_estudiantes = ConsultarEstudiantes(manejo)
consultar_calificaciones = ConsultarCalificaciones(manejo)
consultar_actividad = ConsultarActividad(manejo)
crear_reporte = Reportes(manejo)
administrar_cursos = AdministrarCurso(manejo)
ver_informacion = VerInfo(manejo)
while True:
    print("---- Menú ----")
    print("1. Crear Curso")
    print("2. Administrar Curso")
    print("3. Registrar Usuario (Estudiante/Instructor)")#Realizar sub-menú
    print("4. Asignar Curso (Estudiante/Instructor)")
    print("5. Crear Tarea o Evaluación")
    print("6. Registrar nota (Tarea/Evaluación)") #Realizar sub-menú
    print("7. Consultar Curso")
    print("8. Consultar Estudiantes Inscritos")
    print("9. Consultar Tarea o Evaluación") #Realizar sub-menú
    print("10. Consultar Calificaciones")
    print("11. Generar reporte")
    print("12. Ver Información (Estudiante/Instructor)")
    print("13. Salir del programa")
    menu_option = input("Ingrese el número de la opción que quiera ingresar: ")
    print()
    match menu_option:
        case "1":
            print("Crear Curso")
            crear_curso.registrar_curso()
            print()
        case "2":
            print("Administrar Curso")
            print("1. Eliminar Estudiante/Instructor")
            print("2. Cambiar nombre al curso")
            print("3 Cambiar ID al curso")
            print("4. Cancelar administración")
            menu_option4 = input("Ingrese el número de la opción que quiera realizar: ")
            print()
            match menu_option4:
                case "1":
                    print("Eliminar Estudiante/Instructor")
                    administrar_cursos.eliminar_usuario()
                    print()
                case "2":
                    print("Cambiar nombre al curso")
                    administrar_cursos.cambiar_nombre()
                    print()
                case "3":
                    print("Cambiar ID al curso")
                    administrar_cursos.cambiar_id()
                    print()
                case "4":
                    print("Cancelando intento administrativo")
        case "3":
            print("Registrar Usuario")
            print("1. Registrar Estudiante")
            print("2. Registrar Instructor")
            print("3. Cancelar Registro")
            menu_option2 = input("Ingrese el número de la opción que quiera realizar: ")
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
                    asignar_actividad.crear_evaluacion()
                    print()
                case "3":
                    print("Cancelando creación de actividad")
        case "6":
            print("Asignar nota")
            asignar_nota.asignar_nota()
            print()
        case "7":
            print("Consultar Curso")
            consultar_curso.consultar_curso()
            print()
        case "8":
            print("Consultar Estudiantes Inscritos")
            consultar_estudiantes.consultar_estudiantes()
            print()
        case "9":
            print("Consultar Tarea/Evaluación")
            consultar_actividad.consultar_actividad()
            print()
        case "10":
            print("Consultar calificaciones")
            consultar_calificaciones.consultar_calificaciones()
            print()
        case "11":
            print("Generar reporte")
            crear_reporte.registrar_reporte()
            print()
        case "12":
            print("Ver información")
            ver_informacion.ver_informacion()
            print()
        case "13":
            print("Gracias por usar el programa.")
            break
        case _:
            print("Valor invalido. Vuelva a intentar")
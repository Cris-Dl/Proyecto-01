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

class Confirmacion:
    def __init__(self):
        self.respuesta = None

    def pedir_confirmacion(self, mensaje):
        while True:
            respuesta = input(f"{mensaje} (s/n): ").strip().lower()
            if respuesta == "s":
                self.respuesta = True
                return True
            elif respuesta == "n":
                self.respuesta = False
                return False
            else:
                print("Respuesta inválida. Escribe 's' para sí o 'n' para no.")
class CrearCurso:
    contador_curso = 0
    def __init__(self, manejo):
        super().__init__()
        self.manejo = manejo

    def registrar_curso(self):
        CrearCurso.contador_curso += 2
        while True:
            try:
                nombre_curso = input("Ingrese el nombre del curso: ")
                if not nombre_curso.strip():
                    raise ValueError("El nombre no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        letra = str(CrearCurso.contador_curso)
        id_curso = "CUR" + letra
        datos_curso = {'nombre': nombre_curso, 'ID': id_curso}
        self.manejo.guardar_cursos(id_curso, datos_curso)
        print(f"Curso '{nombre_curso}' con ID '{id_curso}' ha sido creado exitosamente.")


class AdministrarCurso:
    def __init__(self, manejo):
        self.manejo = manejo
        self.confirmacion = Confirmacion()

    def eliminar_usuario(self):
        print("Cursos disponibles:")
        if not self.manejo.cursos:
            print("No hay cursos creados.")
            return
        for id, curso in self.manejo.cursos.items():
            print(f"- ID: {id} | Nombre: {curso['nombre']}")
        while True:
            try:
                id_curso = input("\nIngrese el ID del curso del que desea eliminar a un usuario: ")
                if not id_curso.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
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
        while True:
            try:
                id_usuario = input("\nIngrese el ID del usuario que desea eliminar del curso: ")
                if not id_usuario.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e} \n")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        if id_usuario not in self.manejo.usuarios:
            print("Error: El usuario con ese ID no existe.")
            return
        nombre_usuario = self.manejo.usuarios[id_usuario]['nombre']
        nombre_curso = self.manejo.cursos[id_curso]['nombre']
        mensaje = f"¿Está seguro que desea eliminar a '{nombre_usuario}' del curso '{nombre_curso}'? Esta acción no se puede deshacer"

        if not self.confirmacion.pedir_confirmacion(mensaje):
            print("Operación cancelada.")
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
        while True:
            try:
                id_curso = input("\nIngrese el ID del curso al que desea cambiar el nombre: ")
                if not id_curso.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        if id_curso not in self.manejo.cursos:
            print("Error: El curso con ese ID no existe.")
            return
        while True:
            try:
                nuevo_nombre = input("Ingrese el nuevo nombre para el curso: ")
                if not nuevo_nombre.strip():
                    raise ValueError("El nombre no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        mensaje = f"¿Está seguro que desea cambiar el nombre del curso a '{nuevo_nombre}'?"

        if not self.confirmacion.pedir_confirmacion(mensaje):
            print("Operación cancelada.")
            return
        self.manejo.cursos[id_curso]['nombre'] = nuevo_nombre
        print(f"El nombre del curso con ID '{id_curso}' ha sido cambiado a '{nuevo_nombre}' exitosamente.")

    def cambiar_id(self):
        print("Cursos disponibles:")
        if not self.manejo.cursos:
            print("No hay cursos creados.")
            return
        for id, curso in self.manejo.cursos.items():
            print(f"- ID: {id} | Nombre: {curso['nombre']}")
        while True:
            try:
                id_actual = input("\nIngrese el ID actual del curso: ")
                if not id_actual.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        if id_actual not in self.manejo.cursos:
            print("Error: El curso con ese ID no existe.")
            return
        while True:
            try:
                nuevo_id = input("Ingrese el nuevo ID para el curso: ")
                if not nuevo_id.strip():
                    raise ValueError("El id no puede quedar vacio ")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        if nuevo_id in self.manejo.cursos:
            print("Error: Ya existe un curso con ese ID.")
            return

        nombre_curso = self.manejo.cursos[id_actual]['nombre']
        mensaje = f"¿Está seguro que desea cambiar el ID del curso '{nombre_curso}' de '{id_actual}' a '{nuevo_id}'? Esta operación actualizará todas las referencias y no se puede deshacer"

        if not self.confirmacion.pedir_confirmacion(mensaje):
            print("Operación cancelada.")
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
    contador_estudiante = 991
    contador_instructor = 100
    def __init__(self, manejo):
        super().__init__()
        self.manejo = manejo

    def registrar_estudiante(self):
        CrearUsuario.contador_estudiante += 9
        while True:
            try:
                nombre = input("Ingrese el nombre del estudiante: ")
                if not nombre.strip():
                    raise ValueError("El nombre no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        rol = "Estudiante"
        while True:
            try:
                carrera = input("Ingrese la carrera que pertenece el estudiante: ")
                if not carrera.strip():
                    raise ValueError("El nombre de la carrera no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        letra = str(CrearUsuario.contador_estudiante)
        id = "EST" + letra
        cursos_inscritos = []
        reportes = []
        nuevo_estudiante = Estudiante(nombre, rol, id, carrera, cursos_inscritos, reportes)
        self.manejo.guardar_usuarios(id, {'nombre': nuevo_estudiante.nombre,'rol': nuevo_estudiante.rol,'carrera': nuevo_estudiante.carrera,'cursos': nuevo_estudiante.cursos,'reportes': nuevo_estudiante.reportes})
        print(f"\nEstudiante '{nombre}' con el ID {id} registrado con éxito.")

    def registrar_instructor(self):
        CrearUsuario.contador_instructor += 5
        while True:
            try:
                nombre = input("Ingrese el nombre del instructor: ")
                if not nombre.strip():
                    raise ValueError("El nombre no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        rol = "Instructor"
        while True:
            try:
                facultad = input("Ingrese el nombre de la facultad que pertenece el instructor: ")
                if not facultad.strip():
                    raise ValueError("El nombre de la facultad no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        letra = str(CrearUsuario.contador_instructor)
        id = "CAT" + letra
        cursos_asignados = []
        nuevo_instructor = Instructor(nombre, rol, id, facultad, cursos_asignados)
        self.manejo.guardar_usuarios(id, {'nombre': nuevo_instructor.nombre,'rol': nuevo_instructor.rol,'facultad': nuevo_instructor.facultad,'cursos':nuevo_instructor.cursos})
        print(f"\nInstructor '{nombre}' con el ID {id} registrado con éxito.")

class AsignarCurso:
    def __init__(self, manejo):
        self.manejo = manejo

    def asignar_curso(self):
        while True:
            try:
                id_busqueda = input("Ingrese el carnet del (Estudiante/Instructor) a asignar: ").upper()
                if not id_busqueda.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        if id_busqueda not in self.manejo.usuarios:
            print("Error: El usuario con ese carnet no existe.")
            return
        print("\nCursos disponibles:")
        if not self.manejo.cursos:
            print("No hay cursos disponibles para asignar.")
            return
        for curso_id, curso_info in self.manejo.cursos.items():
            print(f"- ID: {curso_id} | Nombre: {curso_info['nombre']}")
        curso_ids_str = input("\nIngrese los IDs de los cursos a asignar (separados por comas): ").upper()
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
        while True:
            try:
                curso_id = input("\nIngrese el ID del curso al que pertenece la tarea: ").upper()
                if not curso_id.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        if curso_id not in self.manejo.cursos:
            print(f"Error: El curso con ID {curso_id} no existe.")
            return
        while True:
            try:
                nombre_tarea = input("Ingrese el nombre de la tarea: ").upper()
                if not nombre_tarea.strip():
                    raise ValueError("El nombre de la tarea no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        while True:
            try:
                descripcion_tarea = input("Describa el contenido de la tarea: ")
                if not descripcion_tarea.strip():
                    raise ValueError("La descripcion no puede quedar vacia")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        tarea_info = {'nombre': nombre_tarea, 'descripcion': descripcion_tarea, 'curso_id': curso_id}
        clave_actividad = f"{curso_id}-{nombre_tarea}"
        self.manejo.guardar_actividades(clave_actividad, tarea_info)
        print(f"\nTarea '{nombre_tarea}' creada exitosamente y asignada al curso '{self.manejo.cursos[curso_id]['nombre']}'.")

    def crear_evaluacion(self):
        print("Cursos disponibles:")
        if not self.manejo.cursos:
            print("No hay cursos para asignar evaluaciones .")
            return
        for id, curso in self.manejo.cursos.items():
            print(f"- ID: {id} | Nombre: {curso['nombre']}")
        curso_id = input("\nIngrese el ID del curso al que pertenece la tarea: ").upper()
        if curso_id not in self.manejo.cursos:
            print(f"Error: El curso con ID {curso_id} no existe.")
            return
        while True:
            try:
                nombre_evaluacion = input("Ingrese el nombre del tipo de evaluación: ").upper()
                if not nombre_evaluacion.strip():
                    raise ValueError("El nombre no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        while True:
            try:
                descripcion_evaluacion = input("Describa el contenido de la evalución: ")
                if not descripcion_evaluacion.strip():
                    raise ValueError("La descripcion no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        tarea_info = {'nombre': nombre_evaluacion, 'descripcion': descripcion_evaluacion, 'curso_id': curso_id}
        clave_actividad = f"{curso_id}-{nombre_evaluacion}"
        self.manejo.guardar_actividades(clave_actividad, tarea_info)
        print(f"\nTarea '{nombre_evaluacion}' creada exitosamente y asignada al curso '{self.manejo.cursos[curso_id]['nombre']}'.")

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
        while True:
            try:
                id_curso = input("\nIngrese el ID del curso: ").upper()
                if not id_curso.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        if id_curso not in self.manejo.cursos:
            print("Error: El curso no existe.")
            return
        actividades_del_curso = {k: v for k, v in self.manejo.actividades.items() if v['curso_id'] == id_curso}
        if not actividades_del_curso:
            print("No hay tareas o evaluaciones creadas para este curso.")
            return
        print("\nActividades disponibles en el curso:")
        for clave_actividad, actividad in actividades_del_curso.items():
            print(f"- {actividad['nombre']} ({actividad['descripcion']}) - Clave: {clave_actividad}")
        while True:
            try:
                nombre_actividad = input("\nIngrese el nombre de la actividad a calificar: ").upper().strip()
                if not nombre_actividad.strip():
                    raise ValueError("El nombre no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
        clave_actividad = None
        for k, v in self.manejo.actividades.items():
            if v['curso_id'] == id_curso and v['nombre'].upper() == nombre_actividad:
                clave_actividad = k
                break
        if not clave_actividad:
            print("Error: La actividad no se encontró en este curso.")
            return
        estudiantes_inscritos = [id_estudiante for id_estudiante, info_estudiante in self.manejo.usuarios.items() if info_estudiante['rol'] == 'Estudiante' and id_curso in info_estudiante['cursos']]
        if not estudiantes_inscritos:
            print("No hay estudiantes inscritos en este curso.")
            return
        print(f"\nAsignando notas para la actividad '{self.manejo.actividades[clave_actividad]['nombre']}':")
        for id_estudiante in estudiantes_inscritos:
            estudiante_info = self.manejo.usuarios[id_estudiante]
            while True:
                try:
                    nota = float(input(f"  > Ingrese la nota para {estudiante_info['nombre']}: "))
                    if not 0 <= nota <= 100:
                        print("Error: La nota debe ser un número entre 0 y 100.")
                        continue
                except ValueError:
                    print("Error: La nota solo puede ser un número válido.")
                    continue
                except Exception as e:
                    print(f"Ocurrió un error {e}")
                    continue
                else:
                    break
            clave_nota = f"{id_estudiante}-{clave_actividad}"
            self.manejo.guardar_notas(clave_nota, {'nota': nota,'id_estudiante': id_estudiante,'nombre_actividad': self.manejo.actividades[clave_actividad]['nombre'],'curso_id': id_curso})
            print(f"Nota de {nota} registrada para {estudiante_info['nombre']}.")


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
        while True:
            try:
                id_curso = input("\nIngrese el ID del curso que desea consultar: ").upper()
                if not id_curso.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n ")
            except Exception as e:
                print("Ocurrió un error:", e)
            else:
                break
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

        while True:
            try:
                id_curso = input("\nIngrese el ID del curso para ver los estudiantes inscritos: ").upper()
                if not id_curso.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n")
            except Exception as e:
                print(f"Error: {e}\n")
            else:
                break
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
        while True:
            try:
                id_estudiante = input("\nIngrese el carnet del estudiante: ").upper()
                if not id_estudiante.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n")
            except Exception as e:
                print(f"Error: {e}\n")
            else:
                break
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
        while True:
            try:
                id_curso = input("\nIngrese el ID del curso para ver sus actividades: ").upper()
                if not id_curso.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n")
            except Exception as e:
                print(f"Error: {e}\n")
            else:
                break
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
        while True:
            try:
                id_estudiante = input("\nIngrese el carnet del estudiante para generar el reporte: ").upper()
                if not id_estudiante.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n")
            except Exception as e:
                print(f"Error: {e}\n")
            else:
                break
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
        while True:
            try:
                descripcion_reporte = input("\nPor favor, ingrese una descripción del desempeño del estudiante:\n")
                if not descripcion_reporte.strip():
                    raise ValueError("la descripcion no puede quedar vacia")
            except ValueError as e:
                print(f"Error: {e}\n")
            except Exception as e:
                print(f"Error: {e}\n")
            else:
                break
        reporte_guardar = {'fecha': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'descripcion': descripcion_reporte}
        estudiante_info['reportes'].append(reporte_guardar)
        print("\nReporte descriptivo generado y guardado con éxito.")

class VerInfo:
    def __init__(self, manejo):
        self.manejo = manejo

    def ver_informacion(self):
        while True:
            try:
                id_busqueda = input("Ingrese el ID o carnet del usuario a consultar: ").upper()
                if not id_busqueda.strip():
                    raise ValueError("El id no puede quedar vacio")
            except ValueError as e:
                print(f"Error: {e}\n")
            except Exception as e:
                print(f"Error: {e}\n")
            else:
                break
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
    print("1. Crear")
    print("2. Consultoria")
    print("3. Administrar Cursos")
    print("4. Generar Reporte")
    print("5. Salir del Programa")
    menu_option = input("Ingrese el número de la opción que quiera ingresar: ")
    print()
    match menu_option:
        case "1":
            print("Crear")
            print("1. Crear Curso")
            print("2. Crear Usuario")
            print("3. Crear Actividad")
            print("4. Cancelar creacion")
            menu_option2 = input("Ingrese el número de la opción que quiera realizar: ")
            print()
            match menu_option2:
                case "1":
                    print("Crear Curso")
                    crear_curso.registrar_curso()
                    print()
                case "2":
                    print("Crear Usuario")
                    print("1. Registrar Estudiante")
                    print("2. Registrar Instructor")
                    menu_option02 = input("Ingrese el número de la opción que quiera realizar: ")
                    print()
                    match menu_option02:
                        case "1":
                            print("Registrar Estudiante")
                            crear_usuario.registrar_estudiante()
                            print()
                        case "2":
                            print("Registrar Instructor")
                            crear_usuario.registrar_instructor()
                            print()
                        case _:
                            print("Valor invalido, vuelva a intentar")
                            print()
                case "3":
                    print("Crear Actividad")
                    print("1. Crear Tarea")
                    print("2. Crear Evaluación")
                    menu_option002 = input("Ingrese el número de la opción que quiera realizar: ")
                    print()
                    match menu_option002:
                        case "1":
                            print("Crear Tarea")
                            asignar_actividad.crear_tarea()
                            print()
                        case "2":
                            print("Crear Evaluación")
                            asignar_actividad.crear_evaluacion()
                            print()
                        case _:
                            print("Vuelva a intentar")
                            print()
                case "4":
                    print("Cancelando Creación")
                case _:
                    print("Valor invalido, vuelva a intentar")
                    print()
        case "2":
            print("Consultoria")
            print("1. Consultar Curso")
            print("2. Consultar Estudiantes Inscritos")
            print("3. Consultar Actividades")
            print("4. Consultar Calificaciones")
            print("5. Consultar Información de Usuario")
            print("6. Cancelar consulta")
            menu_option3 = input("Ingrese el número de la opción que quiera realizar: ")
            print()
            match menu_option3:
                case "1":
                    print("Consultar Curso")
                    consultar_curso.consultar_curso()
                    print()
                case "2":
                    print("Consultar Estudiantes Inscritos")
                    consultar_estudiantes.consultar_estudiantes()
                    print()
                case "3":
                    print("Consultar Actividades")
                    consultar_actividad.consultar_actividad()
                    print()
                case "4":
                    print("Consultar Calificaciones")
                    consultar_calificaciones.consultar_calificaciones()
                    print()
                case "5":
                    print("Consultar Información de Usuario")
                    ver_informacion.ver_informacion()
                    print()
                case "6":
                    print("Cancelando Consulta...")
                case _:
                    print("Valor invalido, vuelva a intentar")
                    print()
        case "3":
            print("Administrar Curso")
            print("1. Asignar Curso a Usuario")
            print("2. Registrar Nota a Estudiantes")
            print("3. Eliminar Usuario de Algún Curso")
            print("4. Cambiar de Nombre a un Curso")
            print("5. Cambiar ID a un Curso")
            print("6. Cancelar Administración")
            menu_option4 = input("Ingrese el número de la opción que quiera realizar: ")
            print()
            match menu_option4:
                case "1":
                    print("Asignar Curso a Usuario")
                    asignar_curso.asignar_curso()
                    print()
                case "2":
                    print("Registrar Nota a Estudiantes")
                    asignar_nota.asignar_nota()
                    print()
                case "3":
                    print("Eliminar Usuario de Algún Curso")
                    administrar_cursos.eliminar_usuario()
                    print()
                case "4":
                    print("Cambiar de Nombre a un Curso")
                    administrar_cursos.cambiar_nombre()
                    print()
                case "5":
                    print("Cambiar ID a un Curso")
                    administrar_cursos.cambiar_id()
                    print()
                case "6":
                    print("Cancelando adminitración...")
                case _:
                    print("Valor invalido, vuelva a intentar")
                    print()
        case "4":
            print("Generar Reporte")
            crear_reporte.registrar_reporte()
            print()
        case "5":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")
            print()
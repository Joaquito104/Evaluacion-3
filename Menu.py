import mysql.connector as mysql
import bcrypt

# Función para establecer la conexión con la base de datos
def conexion():
    try:
        con = mysql.connect(
            host="127.0.0.1",
            user="root",
            password="Inacap.2024",
            database="Banco"
        )
        if con.is_connected():
            print("Conectado a la base de datos.")
            return con
        else:
            print("No se pudo conectar a la base de datos.")
            return None
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


class Banco:
    def __init__(self):
        self.usuario = None

    # Clase base Usuario
    class Usuario:
        def __init__(self, rut, nombre, apellido, correo, usuario, clave, tipo_usuario):
            self.rut = rut
            self.nombre = nombre
            self.apellido = apellido
            self.correo = correo
            self.usuario = usuario
            self.clave = clave
            self.tipo_usuario = tipo_usuario

        # Método para registrar un nuevo usuario
        def registrar_usuario(self):
            clave_hash = bcrypt.hashpw(self.clave.encode('utf-8'), bcrypt.gensalt())
            con = conexion()
            if con:
                cursor = con.cursor()
                query = "INSERT INTO usuarios (rut, nombre, apellido, correo, usuario, clave, tipo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (self.rut, self.nombre, self.apellido, self.correo, self.usuario, clave_hash, self.tipo_usuario))
                con.commit()
                cursor.close()
                con.close()
                print("Usuario registrado correctamente.")
            else:
                print("No se pudo conectar a la base de datos.")

        # Método para crear una cuenta para el usuario
        def crear_cuenta(self, tipo_cuenta, saldo_inicial):
            con = conexion()
            if con:
                cursor = con.cursor()
                query = "INSERT INTO cuentas (usuario, tipo, saldo) VALUES (%s, %s, %s)"
                cursor.execute(query, (self.rut, tipo_cuenta, saldo_inicial))
                con.commit()
                cursor.close()
                con.close()
                print("Cuenta creada correctamente.")
            else:
                print("No se pudo conectar a la base de datos.")

        # Método para ver las cuentas del usuario
        def ver_cuentas(self):
            con = conexion()
            if con:
                cursor = con.cursor()
                query = "SELECT * FROM cuentas WHERE usuario = %s"
                cursor.execute(query, (self.rut,))
                for cuenta in cursor.fetchall():
                    print(f"ID: {cuenta[0]}, Tipo: {cuenta[2]}, Saldo: {cuenta[3]}")
                cursor.close()
                con.close()
            else:
                print("No se pudo conectar a la base de datos.")
        
        # Método para actualizar los datos del usuario
        def actualizar_usuario(self):
            conn = conexion()
            if conn:
                cursor = conn.cursor()
                
                # Verificar si el tipo de usuario existe en la tabla tipo_usuario
                query_verificar_tipo = "SELECT COUNT(*) FROM tipo_usuario WHERE id = %s"
                cursor.execute(query_verificar_tipo, (self.tipo_usuario,))
                tipo_existente = cursor.fetchone()[0]
                
                if tipo_existente == 0:
                    print("El tipo de usuario no existe en la base de datos.")
                    cursor.close()
                    conn.close()
                    return
                
                # Si el tipo existe, proceder con la actualización del usuario
                query = "UPDATE usuarios SET nombre = %s, correo = %s, tipo = %s WHERE rut = %s"
                cursor.execute(query, (self.nombre, self.correo, self.tipo_usuario, self.rut))
                conn.commit()
                
                cursor.close()
                conn.close()
                print("Datos del usuario actualizados correctamente.")
            else:
                print("No se pudo conectar a la base de datos.")


        # Método para eliminar un usuario
        def eliminar_usuario(self):
            con = conexion()
            if con:
                cursor = con.cursor()
                query = "DELETE FROM usuarios WHERE rut = %s"
                cursor.execute(query, (self.rut,))
                con.commit()
                cursor.close()
                con.close()
                print("Usuario eliminado correctamente.")
            else:
                print("No se pudo conectar a la base de datos.")


    # Funciones de Menú para el Usuario
    def menu_usuario(self, usuario):
        while True:
            print("\nMenú de Usuario")
            print("1. Crear cuenta")
            print("2. Ver mis cuentas")
            print("3. Cambiar mis datos")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                tipo_cuenta = input("Ingrese el tipo de cuenta: ")
                saldo_inicial = float(input("Ingrese el saldo inicial: "))
                usuario.crear_cuenta(tipo_cuenta, saldo_inicial)

            elif opcion == "2":
                usuario.ver_cuentas()

            elif opcion == "3":
                nombre = input("Ingrese su nuevo nombre: ")
                correo = input("Ingrese su nuevo correo: ")
                usuario.nombre = nombre
                usuario.correo = correo
                usuario.actualizar_usuario()

            elif opcion == "4":
                break
            else:
                print("Opción no válida.")


    # Funciones para gestionar Tipos de Usuario
    def gestionar_tipo_usuario(self):
        while True:
            print("\nGestión de Tipos de Usuario")
            print("1. Crear Tipo de Usuario")
            print("2. Actualizar Tipo de Usuario")
            print("3. Eliminar Tipo de Usuario")
            print("4. Volver al menú anterior")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                tipo = input("Ingrese el nombre del nuevo tipo de usuario: ")
                con = conexion()
                if con:
                    cursor = con.cursor()
                    query = "INSERT INTO tipo_usuario (tipo) VALUES (%s)"
                    cursor.execute(query, (tipo,))
                    con.commit()
                    cursor.close()
                    con.close()
                    print("Tipo de usuario creado correctamente.")
            elif opcion == "2":
                id_tipo = input("Ingrese el ID del tipo de usuario a actualizar: ")
                nuevo_tipo = input("Ingrese el nuevo nombre para el tipo de usuario: ")
                con = conexion()
                if con:
                    cursor = con.cursor()
                    query = "UPDATE tipo_usuario SET tipo = %s WHERE id = %s"
                    cursor.execute(query, (nuevo_tipo, id_tipo))
                    con.commit()
                    cursor.close()
                    con.close()
                    print("Tipo de usuario actualizado correctamente.")
            elif opcion == "3":
                id_tipo = input("Ingrese el ID del tipo de usuario a eliminar: ")
                con = conexion()
                if con:
                    cursor = con.cursor()
                    query = "DELETE FROM tipo_usuario WHERE id = %s"
                    cursor.execute(query, (id_tipo,))
                    con.commit()
                    cursor.close()
                    con.close()
                    print("Tipo de usuario eliminado correctamente.")
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

    # Funciones para gestionar Tipos de Cuenta
    def gestionar_tipo_cuenta(self):
        while True:
            print("\nGestión de Tipos de Cuenta")
            print("1. Crear Tipo de Cuenta")
            print("2. Actualizar Tipo de Cuenta")
            print("3. Eliminar Tipo de Cuenta")
            print("4. Volver al menú anterior")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                tipo = input("Ingrese el nombre del nuevo tipo de cuenta: ")
                con = conexion()
                if con:
                    cursor = con.cursor()
                    query = "INSERT INTO tipo_cuenta (tipo) VALUES (%s)"
                    cursor.execute(query, (tipo,))
                    con.commit()
                    cursor.close()
                    con.close()
                    print("Tipo de cuenta creado correctamente.")
            elif opcion == "2":
                id_tipo = input("Ingrese el ID del tipo de cuenta a actualizar: ")
                nuevo_tipo = input("Ingrese el nuevo nombre para el tipo de cuenta: ")
                con = conexion()
                if con:
                    cursor = con.cursor()
                    query = "UPDATE tipo_cuenta SET tipo = %s WHERE id = %s"
                    cursor.execute(query, (nuevo_tipo, id_tipo))
                    con.commit()
                    cursor.close()
                    con.close()
                    print("Tipo de cuenta actualizado correctamente.")
            elif opcion == "3":
                id_tipo = input("Ingrese el ID del tipo de cuenta a eliminar: ")
                con = conexion()
                if con:
                    cursor = con.cursor()
                    query = "DELETE FROM tipo_cuenta WHERE id = %s"
                    cursor.execute(query, (id_tipo,))
                    con.commit()
                    cursor.close()
                    con.close()
                    print("Tipo de cuenta eliminado correctamente.")
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

    # Funciones para gestionar Tipos de Movimiento
    def gestionar_tipo_movimiento(self):
        while True:
            print("\nGestión de Tipos de Movimiento")
            print("1. Crear Tipo de Movimiento")
            print("2. Actualizar Tipo de Movimiento")
            print("3. Eliminar Tipo de Movimiento")
            print("4. Volver al menú anterior")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                tipo = input("Ingrese el nombre del nuevo tipo de movimiento: ")
                con = conexion()
                if con:
                    cursor = con.cursor()
                    query = "INSERT INTO tipo_movimiento (tipo) VALUES (%s)"
                    cursor.execute(query, (tipo,))
                    con.commit()
                    cursor.close()
                    con.close()
                    print("Tipo de movimiento creado correctamente.")
            elif opcion == "2":
                id_tipo = input("Ingrese el ID del tipo de movimiento a actualizar: ")
                nuevo_tipo = input("Ingrese el nuevo nombre para el tipo de movimiento: ")
                con = conexion()
                if con:
                    cursor = con.cursor()
                    query = "UPDATE tipo_movimiento SET tipo = %s WHERE id = %s"
                    cursor.execute(query, (nuevo_tipo, id_tipo))
                    con.commit()
                    cursor.close()
                    con.close()
                    print("Tipo de movimiento actualizado correctamente.")
            elif opcion == "3":
                id_tipo = input("Ingrese el ID del tipo de movimiento a eliminar: ")
                con = conexion()
                if con:
                    cursor = con.cursor()
                    query = "DELETE FROM tipo_movimiento WHERE id = %s"
                    cursor.execute(query, (id_tipo,))
                    con.commit()
                    cursor.close()
                    con.close()
                    print("Tipo de movimiento eliminado correctamente.")
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

    # Funciones de Menú para el Administrador
    def menu_administrador(self):
        while True:
            print("\nMenú de Administrador")
            print("1. Gestionar Usuarios")
            print("2. Gestionar Tipos de Cuenta")
            print("3. Gestionar Tipos de Movimiento")
            print("4. Gestionar Tipos de Usuario")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.gestionar_tipo_usuario()  # Corregido aquí
            elif opcion == "2":
                self.gestionar_tipo_cuenta()
            elif opcion == "3":
                self.gestionar_tipo_movimiento()
            elif opcion == "4":
                self.gestionar_tipo_usuario()
            elif opcion == "5":
                break
            else:
                print("Opción no válida.")

    # Función Principal
    def main(self):
        print("Bienvenido al sistema")
        rol = input("Ingrese su rol (Administrador/Usuario): ").strip().lower()

        if rol == "administrador":
            self.menu_administrador()
        elif rol == "usuario":
            rut = input("Ingrese su rut: ").strip()

        else:
            print("Rol no válido.")

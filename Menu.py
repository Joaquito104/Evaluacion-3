import mysql.connector as mysql
import bcrypt
import time

# Función para establecer la conexión con la base de datos
def conexion():
    try:
        conexion = mysql.connect(
            host="127.0.0.1",
            user="root",
            password="Inacap.2024",
            database="Banco"
        )
        if conexion.is_connected():
            print("Conectado a la base de datos.")
            return conexion
        else:
            print("No se pudo conectar a la base de datos.")
            return None  # Retornar None si no se pudo conectar
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Clase Usuario con atributos específicos de un usuario
class Usuario:
    def __init__(self, rut, nombre, apellido, correo, usuario, tipo_usuario_id, clave):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.usuario = usuario
        self.tipo_usuario_id = tipo_usuario_id
        self.clave = clave
    
    def insertar(self):
        clave_hash = bcrypt.hashpw(self.clave.encode('utf-8'), bcrypt.gensalt())
        try:
            conector = conexion()
            if conector:
                cursor = conector.cursor()
                query = """
                INSERT INTO Banco.usuarios (rut, nombre, apellido, correo, usuario, clave, tipo) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (self.rut, self.nombre, self.apellido, self.correo, self.usuario, clave_hash, self.tipo_usuario_id))
                conector.commit()
                print("Usuario insertado correctamente.")
                cursor.close()
                conector.close()
            else:
                print("ERROR. Acción no ejecutada: No se pudo conectar a la base de datos.")
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")

# Clase Administrador con métodos para gestionar el sistema del banco
class Administrador:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
    
    def insertar_tipo_usuario(self, tipo):
        try:
            conector = conexion()
            if conector:
                cursor = conector.cursor()
                query = "INSERT INTO Banco.tipo_usuario (tipo) VALUES (%s)"
                cursor.execute(query, (tipo,))
                conector.commit()
                print("Tipo de usuario insertado correctamente.")
                cursor.close()
                conector.close()
            else:
                print("ERROR. Acción no ejecutada: No se pudo conectar a la base de datos.")
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")

    def insertar_tipo_cuenta(self, tipo):
        try:
            conector = conexion()
            if conector:
                cursor = conector.cursor()
                query = "INSERT INTO Banco.tipo_cuenta (tipo) VALUES (%s)"
                cursor.execute(query, (tipo,))
                conector.commit()
                print("Tipo de cuenta insertado correctamente.")
                cursor.close()
                conector.close()
            else:
                print("ERROR. Acción no ejecutada: No se pudo conectar a la base de datos.")
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")

    def insertar_cuenta(self, usuario_id, tipo_cuenta_id, saldo):
        try:
            conector = conexion()
            if conector:
                cursor = conector.cursor()
                query = "INSERT INTO Banco.cuentas (usuario, tipo, saldo) VALUES (%s, %s, %s)"
                cursor.execute(query, (usuario_id, tipo_cuenta_id, saldo))
                conector.commit()
                print("Cuenta insertada correctamente.")
                cursor.close()
                conector.close()
            else:
                print("ERROR. Acción no ejecutada: No se pudo conectar a la base de datos.")
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")

    def insertar_tipo_movimiento(self, tipo):
        try:
            conector = conexion()
            if conector:
                cursor = conector.cursor()
                query = "INSERT INTO Banco.tipo_movimiento (tipo) VALUES (%s)"
                cursor.execute(query, (tipo,))
                conector.commit()
                print("Tipo de movimiento insertado correctamente.")
                cursor.close()
                conector.close()
            else:
                print("ERROR. Acción no ejecutada: No se pudo conectar a la base de datos.")
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")

    def insertar_movimiento_cuenta(self, cuenta_id, tipo_movimiento_id, monto):
        try:
            conector = conexion()
            if conector:
                cursor = conector.cursor()
                query = "INSERT INTO Banco.movimientos_cuenta (cuenta, movimiento, monto) VALUES (%s, %s, %s)"
                cursor.execute(query, (cuenta_id, tipo_movimiento_id, monto))
                conector.commit()
                print("Movimiento insertado correctamente.")
                cursor.close()
                conector.close()
            else:
                print("ERROR. Acción no ejecutada: No se pudo conectar a la base de datos.")
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")

    def mostrar_menu(self):
        time.sleep(5)
        print("Inicio de sección exitoso")
        
        while True:
            print("\nSelecciona una opción:")
            print("1. Añadir tipo de usuario")
            print("2. Añadir usuario")
            print("3. Añadir tipo de cuenta")
            print("4. Añadir cuenta")
            print("5. Añadir tipo de movimiento")
            print("6. Añadir movimiento en cuenta")
            print("7. Salir del sistema y cerrar sección")
            opcion = input("Ingrese por favor: ")

            if opcion == '1':
                tipo = input('Ingrese el tipo de usuario: ')
                self.insertar_tipo_usuario(tipo)  
            elif opcion == '2':
                rut = input('Ingrese rut: ')
                nombre = input('Ingrese nombre: ')			
                apellido = input('Ingrese apellido: ')
                correo = input('Ingrese correo: ')
                usuario = input('Ingrese nombre de usuario: ')
                tipo_usuario_id = int(input('Ingrese ID del tipo de usuario: '))
                clave = input('Ingrese clave: ')
                usuario = Usuario(rut, nombre, apellido, correo, usuario, tipo_usuario_id, clave)
                usuario.insertar()
            elif opcion == '3':
                tipo = input('Ingrese el tipo de cuenta: ')
                self.insertar_tipo_cuenta(tipo)  
            elif opcion == '4':
                usuario_id = int(input('Ingrese ID del usuario: '))
                tipo_cuenta_id = int(input('Ingrese ID del tipo de cuenta: '))
                saldo = float(input('Ingrese el saldo: '))
                self.insertar_cuenta(usuario_id, tipo_cuenta_id, saldo)  
            elif opcion == '5':
                tipo = input('Ingrese el tipo de movimiento: ')
                self.insertar_tipo_movimiento(tipo)  
            elif opcion == '6':
                cuenta_id = int(input('Ingrese ID de la cuenta: '))
                tipo_movimiento_id = int(input('Ingrese ID del tipo de movimiento: '))
                monto = float(input('Ingrese el monto del movimiento: '))
                self.insertar_movimiento_cuenta(cuenta_id, tipo_movimiento_id, monto)  
            elif opcion == '7':
                print("Cerrando sección...")
                time.sleep(1)
                print("Que tenga un excelente día")
                time.sleep(3)
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

# Función principal para elegir la acción a realizar
def main():
    print("Hola estimado administrador, Bienvenido al sistema del banco ")

    Seccion = input("Ingrese 1 para Iniciar sección como administrador.\n Ingrese 2 para iniciar sección como usuario.\n En caso de cerrar el sistema ingrese cualquier cosa diferente\n")

    if Seccion == "1":
        nombre_admin = input('Ingrese el nombre del administrador: ')
        admin = Administrador(nombre_admin, 'Administrador')
        admin.mostrar_menu()
    
    elif Seccion == "2":
        # Aquí se podría implementar la lógica de usuario
        pass
    else:
        print('Saliendo del sistema...')
        time.sleep(1)

main()

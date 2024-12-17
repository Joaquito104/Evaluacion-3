import mysql.connector as mysql
import bcrypt

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

# Función para insertar tipo de usuario
def insertar_tipo_usuario():
    tipo = input('Ingrese el tipo de usuario: ')
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

# Función para insertar usuario
def insertar_usuario():
    rut = input('Ingrese rut: ')
    nombre = input('Ingrese nombre: ')			
    apellido = input('Ingrese apellido: ')
    correo = input('Ingrese correo: ')
    usuario = input('Ingrese nombre de usuario: ')
    tipo_usuario_id = int(input('Ingrese ID del tipo de usuario: '))  # Usar el ID de tipo_usuario
    clave = input('Ingrese clave: ').encode('utf-8')
    clave_hash = bcrypt.hashpw(clave, bcrypt.gensalt())
    try:
        conector = conexion()
        if conector:
            cursor = conector.cursor()
            query = """
            INSERT INTO Banco.usuarios (rut, nombre, apellido, correo, usuario, clave, tipo) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (rut, nombre, apellido, correo, usuario, clave_hash, tipo_usuario_id))
            conector.commit()
            print("Usuario insertado correctamente.")
            cursor.close()
            conector.close()
        else:
            print("ERROR. Acción no ejecutada: No se pudo conectar a la base de datos.")
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")

# Función para insertar tipo de cuenta
def insertar_tipo_cuenta():
    tipo = input('Ingrese el tipo de cuenta: ')
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

# Función para insertar cuenta
def insertar_cuenta():
    usuario_id = int(input('Ingrese ID del usuario: '))
    tipo_cuenta_id = int(input('Ingrese ID del tipo de cuenta: '))
    saldo = float(input('Ingrese el saldo: '))
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

# Función para insertar tipo de movimiento
def insertar_tipo_movimiento():
    tipo = input('Ingrese el tipo de movimiento: ')
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

# Función para insertar movimiento en cuenta
def insertar_movimiento_cuenta():
    cuenta_id = int(input('Ingrese ID de la cuenta: '))
    tipo_movimiento_id = int(input('Ingrese ID del tipo de movimiento: '))
    monto = float(input('Ingrese el monto del movimiento: '))
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

# Función principal para elegir la acción a realizar
def main():
    while True:
        print("\nSelecciona una opción:")
        print("1. Insertar tipo de usuario")
        print("2. Insertar usuario")
        print("3. Insertar tipo de cuenta")
        print("4. Insertar cuenta")
        print("5. Insertar tipo de movimiento")
        print("6. Insertar movimiento en cuenta")
        print("7. Salir")
        opcion = input("Opción: ")

        if opcion == '1':
            insertar_tipo_usuario()  # Insertar tipo de usuario
        elif opcion == '2':
            insertar_usuario()  # Insertar usuario
        elif opcion == '3':
            insertar_tipo_cuenta()  # Insertar tipo de cuenta
        elif opcion == '4':
            insertar_cuenta()  # Insertar cuenta
        elif opcion == '5':
            insertar_tipo_movimiento()  # Insertar tipo de movimiento
        elif opcion == '6':
            insertar_movimiento_cuenta()  # Insertar movimiento en cuenta
        elif opcion == '7':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Llamar a la función principal
if __name__ == "__main__":
    main()

import mysql.connector as mysql

def conexion():

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
        return print('Error no se pudo conectar a la base de datos')


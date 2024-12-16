from Base_de_Datos.Acciones.Conexion import conexion as connectar

def insertar(insercion, tabla, valores):    #Valores asignados en otro modulo
    try:
        conector = connectar.conn()

        if conector:
            cursor = conector.cursor()  #Realiza accion /Querys
            query = f"INSERT INTO Banco.{insercion} ({tabla}) VALUES (%s)"
            cursor.execute(query, (valores,))  # Pasa 'valores' como parámetro
            conector.commit()  # Confirmar la inserción
            print("Inserción realizada correctamente.")

            # Cerrar el cursor y la conexión
            cursor.close()
            conector.close()
        else:
            print("ERROR. Acción no ejecutada: No se pudo conectar a la base de datos.")
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")

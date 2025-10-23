# db/conexion.py

import mysql.connector
from mysql.connector import errorcode

# Configuración de tu base de datos
# Estos datos son los que usas para acceder a phpMyAdmin/MySQL
DB_CONFIG = {
    'user': 'root',       
    'password': '',   
    'host': 'localhost',                  
    'database': 'hotel_db'                
}

def conectar_db():
    """Establece y retorna una conexión a la base de datos."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Usuario o contraseña incorrectos.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: La base de datos no existe.")
        else:
            print(f"Error de conexión: {err}")
        return None

# Ejemplo de función para cargar datos al inicio (uso en MenuPrincipal)
def obtener_todas_las_habitaciones():
    """Consulta todas las habitaciones y retorna una lista de datos."""
    conn = conectar_db()
    if conn is None:
        return []
        
    cursor = conn.cursor(dictionary=True)
    habitaciones = []
    try:
        cursor.execute("SELECT id_habitacion, num_habitacion, tipo, precio_noche, estado FROM habitaciones")
        habitaciones = cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener habitaciones: {e}")
    finally:
        cursor.close()
        conn.close()
    return habitaciones
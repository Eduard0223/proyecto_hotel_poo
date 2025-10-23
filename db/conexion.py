import mysql.connector
from mysql.connector import errorcode

# Configuración de tu base de datos
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

# Función de Carga Genérica (Soluciona el ImportError)
def obtener_datos_iniciales(tabla, campos):
    """Función genérica para cargar datos iniciales de cualquier tabla."""
    conn = conectar_db()
    if conn is None:
        return []
        
    cursor = conn.cursor(dictionary=True)
    datos = []
    try:
        sql = f"SELECT {', '.join(campos)} FROM {tabla}"
        cursor.execute(sql)
        datos = cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener datos de {tabla}: {e}")
    finally:
        cursor.close()
        conn.close()
    return datos
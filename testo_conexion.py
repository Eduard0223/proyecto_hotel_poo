import pymysql

try:
    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="hotel_programa"
    )
    print("✅ Conexión exitosa!")
    conexion.close()
except:
    print("❌ Error de conexión")
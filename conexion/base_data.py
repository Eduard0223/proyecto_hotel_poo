# Conexión a la base de datos
import pymysql

class Database:
    
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "hotel_programa"
        self.connection = None
    
    def conectar(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conectado a la base de datos")
            return self.connection
        except:
            print("Error al conectar")
            return None
    
    def cerrar(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")
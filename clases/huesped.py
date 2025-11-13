# Clase para manejar huéspedes

class Huesped:
    
    def __init__(self, conexion):
        self.conexion = conexion
        self.id = None
        self.nombre = None
        self.apellido = None
        self.telefono = None
        self.email = None
        self.rut = None
    
    def agregar(self, nombre, apellido, telefono, email, rut):
        try:
            cursor = self.conexion.cursor()
            sql = "INSERT INTO huespedes (nombre, apellido, telefono, email, rut) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (nombre, apellido, telefono, email, rut))
            self.conexion.commit()
            self.id = cursor.lastrowid
            cursor.close()
            return True
        except:
            return False
    
    def buscar(self, rut):
        try:
            cursor = self.conexion.cursor()
            sql = "SELECT * FROM huespedes WHERE rut = %s"
            cursor.execute(sql, (rut,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        except:
            return None
    
    def listar(self):
        try:
            cursor = self.conexion.cursor()
            sql = "SELECT * FROM huespedes"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except:
            return []
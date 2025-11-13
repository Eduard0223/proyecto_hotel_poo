# Clase para manejar habitaciones

class Habitacion:
    
    def __init__(self, conexion):
        self.conexion = conexion
        self.id = None
        self.numero = None
        self.tipo = None
        self.precio = None
    
    def obtener(self, id_habitacion):
        try:
            cursor = self.conexion.cursor()
            sql = "SELECT * FROM habitaciones WHERE id = %s"
            cursor.execute(sql, (id_habitacion,))
            resultado = cursor.fetchone()
            cursor.close()
            if resultado:
                self.id = resultado[0]
                self.numero = resultado[1]
                self.tipo = resultado[2]
                self.precio = resultado[3]
            return resultado
        except:
            return None
    
    def listar_disponibles(self):
        try:
            cursor = self.conexion.cursor()
            sql = "SELECT * FROM habitaciones WHERE estado = 'disponible'"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except:
            return []
    
    def esta_disponible(self, id_habitacion, fecha_entrada, fecha_salida):
        try:
            cursor = self.conexion.cursor()
            sql = """SELECT COUNT(*) FROM reservas 
                     WHERE habitacion_id = %s 
                     AND estado IN ('pendiente', 'confirmada')
                     AND ((fecha_entrada <= %s AND fecha_salida > %s)
                     OR (fecha_entrada < %s AND fecha_salida >= %s)
                     OR (fecha_entrada >= %s AND fecha_salida <= %s))"""
            cursor.execute(sql, (id_habitacion, fecha_entrada, fecha_entrada,
                                fecha_salida, fecha_salida, fecha_entrada, fecha_salida))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado[0] == 0
        except:
            return False
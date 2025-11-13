# Clase para manejar reservas
from datetime import datetime

class Reserva:
    
    def __init__(self, conexion):
        self.conexion = conexion
        self.id = None
    
    def crear(self, huesped_id, habitacion_id, fecha_entrada, fecha_salida):
        try:
            # calcular noches
            entrada = datetime.strptime(fecha_entrada, '%Y-%m-%d')
            salida = datetime.strptime(fecha_salida, '%Y-%m-%d')
            noches = (salida - entrada).days
            
            # bbtener precio
            cursor = self.conexion.cursor()
            sql = "SELECT precio_noche FROM habitaciones WHERE id = %s"
            cursor.execute(sql, (habitacion_id,))
            precio = cursor.fetchone()[0]
            
            # calcular total
            total = noches * float(precio)
            
            # nsertar reserva
            sql = """INSERT INTO reservas (huesped_id, habitacion_id, fecha_entrada, 
                     fecha_salida, num_noches, costo_total, estado) 
                     VALUES (%s, %s, %s, %s, %s, %s, 'pendiente')"""
            cursor.execute(sql, (huesped_id, habitacion_id, fecha_entrada, 
                                fecha_salida, noches, total))
            self.conexion.commit()
            self.id = cursor.lastrowid
            cursor.close()
            return True, total
        except:
            return False, 0
    
    def listar(self):
        try:
            cursor = self.conexion.cursor()
            sql = """SELECT r.id, h.nombre, h.apellido, hab.numero, 
                     r.fecha_entrada, r.fecha_salida, r.costo_total, r.estado
                     FROM reservas r
                     JOIN huespedes h ON r.huesped_id = h.id
                     JOIN habitaciones hab ON r.habitacion_id = hab.id"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except:
            return []
    
    def cambiar_estado(self, id_reserva, nuevo_estado):
        try:
            cursor = self.conexion.cursor()
            sql = "UPDATE reservas SET estado = %s WHERE id = %s"
            cursor.execute(sql, (nuevo_estado, id_reserva))
            self.conexion.commit()
            cursor.close()
            return True
        except:
            return False
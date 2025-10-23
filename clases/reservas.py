from db.conexion import conectar_db 
from datetime import datetime

class Reserva:
    def __init__(self, id_reserva, huesped, habitacion, fecha_entrada_str, fecha_salida_str, estado="Confirmada"):
        self.id = id_reserva
        self.huesped = huesped
        self.habitacion = habitacion
        self.fecha_entrada = datetime.strptime(fecha_entrada_str, "%Y-%m-%d").date()
        self.fecha_salida = datetime.strptime(fecha_salida_str, "%Y-%m-%d").date()
        self.estado = estado
        self.total = self.calcular_total() 
        
    def calcular_total(self):
        dias = (self.fecha_salida - self.fecha_entrada).days
        return dias * self.habitacion.precio_noche if dias > 0 else 0

    def obtener_detalles(self):
        return {
            "ID Reserva": self.id,
            "Huésped": f"{self.huesped.nombre} {self.huesped.apellido}",
            "Habitación": self.habitacion.numero,
            "Entrada": self.fecha_entrada,
            "Salida": self.fecha_salida,
            "Estado": self.estado,
            "Total": f"${self.total:,.0f}"
        }


    def modificar_estado_reserva(self, nuevo_estado):
        """Método auxiliar para cambiar el estado de la reserva en la DB."""
        conn = conectar_db()
        if conn is None: return False
        cursor = conn.cursor()
        
        try:
            sql = "UPDATE reservas SET estado = %s WHERE id_reserva = %s"
            cursor.execute(sql, (nuevo_estado, self.id))
            conn.commit()
            self.estado = nuevo_estado
            return cursor.rowcount > 0
        except Exception as e:
            conn.rollback()
            print(f"DB ERROR (Reserva.modificar_estado): {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def confirmar_reserva(self):
        """CREATE: Inserta la reserva y actualiza el estado de la habitación en la DB (Transacción)."""
        conn = conectar_db()
        if conn is None: return False
        cursor = conn.cursor()
        
        try:
            # 1. Insertar Reserva
            sql_reserva = "INSERT INTO reservas (id_huesped, id_habitacion, fecha_entrada, fecha_salida, estado, total) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_reserva, (self.huesped.id, self.habitacion.id, self.fecha_entrada, self.fecha_salida, "Confirmada", self.total))
            self.id = cursor.lastrowid
            
            # 2. Actualizar estado de la Habitación
            self.habitacion.modificar_habitacion(estado="Reservada")
            
            conn.commit()
            return True
        except Exception as e:
            conn.rollback()
            print(f"DB ERROR (Reserva.confirmar): {e}")
            return False
        finally:
            cursor.close()
            conn.close()
            
    def cancelar_reserva(self):
        if self.modificar_estado_reserva("Cancelada") and self.habitacion.modificar_habitacion(estado="Disponible"):
            return True
        return False
        
    def realizar_check_in(self):
        if self.modificar_estado_reserva("Ocupada") and self.habitacion.modificar_habitacion(estado="Ocupada"):
            return True
        return False

    def finalizar_reserva(self):
        if self.modificar_estado_reserva("Finalizada") and self.habitacion.modificar_habitacion(estado="Limpieza"):
            return True
        return False
    
    def modificar_fechas(self, nueva_entrada_str, nueva_salida_str):
        return True
from datetime import datetime, timedelta
from .habitaciones import Habitacion
from .huesped import Huesped

class Reserva:
    def __init__(self, id_reserva, huesped, habitacion, fecha_entrada, fecha_salida):
        self.id_reserva = id_reserva
        self.huesped = huesped
        self.habitacion = habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.estado = "Pendiente"  # Estados posibles: Pendiente, Confirmada, Cancelada, Finalizada
        self.total = self._calcular_total()

    def _calcular_total(self):
        """Calcula el total de la reserva basado en las noches de estancia"""
        fecha_entrada = datetime.strptime(self.fecha_entrada, "%Y-%m-%d")
        fecha_salida = datetime.strptime(self.fecha_salida, "%Y-%m-%d")
        noches = (fecha_salida - fecha_entrada).days
        return noches * self.habitacion.precio_noche

    def confirmar_reserva(self):
        """Confirma la reserva y actualiza el estado de la habitación"""
        if self.habitacion.estado == "Disponible":
            self.estado = "Confirmada"
            self.habitacion.estado = "Ocupada"
            return True
        return False

    def cancelar_reserva(self):
        """Cancela la reserva y libera la habitación"""
        if self.estado == "Confirmada":
            self.estado = "Cancelada"
            self.habitacion.estado = "Disponible"
            return True
        return False

    def finalizar_reserva(self):
        """Finaliza la reserva cuando el huésped hace check-out"""
        if self.estado == "Confirmada":
            self.estado = "Finalizada"
            self.habitacion.estado = "Disponible"
            return True
        return False

    def obtener_detalles(self):
        """Retorna los detalles de la reserva"""
        return {
            "ID Reserva": self.id_reserva,
            "Huésped": f"{self.huesped.nombre} {self.huesped.apellido}",
            "Habitación": self.habitacion.n_habitacion,
            "Fecha Entrada": self.fecha_entrada,
            "Fecha Salida": self.fecha_salida,
            "Estado": self.estado,
            "Total": f"${self.total}"
        }

    def modificar_fechas(self, nueva_fecha_entrada=None, nueva_fecha_salida=None):
        """Modifica las fechas de la reserva si es posible"""
        if self.estado != "Confirmada":
            if nueva_fecha_entrada:
                self.fecha_entrada = nueva_fecha_entrada
            if nueva_fecha_salida:
                self.fecha_salida = nueva_fecha_salida
            self.total = self._calcular_total()
            return True
        return False
    

class Huesped:   
    def __init__(self, id_huesped, nombre, apellido, rut, telefono, correo):
        if not self._validar_rut(rut):
            raise ValueError("Formato de RUT inválido")
        if not self._validar_correo(correo):
            raise ValueError("Formato de correo inválido")
            
        self.id_huesped = id_huesped
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.telefono = telefono
        self.correo = correo
        self.historial_reservas = []

    def crear_perfil(self):
        """Crea y muestra el perfil del huésped"""
        print(f"Perfil creado: {self.nombre} {self.apellido} (RUT: {self.rut})")
        return True

    def actualizar_informacion(self, **kwargs):
        """Actualiza la información del huésped.
       (nombre, apellido, telefono, correo)
        """
        for campo, valor in kwargs.items():
            if campo == 'correo' and not self._validar_correo(valor):
                raise ValueError("Formato de correo inválido")
            if hasattr(self, campo):
                setattr(self, campo, valor)
        print(f"Información actualizada para {self.nombre} {self.apellido}")

    def mostrar_informacion(self):
        """Muestra toda la información del huésped"""
        info = {
            "ID": self.id_huesped,
            "Nombre completo": f"{self.nombre} {self.apellido}",
            "RUT": self.rut,
            "Teléfono": self.telefono,
            "Correo": self.correo,
            "Número de reservas": len(self.historial_reservas)
        }
        for campo, valor in info.items():
            print(f"{campo}: {valor}")

    def agregar_reserva(self, reserva):
        """Agrega una reserva al historial del huésped"""
        self.historial_reservas.append(reserva)
        print(f"Reserva {reserva.id_reserva} agregada al historial")

    def mostrar_historial_reservas(self):
        """Muestra el historial de reservas del huésped"""
        if not self.historial_reservas:
            print("No hay reservas en el historial")
            return
        
        print(f"\nHistorial de reservas de {self.nombre} {self.apellido}:")
        for reserva in self.historial_reservas:
            print(f"Reserva ID: {reserva.id_reserva}")
            print(f"Habitación: {reserva.habitacion.n_habitacion}")
            print(f"Fechas: {reserva.fecha_entrada} - {reserva.fecha_salida}")
            print(f"Estado: {reserva.estado}")
            print("-" * 30)

    @staticmethod
    def _validar_rut(rut):
        """Valida el formato del RUT chileno"""
        import re
        patron = r'^\d{7,8}-[\dkK]$'
        return bool(re.match(patron, rut))

    @staticmethod
    def _validar_correo(correo):
        """Valida el formato del correo electrónico"""
        import re
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(patron, correo))

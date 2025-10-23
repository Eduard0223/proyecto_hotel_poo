from db.conexion import conectar_db 

class Huesped:
    def __init__(self, id_huesped, nombre, apellido, rut, telefono, correo):
        self.id = id_huesped
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.telefono = telefono
        self.correo = correo
        self.historial_reservas = [] # Se llena al cargar las reservas

    def mostrar_informacion(self):
        print(f"ID: {self.id} | Nombre: {self.nombre} {self.apellido} | RUT: {self.rut} | Teléfono: {self.telefono} | Correo: {self.correo}")

    def agregar_reserva(self, reserva):
        self.historial_reservas.append(reserva)

    def mostrar_historial_reservas(self):
        print(f"\n--- Historial de Reservas para {self.nombre} ---")
        if not self.historial_reservas:
            print("No hay reservas registradas.")
            return
        for reserva in self.historial_reservas:
            print(f"ID Reserva: {reserva.id} | Hab: {reserva.habitacion.numero} | Entrada: {reserva.fecha_entrada} | Salida: {reserva.fecha_salida} | Estado: {reserva.estado}")
    
    def crear_perfil(self):
        """CREATE: Inserta el huésped en la DB."""
        conn = conectar_db()
        if conn is None: return False
        cursor = conn.cursor()
        sql = "INSERT INTO huespedes (nombre, apellido, rut, telefono, correo) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.execute(sql, (self.nombre, self.apellido, self.rut, self.telefono, self.correo))
            conn.commit()
            self.id = cursor.lastrowid
            return True
        except Exception as e:
            conn.rollback()
            print(f"DB ERROR (Huesped.crear_perfil): {e}") 
            return False
        finally:
            cursor.close()
            conn.close()

    def actualizar_informacion(self, **kwargs):
        """UPDATE: Modifica el teléfono o correo en la DB."""
        conn = conectar_db()
        if conn is None: return False
        
        updates = []
        params = []
        
        if 'telefono' in kwargs: 
            self.telefono = kwargs['telefono']
            updates.append("telefono = %s")
            params.append(self.telefono)
        if 'correo' in kwargs: 
            self.correo = kwargs['correo']
            updates.append("correo = %s")
            params.append(self.correo)
            
        if not updates: return False
        
        sql = f"UPDATE huespedes SET {', '.join(updates)} WHERE rut = %s"
        params.append(self.rut)
        
        cursor = conn.cursor()
        try:
            cursor.execute(sql, tuple(params))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            conn.rollback()
            print(f"DB ERROR (Huesped.actualizar): {e}")
            return False
        finally:
            cursor.close()
            conn.close()
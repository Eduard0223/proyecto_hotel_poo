from db.conexion import conectar_db 

class Habitacion:
    TIPOS_VALIDOS = {"Individual": 45000, "Doble": 65000, "Suite": 120000, "Familiar": 95000}

    def __init__(self, id_hab, num, tipo, precio, estado="Disponible"):
        self.id = id_hab
        self.numero = num
        self.tipo = tipo
        self.precio_noche = precio
        self.estado = estado

    def mostrar_detalles(self):
        print(f"ID: {self.id} | Número: {self.numero} | Tipo: {self.tipo} | Precio: ${self.precio_noche:,.0f} | Estado: {self.estado}")

    def agregar_habitacion(self):
        """CREATE: Inserta una nueva habitación en la DB."""
        conn = conectar_db()
        if conn is None: return False
        cursor = conn.cursor()
        sql = "INSERT INTO habitaciones (num_habitacion, tipo, precio_noche, estado) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql, (self.numero, self.tipo, self.precio_noche, self.estado))
            conn.commit()
            self.id = cursor.lastrowid # Obtiene el ID generado por la DB
            return True
        except Exception as e:
            conn.rollback()
            print(f"DB ERROR (Habitacion.agregar): {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def modificar_habitacion(self, **kwargs):
        """UPDATE: Modifica atributos de la habitación en la DB."""
        conn = conectar_db()
        if conn is None: return False
        
        updates = []
        params = []
        
        if 'tipo' in kwargs: 
            self.tipo = kwargs['tipo']
            updates.append("tipo = %s")
            params.append(self.tipo)
        if 'precio_noche' in kwargs: 
            self.precio_noche = kwargs['precio_noche']
            updates.append("precio_noche = %s")
            params.append(self.precio_noche)
        if 'estado' in kwargs: 
            self.estado = kwargs['estado']
            updates.append("estado = %s")
            params.append(self.estado)
            
        if not updates: return False
        
        sql = f"UPDATE habitaciones SET {', '.join(updates)} WHERE id_habitacion = %s"
        params.append(self.id)
        
        cursor = conn.cursor()
        try:
            cursor.execute(sql, tuple(params))
            conn.commit()
            return cursor.rowcount > 0 
        except Exception as e:
            conn.rollback()
            print(f"DB ERROR (Habitacion.modificar): {e}")
            return False
        finally:
            cursor.close()
            conn.close()
            
    def programar_limpieza(self):
        return self.modificar_habitacion(estado="Limpieza")
        
    def agregar_nota_mantenimiento(self, nota):
        return self.modificar_habitacion(estado="Mantenimiento")
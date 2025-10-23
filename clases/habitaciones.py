class Habitacion:
    # Definición de constantes de clase
    TIPOS_VALIDOS = {
        "Individual": {"capacidad": 1, "descripcion": "Habitación con una cama individual"},
        "Doble": {"capacidad": 2, "descripcion": "Habitación con una cama matrimonial"},
        "Twin": {"capacidad": 2, "descripcion": "Habitación con dos camas individuales"},
        "Triple": {"capacidad": 3, "descripcion": "Habitación con tres camas individuales"},
        "Suite": {"capacidad": 2, "descripcion": "Suite de lujo con sala de estar"},
        "Familiar": {"capacidad": 4, "descripcion": "Habitación amplia para familias"}
    }
    
    ESTADOS_VALIDOS = ["Disponible", "Ocupada", "Mantenimiento", "Limpieza", "Reservada"]

    def __init__(self, id_habitacion, n_habitacion, tipo, precio_noche, estado="Disponible"):
        # Validaciones
        if not isinstance(id_habitacion, int) or id_habitacion < 1:
            raise ValueError("ID de habitación debe ser un número entero positivo")
        
        if not isinstance(precio_noche, (int, float)) or precio_noche < 0:
            raise ValueError("Precio por noche debe ser un número positivo")
            
        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo de habitación inválido. Tipos válidos: {', '.join(self.TIPOS_VALIDOS.keys())}")
            
        if estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido. Estados válidos: {', '.join(self.ESTADOS_VALIDOS)}")

        self.id_habitacion = id_habitacion
        self.n_habitacion = n_habitacion    
        self.tipo = tipo
        self.precio_noche = precio_noche
        self.estado = estado
        self.historial_ocupacion = []
        self.ultima_limpieza = None
        self.caracteristicas = self.TIPOS_VALIDOS[tipo]
        self.notas_mantenimiento = []
    
    def agregar_habitacion(self):
        """Registra una nueva habitación en el sistema"""
        print(f"Habitación: {self.n_habitacion} agregada")
        self.mostrar_detalles()
        return True
    
    def modificar_habitacion(self, **kwargs):
        """Modifica los atributos de la habitación.
        (tipo, precio_noche, estado)
        """
        cambios = []
        
        if 'tipo' in kwargs and kwargs['tipo'] in self.TIPOS_VALIDOS:
            self.tipo = kwargs['tipo']
            self.caracteristicas = self.TIPOS_VALIDOS[kwargs['tipo']]
            cambios.append('tipo')
            
        if 'precio_noche' in kwargs and isinstance(kwargs['precio_noche'], (int, float)) and kwargs['precio_noche'] > 0:
            self.precio_noche = kwargs['precio_noche']
            cambios.append('precio')
            
        if 'estado' in kwargs and kwargs['estado'] in self.ESTADOS_VALIDOS:
            self.estado = kwargs['estado']
            cambios.append('estado')
            
        if cambios:
            print(f"Habitación {self.n_habitacion} modificada. Campos actualizados: {', '.join(cambios)}")
            return True
        return False
    
    def consultar_estado(self):
        """Muestra el estado actual de la habitación"""
        print(f"Habitación {self.n_habitacion} está actualmente {self.estado}")
        if self.estado == "Ocupada":
            ultima_ocupacion = self.historial_ocupacion[-1] if self.historial_ocupacion else None
            if ultima_ocupacion:
                print(f"Ocupada desde: {ultima_ocupacion['fecha_entrada']}")
        return self.estado

    def registrar_ocupacion(self, fecha_entrada, fecha_salida, huesped):
        """Registra una nueva ocupación en el historial"""
        self.historial_ocupacion.append({
            "fecha_entrada": fecha_entrada,
            "fecha_salida": fecha_salida,
            "huesped": huesped
        })
        self.estado = "Ocupada"
        
    def programar_limpieza(self):
        """Programa la limpieza de la habitación"""
        if self.estado == "Ocupada":
            print("No se puede programar limpieza de una habitación ocupada")
            return False
        self.estado = "Limpieza"
        return True
        
    def finalizar_limpieza(self):
        """Registra la finalización de la limpieza"""
        if self.estado != "Limpieza":
            return False
        from datetime import datetime
        self.ultima_limpieza = datetime.now()
        self.estado = "Disponible"
        return True
        
    def agregar_nota_mantenimiento(self, nota):
        """Agrega una nota de mantenimiento"""
        from datetime import datetime
        self.notas_mantenimiento.append({
            "fecha": datetime.now(),
            "nota": nota
        })
        
    def mostrar_detalles(self):
        """Muestra todos los detalles de la habitación"""
        print(f"\nDetalles de la Habitación {self.n_habitacion}")
        print("-" * 40)
        print(f"ID: {self.id_habitacion}")
        print(f"Tipo: {self.tipo}")
        print(f"Capacidad: {self.caracteristicas['capacidad']} personas")
        print(f"Descripción: {self.caracteristicas['descripcion']}")
        print(f"Precio por noche: ${self.precio_noche}")
        print(f"Estado actual: {self.estado}")
        if self.ultima_limpieza:
            print(f"Última limpieza: {self.ultima_limpieza}")
        print("-" * 40)
        
    def obtener_historial(self):
        """Retorna el historial de ocupación de la habitación"""
        return self.historial_ocupacion

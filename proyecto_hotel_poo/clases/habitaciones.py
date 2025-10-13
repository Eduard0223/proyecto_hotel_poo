class Habitacion:
    def __init__(self, id_habitacion, n_habitacion, tipo, precio_noche, estado= "Disponible"): # le puse = disponible por si no se pasa el argumento de estado, 
                                                                                                 #por lo cual por defecto va a ser "Disponible"
        self.id_habitacion = id_habitacion
        self.n_habitacion = n_habitacion    
        self.tipo = tipo
        self.precio_noche = precio_noche
        self.estado = estado
    
    def agregar_habitacion(self):
        print(f"Habitación: {self.n_habitacion}agregada ({self.tipo})- ${self.precio_noche}/noche")
    
    def modificar_habitacion(self,nuevo_tipo= None, nuevo_precio = None): # al usar "None" hace que los parametros sean opcionales por si el profe pregunta XD
        if nuevo_tipo:
            self.tipo = nuevo_tipo
        if nuevo_precio:
            self.precio_noche = nuevo_precio
        print(f"Habitación {self.n_habitacion}modificada")
    
    def consultar_estado(self):
        print(f"Habitación {self.n_habitacion} esta actualmente {self.estado}")

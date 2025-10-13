class Huesped:   
    def __init__(self, id_huesped, nombre, apellido, rut, telefono, correo):
            self.id_huesped = id_huesped
            self.nombre = nombre
            self.apellido = apellido
            self.rut = rut
            self.telefono = telefono
            self.correo = correo
    def crear_perfil(self):
            print(f"Perfil creado: {self.nombre} {self.apellido}{self.apellido}(RUT: {self.rut})")


from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey, Text, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime
from principal.conexion import Base

class Huesped(Base):
    __tablename__ = 'huespedes'
    
    id_huesped = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    documento_identidad = Column(String(50), unique=True, nullable=False)
    telefono = Column(String(20), nullable=False)
    email = Column(String(100))
    fecha_registro = Column(TIMESTAMP, default=datetime.utcnow)
    ultima_actualizacion = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    estado = Column(Enum('Activo', 'Inactivo'), default='Activo')
    
    # Relación con reservas
    reservas = relationship("Reserva", back_populates="huesped")

class Habitacion(Base):
    __tablename__ = 'habitaciones'
    
    id_habitacion = Column(Integer, primary_key=True, autoincrement=True)
    numero_habitacion = Column(String(10), unique=True, nullable=False)
    tipo = Column(Enum('Individual', 'Doble', 'Suite', 'Familiar'), nullable=False)
    precio_por_noche = Column(DECIMAL(10, 2), nullable=False)
    estado = Column(Enum('Disponible', 'Ocupada', 'Mantenimiento', 'Reservada'), default='Disponible')
    capacidad = Column(Integer, nullable=False)
    descripcion = Column(Text)
    piso = Column(Integer, nullable=False)
    ultima_limpieza = Column(TIMESTAMP)
    fecha_registro = Column(TIMESTAMP, default=datetime.utcnow)
    
    # Relación con reservas
    reservas = relationship("Reserva", back_populates="habitacion")

class Reserva(Base):
    __tablename__ = 'reservas'
    
    id_reserva = Column(Integer, primary_key=True, autoincrement=True)
    id_huesped = Column(Integer, ForeignKey('huespedes.id_huesped', ondelete='RESTRICT'), nullable=False)
    id_habitacion = Column(Integer, ForeignKey('habitaciones.id_habitacion', ondelete='RESTRICT'), nullable=False)
    fecha_entrada = Column(Date, nullable=False)
    fecha_salida = Column(Date, nullable=False)
    costo_total = Column(DECIMAL(12, 2), nullable=False)
    estado = Column(Enum('Pendiente', 'Confirmada', 'CheckIn', 'CheckOut', 'Cancelada'), default='Pendiente')
    numero_huespedes = Column(Integer, nullable=False)
    metodo_pago = Column(Enum('Efectivo', 'Tarjeta', 'Transferencia'))
    observaciones = Column(Text)
    fecha_registro = Column(TIMESTAMP, default=datetime.utcnow)
    ultima_actualizacion = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relaciones
    huesped = relationship("Huesped", back_populates="reservas")
    habitacion = relationship("Habitacion", back_populates="reservas")
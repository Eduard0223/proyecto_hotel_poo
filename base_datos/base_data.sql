-- Crear base de datos
CREATE DATABASE IF NOT EXISTS hotel_programa;
USE hotel_programa;

-- Tabla de huéspedes
CREATE TABLE huespedes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    rut VARCHAR(20) UNIQUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de habitaciones
CREATE TABLE habitaciones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    numero VARCHAR(10) UNIQUE NOT NULL,
    tipo ENUM('simple', 'doble', 'suite') NOT NULL,
    precio_noche DECIMAL(10,2) NOT NULL,
    estado ENUM('disponible', 'ocupada', 'mantenimiento') DEFAULT 'disponible',
    capacidad INT NOT NULL
);

-- Tabla de reservas
CREATE TABLE reservas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    huesped_id INT NOT NULL,
    habitacion_id INT NOT NULL,
    fecha_entrada DATE NOT NULL,
    fecha_salida DATE NOT NULL,
    num_noches INT NOT NULL,
    costo_total DECIMAL(10,2) NOT NULL,
    estado ENUM('pendiente', 'confirmada', 'cancelada', 'finalizada') DEFAULT 'pendiente',
    fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (huesped_id) REFERENCES huespedes(id),
    FOREIGN KEY (habitacion_id) REFERENCES habitaciones(id)
);

-- Insertar datos de ejemplo
INSERT INTO habitaciones (numero, tipo, precio_noche, capacidad) VALUES
('101', 'simple', 50.00, 1),
('102', 'simple', 50.00, 1),
('201', 'doble', 80.00, 2),
('202', 'doble', 80.00, 2),
('301', 'suite', 150.00, 4);
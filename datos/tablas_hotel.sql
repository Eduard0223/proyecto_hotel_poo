
    CREATE TABLE Huespedes (
        ID_Huesped INT PRIMARY KEY AUTO_INCREMENT,
        Nombre VARCHAR(100) NOT NULL,
        Apellido VARCHAR(100) NOT NULL,
        Documento_Identidad VARCHAR(50) UNIQUE NOT NULL,
        Telefono VARCHAR(20) NOT NULL,
        Email VARCHAR(100),
        Fecha_Registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Ultima_Actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        Estado ENUM('Activo', 'Inactivo') DEFAULT 'Activo',
        CONSTRAINT chk_email CHECK (Email LIKE '%@%.%' OR Email IS NULL)
    ) ENGINE=InnoDB;

    CREATE TABLE Habitaciones (
        ID_Habitacion INT PRIMARY KEY AUTO_INCREMENT,
        Numero_Habitacion VARCHAR(10) NOT NULL UNIQUE,
        Tipo ENUM('Individual', 'Doble', 'Suite', 'Familiar') NOT NULL,
        Precio_Por_Noche DECIMAL(10, 2) NOT NULL,
        Estado ENUM('Disponible', 'Ocupada', 'Mantenimiento', 'Reservada') DEFAULT 'Disponible',
        Capacidad INT NOT NULL,
        Descripcion TEXT,
        Piso INT NOT NULL,
        Ultima_Limpieza TIMESTAMP,
        Fecha_Registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT chk_precio CHECK (Precio_Por_Noche > 0),
        CONSTRAINT chk_capacidad CHECK (Capacidad > 0)
    ) ENGINE=InnoDB;

    CREATE TABLE Reservas (
        ID_Reserva INT PRIMARY KEY AUTO_INCREMENT,
        ID_Huesped INT NOT NULL,
        ID_Habitacion INT NOT NULL,
        Fecha_Entrada DATE NOT NULL,
        Fecha_Salida DATE NOT NULL,
        Costo_Total DECIMAL(12, 2) NOT NULL,
        Estado ENUM('Pendiente', 'Confirmada', 'CheckIn', 'CheckOut', 'Cancelada') DEFAULT 'Pendiente',
        Numero_Huespedes INT NOT NULL,
        Metodo_Pago ENUM('Efectivo', 'Tarjeta', 'Transferencia') NULL,
        Observaciones TEXT,
        Fecha_Registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Ultima_Actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (ID_Huesped) REFERENCES Huespedes(ID_Huesped) ON DELETE RESTRICT,
        FOREIGN KEY (ID_Habitacion) REFERENCES Habitaciones(ID_Habitacion) ON DELETE RESTRICT,
        CONSTRAINT chk_fechas CHECK (Fecha_Salida >= Fecha_Entrada),
        CONSTRAINT chk_costo CHECK (Costo_Total >= 0)
    ) ENGINE=InnoDB;

    -- Índices para mejorar el rendimiento
    CREATE INDEX idx_habitaciones_estado ON Habitaciones(Estado);
    CREATE INDEX idx_reservas_fechas ON Reservas(Fecha_Entrada, Fecha_Salida);
    CREATE INDEX idx_reservas_estado ON Reservas(Estado);
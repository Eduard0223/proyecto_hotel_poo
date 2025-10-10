    CREATE TABLE Huespedes (
        ID_Huesped INT PRIMARY KEY AUTO_INCREMENT,
        Nombre VARCHAR(100) NOT NULL,
        Apellido VARCHAR(100) NOT NULL,
        Documento_Identidad VARCHAR(50) UNIQUE NOT NULL,
        Telefono VARCHAR(20),
        Email VARCHAR(100)
    );


    CREATE TABLE Habitaciones (
        ID_Habitacion INT PRIMARY KEY AUTO_INCREMENT,
        Numero_Habitacion VARCHAR(10) NOT NULL,
        Tipo VARCHAR(50) NOT NULL, 
        Precio_Por_Noche DECIMAL(10, 2) NOT NULL,
        Estado VARCHAR(20) DEFAULT 'Disponible'
    );

    CREATE TABLE Reservas (
        ID_Reserva INT PRIMARY KEY AUTO_INCREMENT,
        ID_Huesped INT NOT NULL,
        ID_Habitacion INT NOT NULL,
        Fecha_Entrada DATE NOT NULL,
        Fecha_Salida DATE NOT NULL,
        Costo_Total DECIMAL(12, 2) NOT NULL,
        FOREIGN KEY (ID_Huesped) REFERENCES Huespedes(ID_Huesped),
        FOREIGN KEY (ID_Habitacion) REFERENCES Habitaciones(ID_Habitacion)
    );

-- 
-- 1. Crear la Base de Datos
CREATE DATABASE SistemaInventarioDB;
GO

-- 2. Usar la Base de Datos creada
USE SistemaInventarioDB;
GO

-- 3. Tabla de Productos (Catálogo y Stock)
CREATE TABLE Productos (
    id_producto INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);
GO

-- 4. Tabla de Clientes
CREATE TABLE Clientes (
    id_cliente INT IDENTITY(1,1) PRIMARY KEY,
    nombre_completo VARCHAR(150) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(100)
);
GO

-- 5. Tabla de Ventas (Cabecera de la transacción)
CREATE TABLE Ventas (
    id_venta INT IDENTITY(1,1) PRIMARY KEY,
    fecha_venta DATETIME DEFAULT GETDATE(),
    id_cliente INT NOT NULL,
    total_venta DECIMAL(10, 2) NOT NULL,
    -- Llave foránea que conecta la venta con el cliente
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);
GO

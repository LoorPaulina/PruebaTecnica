drop database if exists vuelos;
create database vuelos;
use vuelos;

-- Tabla: usuario
CREATE TABLE usuario (
    id VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(250) not null,
    correo VARCHAR(100) not null,
    telefono VARCHAR(10),
    contraseña VARCHAR(250) not null,
    audit_create_date DATE
);

-- Tabla: ciudad
CREATE TABLE ciudad (
    id VARCHAR(10) PRIMARY KEY,
    descripcion VARCHAR(200) not null,
    audit_create_date DATE,
    audit_create_user VARCHAR(10),
    audit_update_date DATE,
    audit_update_user VARCHAR(10),
    FOREIGN KEY (audit_create_user) REFERENCES usuario(id),
    FOREIGN KEY (audit_update_user) REFERENCES usuario(id)
);

-- Tabla: clase
CREATE TABLE clase (
    codigo VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(100) not null,
    descripcion VARCHAR(100),
    equipaje_permitido FLOAT,
    precio FLOAT not null,
    audit_create_date DATE,
    audit_create_user VARCHAR(10),
    audit_update_date DATE,
    audit_update_user VARCHAR(10),
    FOREIGN KEY (audit_create_user) REFERENCES usuario(id),
    FOREIGN KEY (audit_update_user) REFERENCES usuario(id)
);

-- Tabla: estado_reserva
CREATE TABLE estado_reserva (
    codigo VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(50) not null,
    descripcion VARCHAR(100),
    audit_create_date DATE,
    audit_create_user VARCHAR(10),
    audit_update_date DATE,
    audit_update_user VARCHAR(10),
    FOREIGN KEY (audit_create_user) REFERENCES usuario(id),
    FOREIGN KEY (audit_update_user) REFERENCES usuario(id)
);

-- Tabla: metodo_pago
CREATE TABLE metodo_pago (
    codigo VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(10) not null,
    audit_create_date DATE,
    audit_create_user VARCHAR(10),
    audit_update_date DATE,
    audit_update_user VARCHAR(10),
    FOREIGN KEY (audit_create_user) REFERENCES usuario(id),
    FOREIGN KEY (audit_update_user) REFERENCES usuario(id)
);

-- Tabla: vuelo
CREATE TABLE vuelo (
    id VARCHAR(10) PRIMARY KEY,
    origen VARCHAR(100),
    destino VARCHAR(100),
    precio FLOAT,
    disponibilidad TINYINT(1),
    fecha DATE,
    clase VARCHAR(10),
    audit_create_date DATE,
    audit_create_user VARCHAR(10),
    audit_update_date DATE,
    audit_update_user VARCHAR(10),
    FOREIGN KEY (clase) REFERENCES clase(codigo),
    FOREIGN KEY (audit_create_user) REFERENCES usuario(id),
    FOREIGN KEY (audit_update_user) REFERENCES usuario(id)
);

-- Tabla: reserva
CREATE TABLE reserva (
    id VARCHAR(10) PRIMARY KEY,
    vuelo VARCHAR(10) not null,
    usuario VARCHAR(10) not null,
    estado VARCHAR(10) not null,
    metodo_pago VARCHAR(10),
    audit_create_date DATE,
    audit_create_user VARCHAR(10),
    audit_update_date DATE,
    audit_update_user VARCHAR(10),
    FOREIGN KEY (estado) REFERENCES estado_reserva(codigo),
    FOREIGN KEY (metodo_pago) REFERENCES metodo_pago(codigo),
    FOREIGN KEY (usuario) REFERENCES usuario(id),
    FOREIGN KEY (vuelo) REFERENCES vuelo(id),
    FOREIGN KEY (audit_create_user) REFERENCES usuario(id),
    FOREIGN KEY (audit_update_user) REFERENCES usuario(id)
);


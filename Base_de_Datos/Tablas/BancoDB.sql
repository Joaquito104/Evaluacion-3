Create database Banco;
Use Banco;

create table tipo_usuario (
    id int not null auto_increment,
    tipo varchar(20) not null,
    primary key (id)
) engine=InnoDB default charset=utf8mb3 collate=utf8mb3_spanish_ci;

create table usuarios (
    id int not null auto_increment,
    rut varchar(20) not null,
    nombre varchar(20) not null,
    apellido varchar(20) not null,
    correo varchar(50) not null,
    usuario varchar(20) not null,
    clave varchar(257) not null,
    tipo int not null,
    primary key (id),
    key tipo (tipo),
    constraint tipo_usuario_banco foreign key (tipo) references tipo_usuario (id)
) engine=InnoDB default charset=utf8mb3 collate=utf8mb3_spanish_ci;

create table tipo_cuenta (
    id int not null auto_increment,
    tipo varchar (20) not null,
    primary key (id)
) engine=InnoDB default charset=utf8mb3 collate=utf8mb3_spanish_ci;

create table cuentas (
    id int not null auto_increment,
    usuario int not null,
    tipo int not null,
    saldo float not null,
    primary key (id),
    key usuario (usuario),
    key tipo (tipo),
    constraint usuario_cuenta foreign key (usuario) references usuarios (id),
    constraint tipo_cuenta_usuario foreign key (tipo) references tipo_cuenta (id)
) engine=InnoDB default charset=utf8mb3 collate=utf8mb3_spanish_ci;

create table tipo_movimiento (
    id int not null auto_increment,
    tipo varchar (20) not null,
    primary key (id)
) engine=InnoDB default charset=utf8mb3 collate=utf8mb3_spanish_ci;

create table movimientos_cuenta (
    id int not null auto_increment,
    cuenta int not null,
    movimiento int not null,
    monto float not null,
    primary key (id),
    key cuenta (cuenta),
    key movimiento (movimiento),
    constraint cuenta_usuario foreign key (cuenta) references cuentas (id),
    constraint tipo_movimiento_cuenta foreign key (movimiento) references tipo_movimiento (id)
) engine=InnoDB default charset=utf8mb3 collate=utf8mb3_spanish_ci;
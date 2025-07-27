CREATE DATABASE IF NOT EXISTS Pycodebr;
USE Pycodebr;

CREATE TABLE IF NOT EXISTS carros (
    id int not null auto_increment primary key,
    marca varchar(100) not null,
    modelo varchar(100) not null,
    ano int not null
) CHARACTER SET utf8 COLLATE utf8_general_ci;

INSERT INTO carros (marca, modelo, ano) values
    ('Toyota', 'Corolla', 2020),
    ('Honda', 'Civic', 2019),
    ('Ford', 'Focus', 2018),
    ('Chevrolet', 'Onix', 2021),
    ('Volkswagen', 'Gol', 2022);
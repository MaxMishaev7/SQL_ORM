-- TABLES:
-- publisher
-- book
-- shop
-- stock
-- sale

DROP TABLE IF EXISTS sale;
DROP TABLE IF EXISTS stock;
DROP TABLE IF EXISTS shop;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS publisher;


CREATE TABLE IF NOT EXISTS publisher(
id serial PRIMARY KEY NOT NULL,
name varchar(40) NOT NULL 
);

CREATE TABLE IF NOT EXISTS book(
id serial PRIMARY KEY NOT NULL,
title varchar(60) NOT NULL,
id_publisher integer NOT NULL REFERENCES publisher(id)
);

CREATE TABLE IF NOT EXISTS shop(
id serial PRIMARY KEY NOT NULL,
name varchar(40) NOT null
);

CREATE TABLE IF NOT EXISTS stock(
id serial PRIMARY KEY NOT NULL,
id_book integer NOT NULL REFERENCES book(id),
id_shop integer NOT NULL REFERENCES shop(id),
count integer NOT NULL
);

CREATE TABLE IF NOT EXISTS sale(
id serial PRIMARY KEY NOT NULL,
price integer NOT NULL,
date_sale date NOT NULL,
id_stock integer NOT NULL REFERENCES stock(id),
count integer NOT NULL
);
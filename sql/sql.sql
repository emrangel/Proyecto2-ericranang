CREATE DATABASE  IF NOT EXISTS `heladeria`;
USE `heladeria`;

DROP TABLE IF EXISTS heladeria.productos;
DROP TABLE IF EXISTS heladeria.ingredientes;

CREATE TABLE `ingredientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `precio` int NOT NULL,
  `calorias` decimal(5,2) NOT NULL,
  `vegetariano` bit(1) NOT NULL,
  `inventario` decimal(5,2) NOT NULL,
  `tipo` varchar(15) NOT NULL,
  `sabor` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_UNIQUE` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `ingredientes` WRITE;
INSERT INTO `ingredientes` VALUES (1,'Helado de fresa',1500,50.00,_binary '\0',1.00,'Base','Fresa'),(2,'Chispas de chocolate',2500,80.00,_binary '\0',0.80,'Base','Chocolate'),(3,'Maní sin dulce',1200,10.00,_binary '',20.00,'Complemento','Maní'),(4,'Helado de vainilla',1300,48.00,_binary '\0',0.20,'Base','Vainilla'),(5,'Helado de chocolate',1800,120.00,_binary '\0',0.60,'Base','Chocolate'),(6,'Cereales',500,10.00,_binary '',1.20,'Base','Maíz'),(7,'Frutas varias',900,25.00,_binary '',5.00,'Complemento','Frutas varias'),(8,'Chispas de colores',1000,52.00,_binary '',5.00,'Complemento','Dulce'),(9,'Crema de leche',1500,400.00,_binary '\0',10.00,'Complemento','Leche'),(10,'Crema chantilly',3000,200.00,_binary '\0',5.00,'Complemento','Crema');
UNLOCK TABLES;

CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `precio` int NOT NULL,
  `ventas_dia` int NOT NULL,
  `precio_ventas_dia` int NOT NULL,
  `id_ingrediente1` int NOT NULL,
  `id_ingrediente2` int NOT NULL,
  `id_ingrediente3` int NOT NULL,
  `tipo` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_UNIQUE` (`nombre`),
  FOREIGN KEY (`id_ingrediente1`) REFERENCES `ingredientes` (`id`),
  FOREIGN KEY (`id_ingrediente2`) REFERENCES `ingredientes` (`id`),
  FOREIGN KEY (`id_ingrediente3`) REFERENCES `ingredientes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


LOCK TABLES `productos` WRITE;
INSERT INTO `productos` VALUES (1,'Copa1',15000,0,0,1,2,3,'Copa'),(2,'Copa2',12000,0,0,6,9,8,'Copa'),(3,'Copa3',11500,0,0,4,9,7,'Copa'),(4,'Copa4',18000,0,0,4,9,7,'Malteada'),(5,'Copa5',15000,0,0,5,9,8,'Malteada'),(6,'Copa7',12000,0,0,1,9,8,'Malteada');
UNLOCK TABLES;


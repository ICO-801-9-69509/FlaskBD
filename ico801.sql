-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 17, 2026 at 05:40 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ico801`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('253cd6b371d9');

-- --------------------------------------------------------

--
-- Table structure for table `alumnos`
--

CREATE TABLE `alumnos` (
  `matricula` int NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `apaterno` varchar(50) NOT NULL,
  `amaterno` varchar(100) NOT NULL,
  `edad` int NOT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `alumnos`
--

INSERT INTO `alumnos` (`matricula`, `nombre`, `apaterno`, `amaterno`, `edad`, `correo`, `created_date`) VALUES
(65798, 'Manuel', 'Zavala', 'Mendoza', 21, 'example@mail.com', '2026-04-16 11:40:43'),
(67453, 'Aldo David', 'Amaro', 'Chavez', 27, 'example@mail.com', '2026-04-16 11:40:43'),
(68549, 'Leonardo', 'Ramirez', 'Lara', 22, 'example@mail.com', '2026-04-16 11:40:43'),
(69509, 'David', 'Adame', 'Vázquez', 20, 'example@mail.com', '2026-04-16 11:40:43');

-- --------------------------------------------------------

--
-- Table structure for table `cursos`
--

CREATE TABLE `cursos` (
  `id_curso` int NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `id_maestro` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cursos`
--

INSERT INTO `cursos` (`id_curso`, `nombre`, `descripcion`, `id_maestro`) VALUES
(7, 'Sistemas Operativos', 'análisis de arquitecturas para computadoras', 1),
(8, 'Programacion', 'algoritmos', 1),
(9, 'Programacion II', 'algoritmos y programación estructurada', 2),
(10, 'Arturo', 'fisica nivel prepa', 23),
(11, 'Leo', 'algoritmos', 23);

-- --------------------------------------------------------

--
-- Table structure for table `inscripciones`
--

CREATE TABLE `inscripciones` (
  `id_inscripcion` int NOT NULL,
  `id_alumno` int NOT NULL,
  `id_curso` int NOT NULL,
  `fecha_inscripcion` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `inscripciones`
--

INSERT INTO `inscripciones` (`id_inscripcion`, `id_alumno`, `id_curso`, `fecha_inscripcion`) VALUES
(9, 69509, 7, '2026-04-16 19:19:09'),
(10, 67453, 7, '2026-04-16 19:19:16'),
(11, 68549, 7, '2026-04-16 19:19:25'),
(12, 69509, 8, '2026-04-16 19:23:16');

-- --------------------------------------------------------

--
-- Table structure for table `maestros`
--

CREATE TABLE `maestros` (
  `clave` int NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apaterno` varchar(50) NOT NULL,
  `amaterno` varchar(50) NOT NULL,
  `edad` int NOT NULL,
  `correo` varchar(50) NOT NULL,
  `especialidad` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `maestros`
--

INSERT INTO `maestros` (`clave`, `nombre`, `apaterno`, `amaterno`, `edad`, `correo`, `especialidad`) VALUES
(1, 'Roberto', 'Cardiel', 'Rodriguez', 45, 'example@mail.com', 'Ing. en Software'),
(2, 'Alejandro', 'Montes', 'Moreno', 50, 'example@mail.com', 'Ing. en Software'),
(3, 'Luis Roberto', 'Gallegos', 'Muñoz', 45, 'example@mail.com', 'Ing. en Redes'),
(23, 'sdf', 'sf', 'sdf', 22, 'sdf', 'sdf'),
(23437, 'Martha', 'Delgado', 'Perez', 40, 'example@mail.com', 'Ing. en Redes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`matricula`);

--
-- Indexes for table `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id_curso`),
  ADD KEY `id_maestro` (`id_maestro`);

--
-- Indexes for table `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD PRIMARY KEY (`id_inscripcion`),
  ADD UNIQUE KEY `uq_alumno_curso` (`id_alumno`,`id_curso`),
  ADD KEY `id_curso` (`id_curso`);

--
-- Indexes for table `maestros`
--
ALTER TABLE `maestros`
  ADD PRIMARY KEY (`clave`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `matricula` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69510;

--
-- AUTO_INCREMENT for table `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id_curso` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `inscripciones`
--
ALTER TABLE `inscripciones`
  MODIFY `id_inscripcion` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `maestros`
--
ALTER TABLE `maestros`
  MODIFY `clave` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23438;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cursos`
--
ALTER TABLE `cursos`
  ADD CONSTRAINT `cursos_ibfk_1` FOREIGN KEY (`id_maestro`) REFERENCES `maestros` (`clave`);

--
-- Constraints for table `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD CONSTRAINT `inscripciones_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumnos` (`matricula`),
  ADD CONSTRAINT `inscripciones_ibfk_2` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

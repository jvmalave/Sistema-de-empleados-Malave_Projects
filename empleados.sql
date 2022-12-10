-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-12-2022 a las 17:38:01
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistema`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `id_empleado` int(10) NOT NULL,
  `nombre_empleado` varchar(255) NOT NULL,
  `apellido_empleado` varchar(255) NOT NULL,
  `correo_empleado` varchar(255) NOT NULL,
  `foto_empleado` varchar(5000) NOT NULL,
  `fecha_nacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id_empleado`, `nombre_empleado`, `apellido_empleado`, `correo_empleado`, `foto_empleado`, `fecha_nacimiento`) VALUES
(28, 'Carlos', 'Martínez', 'carlosmarinez@gmail.com', '2022120155Carlos_Martinez.PNG', '1992-10-15'),
(29, 'Ruth', 'González', 'rgonzalez@hotmail.com', '2022120318Ruth_Gonzalez.PNG', '1989-05-22'),
(30, 'Juan', 'González', 'juan.gonzalez@gmail.com', '2022120435Juan_Gonzalez.PNG', '1998-02-11'),
(31, 'Mónica', 'Paéz', 'monicap@outlook.com', '2022120639Monica_Paez.PNG', '1996-09-27'),
(32, 'Cristobal', 'Mayers', 'Crismayers@gmail.com', '2022120851Cristobal_Mayers.PNG', '1990-12-24'),
(33, 'Laura', 'Fernández', 'lfernandez@gmail.com', '2022121102Laura_Fernandez.PNG', '2001-01-17');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`id_empleado`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id_empleado` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

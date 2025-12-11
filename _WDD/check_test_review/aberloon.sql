-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 11, 2025 at 04:37 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aberloon`
--

-- --------------------------------------------------------

--
-- Table structure for table `pupildata`
--

CREATE TABLE `pupildata` (
  `PupilID` int(11) NOT NULL,
  `FirstName` varchar(20) NOT NULL,
  `LastName` varchar(20) NOT NULL,
  `DateOfBirth` date NOT NULL,
  `RegClass` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `pupildata`
--

INSERT INTO `pupildata` (`PupilID`, `FirstName`, `LastName`, `DateOfBirth`, `RegClass`) VALUES
(112211, 'Joan', 'Simpson', '1999-02-23', '6A'),
(112212, 'John', 'Adam', '1998-04-12', '6B'),
(112213, 'Alison', 'Brown', '1998-10-30', '6A');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pupildata`
--
ALTER TABLE `pupildata`
  ADD PRIMARY KEY (`PupilID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

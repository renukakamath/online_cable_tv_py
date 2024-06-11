-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 15, 2023 at 08:27 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `musicians_hiring`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_application_child`
--

CREATE TABLE `tbl_application_child` (
  `app_cid` int(5) NOT NULL,
  `app_mid` int(5) NOT NULL,
  `app_desc` varchar(350) NOT NULL,
  `app_status` varchar(10) NOT NULL,
  `exp_id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_application_master`
--

CREATE TABLE `tbl_application_master` (
  `app_mid` int(5) NOT NULL,
  `msc_id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_employer`
--

CREATE TABLE `tbl_employer` (
  `emp_id` int(5) NOT NULL,
  `emp_name` varchar(20) NOT NULL,
  `emp_email` varchar(35) NOT NULL,
  `emp_no` decimal(10,0) NOT NULL,
  `emp_aadhar` decimal(12,0) NOT NULL,
  `emp_password` varchar(10) NOT NULL,
  `emp_status` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_employer`
--

INSERT INTO `tbl_employer` (`emp_id`, `emp_name`, `emp_email`, `emp_no`, `emp_aadhar`, `emp_password`, `emp_status`) VALUES
(1, 'zebah', 'zebah@gmail.com', '907414916', '654782196378', 'zebah123', 1),
(2, 'Sneha Ravi', 'sneha@gmail.com', '863145796', '654782196123', 'sneharav12', 1),
(3, 'Sara Roy', 'sara@gmail.com', '9874236514', '654782196569', 'sara123', 1),
(4, 'Mariya Joseph', 'mariya@gmail.com', '7994169860', '657456982355', 'mariya123', 1),
(5, 'Hiba', 'hiba@gmail.com', '9845632489', '654782196566', 'hiba123', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_experience`
--

CREATE TABLE `tbl_experience` (
  `exp_id` int(5) NOT NULL,
  `exp_title` varchar(20) NOT NULL,
  `exp_desc` varchar(200) NOT NULL,
  `exp_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_genre`
--

CREATE TABLE `tbl_genre` (
  `genre_id` int(5) NOT NULL,
  `genre_name` varchar(20) NOT NULL,
  `genre_status` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_genre`
--

INSERT INTO `tbl_genre` (`genre_id`, `genre_name`, `genre_status`) VALUES
(1, 'Rock', 0),
(2, 'RnB', 1),
(3, 'Hip-Hop', 1),
(4, 'Soul', 1),
(5, 'Jazz', 1),
(6, 'RnB', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_job`
--

CREATE TABLE `tbl_job` (
  `job_id` int(5) NOT NULL,
  `emp_id` int(5) NOT NULL,
  `job_title` varchar(25) NOT NULL,
  `job_desc` varchar(100) NOT NULL,
  `type_id` int(5) NOT NULL,
  `genre_id` int(5) NOT NULL,
  `job_rate` int(3) NOT NULL,
  `job_duration` int(3) NOT NULL,
  `job_location` varchar(35) NOT NULL,
  `job_status` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_login`
--

CREATE TABLE `tbl_login` (
  `username` varchar(35) NOT NULL,
  `password` varchar(10) NOT NULL,
  `type` varchar(10) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_login`
--

INSERT INTO `tbl_login` (`username`, `password`, `type`, `status`) VALUES
('admin', 'admin', 'admin', 1),
('hiba@gmail.com', 'hiba123', 'employer', 1),
('john@gmail.com', 'john123', 'musician', 1),
('mariya@gmail.com', 'mariya123', 'employer', 1),
('ria@gmail.com', 'ria123', 'musician', 1),
('sam@gmail.com', 'sam123', 'musician', 1),
('sara@gmail.com', 'sara123', 'employer', 1),
('sneha@gmail.com', 'sneharav12', 'employer', 1),
('zebah@gmail.com', 'zebah123', 'Employer', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_musician`
--

CREATE TABLE `tbl_musician` (
  `msc_id` int(5) NOT NULL,
  `msc_name` varchar(20) NOT NULL,
  `msc_email` varchar(35) NOT NULL,
  `msc_no` decimal(10,0) NOT NULL,
  `msc_aadhar` decimal(12,0) NOT NULL,
  `msc_password` varchar(10) NOT NULL,
  `msc_status` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_musician`
--

INSERT INTO `tbl_musician` (`msc_id`, `msc_name`, `msc_email`, `msc_no`, `msc_aadhar`, `msc_password`, `msc_status`) VALUES
(1, 'ria', 'ria@gmail.com', '9631487569', '654782196399', 'ria123', 1),
(2, 'Sam', 'sam@gmail.com', '9864412134', '654782196366', 'sam123', 1),
(3, 'john', 'john@gmail.com', '9654752136', '654782196378', 'john123', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_type`
--

CREATE TABLE `tbl_type` (
  `type_id` int(5) NOT NULL,
  `type_name` varchar(20) NOT NULL,
  `type_status` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_type`
--

INSERT INTO `tbl_type` (`type_id`, `type_name`, `type_status`) VALUES
(1, 'Pianist', 1),
(2, 'Vocalist', 0),
(3, 'Violinist', 1),
(4, 'Guitarist', 1),
(5, 'Drummer', 1),
(6, 'Bassist', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_application_child`
--
ALTER TABLE `tbl_application_child`
  ADD PRIMARY KEY (`app_cid`);

--
-- Indexes for table `tbl_application_master`
--
ALTER TABLE `tbl_application_master`
  ADD PRIMARY KEY (`app_mid`);

--
-- Indexes for table `tbl_employer`
--
ALTER TABLE `tbl_employer`
  ADD PRIMARY KEY (`emp_id`);

--
-- Indexes for table `tbl_experience`
--
ALTER TABLE `tbl_experience`
  ADD PRIMARY KEY (`exp_id`);

--
-- Indexes for table `tbl_genre`
--
ALTER TABLE `tbl_genre`
  ADD PRIMARY KEY (`genre_id`);

--
-- Indexes for table `tbl_job`
--
ALTER TABLE `tbl_job`
  ADD PRIMARY KEY (`job_id`);

--
-- Indexes for table `tbl_login`
--
ALTER TABLE `tbl_login`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `tbl_musician`
--
ALTER TABLE `tbl_musician`
  ADD PRIMARY KEY (`msc_id`);

--
-- Indexes for table `tbl_type`
--
ALTER TABLE `tbl_type`
  ADD PRIMARY KEY (`type_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_application_child`
--
ALTER TABLE `tbl_application_child`
  MODIFY `app_cid` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_application_master`
--
ALTER TABLE `tbl_application_master`
  MODIFY `app_mid` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_employer`
--
ALTER TABLE `tbl_employer`
  MODIFY `emp_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tbl_experience`
--
ALTER TABLE `tbl_experience`
  MODIFY `exp_id` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_genre`
--
ALTER TABLE `tbl_genre`
  MODIFY `genre_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_job`
--
ALTER TABLE `tbl_job`
  MODIFY `job_id` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_musician`
--
ALTER TABLE `tbl_musician`
  MODIFY `msc_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_type`
--
ALTER TABLE `tbl_type`
  MODIFY `type_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for logbook_skripsi
CREATE DATABASE IF NOT EXISTS `logbook_skripsi` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `logbook_skripsi`;

-- Dumping structure for table logbook_skripsi.admin
CREATE TABLE IF NOT EXISTS `admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `nidn` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `nidn` (`nidn`),
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`nidn`) REFERENCES `dosen` (`nidn`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table logbook_skripsi.admin: ~2 rows (approximately)
INSERT INTO `admin` (`id`, `username`, `password`, `nidn`) VALUES
	(1, 'dosen', '123', '937182'),
	(2, 'dosen_2', '1234', '010101');

-- Dumping structure for table logbook_skripsi.bimbingan_mahasiswa
CREATE TABLE IF NOT EXISTS `bimbingan_mahasiswa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `npm` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `nama_mahasiswa` varchar(50) DEFAULT NULL,
  `judul_skripsi` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `nidn` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `file_skripsi` longblob,
  `tanggal` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `judul_skripsi` (`judul_skripsi`),
  KEY `npm` (`npm`),
  KEY `nidn` (`nidn`),
  KEY `FK_bimbingan_mahasiswa_mahasiswa` (`nama_mahasiswa`),
  CONSTRAINT `bimbingan_mahasiswa_ibfk_1` FOREIGN KEY (`judul_skripsi`) REFERENCES `skripsi` (`judul_skripsi`),
  CONSTRAINT `bimbingan_mahasiswa_ibfk_2` FOREIGN KEY (`npm`) REFERENCES `mahasiswa` (`npm`),
  CONSTRAINT `bimbingan_mahasiswa_ibfk_3` FOREIGN KEY (`nidn`) REFERENCES `dosen` (`nidn`),
  CONSTRAINT `FK_bimbingan_mahasiswa_mahasiswa` FOREIGN KEY (`nama_mahasiswa`) REFERENCES `mahasiswa` (`nama`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table logbook_skripsi.bimbingan_mahasiswa: ~12 rows (approximately)
INSERT INTO `bimbingan_mahasiswa` (`id`, `npm`, `nama_mahasiswa`, `judul_skripsi`, `nidn`, `file_skripsi`, `tanggal`) VALUES
	(4, '2332002', 'kelvin', 'Ternak Ayam', '010101', _binary 0x433a2f55736572732f757365722f446f63756d656e74732f4761627269656c20546172696b68204f6d6172202832333332303533292074756761732070626f20342e342e706466, '2024-06-11'),
	(5, '2332002', 'kelvin', 'Ternak Ayam', '010101', _binary 0x433a2f55736572732f757365722f446f63756d656e74732f4761627269656c20546172696b68204f6d6172202832333332303533292073697374656d206f706572617369206c61742032206d61792074676c20322e706466, '2024-06-11'),
	(6, '2332002', 'kelvin', 'Ternak Ayam', '010101', _binary 0x433a2f55736572732f757365722f446f776e6c6f6164732f4761627269656c20546172696b68204f6d6172202832333332303533292073697374656d206f706572617369206c617420312074676c206d617920322e706466, '2024-06-11'),
	(7, '2332053', 'Gabriel Tarikh Omar', 'Ternak Lele', '020202', _binary 0x433b617364617364617364, '2024-06-11'),
	(8, '2332002', 'kelvin', 'Ternak Ayam', '1231313', _binary 0x433a2f55736572732f757365722f446f776e6c6f6164732f4761627269656c20546172696b68204f6d6172202832333332303533292073697374656d206f706572617369206c61742032206d61792074676c20322e706466, '2024-06-12'),
	(9, '2332002', 'kelvin', 'Ternak Ayam', '937182', _binary 0x433a2f55736572732f757365722f446f63756d656e74732f4761627269656c20546172696b68204f6d6172202832333332303533292073697374656d206f706572617369206c61742032206d61792074676c20322e706466, '2024-06-12'),
	(10, '2332002', 'kelvin', 'Ternak Ayam', '937182', _binary 0x433a2f55736572732f757365722f446f63756d656e74732f4761627269656c20546172696b68204f6d6172202832333332303533292073697374656d206f706572617369206c61742032206d61792074676c20322e706466, '2024-06-12'),
	(11, '2332002', 'kelvin', 'Ternak Ayam', '010101', _binary 0x433a2f55736572732f757365722f446f63756d656e74732f4761627269656c20546172696b68204f6d6172202832333332303533292073697374656d206f706572617369206c61742032206d61792074676c20322e706466, '2024-06-12'),
	(12, '2332053', 'Gabriel Tarikh Omar', 'Ternak Lele', '937182', _binary 0x433a2f55736572732f757365722f446f63756d656e74732f4761627269656c20546172696b68204f6d6172202832333332303533292074756761732070626f20342e342e706466, '2024-06-12'),
	(13, '2332053', 'Gabriel Tarikh Omar', 'Ternak Lele', '010101', _binary 0x433a2f55736572732f757365722f446f776e6c6f6164732f4761627269656c20546172696b68204f6d6172202832333332303533292073697374656d206f706572617369206c61742032206d61792074676c20322e706466, '2024-06-12'),
	(14, '2332002', 'kelvin', 'Ternak Ayam', '010101', _binary 0x433a2f55736572732f757365722f446f776e6c6f6164732f4761627269656c20546172696b68204f6d6172202832333332303533292073697374656d206f706572617369206c617420312074676c206d617920322e706466, '2024-06-12'),
	(15, '2332002', 'kelvin', 'Ternak Lele', '010101', _binary 0x433a2f55736572732f757365722f446f776e6c6f6164732f4761627269656c20546172696b68204f6d6172202832333332303533292073697374656d206f706572617369206c617420312074676c206d617920322e706466, '2024-06-13');

-- Dumping structure for table logbook_skripsi.detail_bimbingan_mahasiswa
CREATE TABLE IF NOT EXISTS `detail_bimbingan_mahasiswa` (
  `id_detail` int NOT NULL AUTO_INCREMENT,
  `id_mng_pembimbing` int DEFAULT NULL,
  `npm` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_detail`),
  KEY `id_mng_pembimbing` (`id_mng_pembimbing`),
  KEY `npm` (`npm`),
  CONSTRAINT `FK_detail_bimbingan_mahasiswa_mahasiswa` FOREIGN KEY (`npm`) REFERENCES `mahasiswa` (`npm`),
  CONSTRAINT `FK_detail_bimbingan_mahasiswa_management_pembimbing` FOREIGN KEY (`id_mng_pembimbing`) REFERENCES `management_pembimbing` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table logbook_skripsi.detail_bimbingan_mahasiswa: ~25 rows (approximately)
INSERT INTO `detail_bimbingan_mahasiswa` (`id_detail`, `id_mng_pembimbing`, `npm`) VALUES
	(8, 19, '2332002'),
	(9, 22, '2332002'),
	(10, 23, '2332002'),
	(11, 24, '2332002'),
	(12, 25, '2332002'),
	(13, 26, '2332002'),
	(14, 27, '2332002'),
	(15, 28, '2332002'),
	(16, 29, '2332002'),
	(17, 30, '2332002'),
	(18, 31, '2332002'),
	(19, 32, '2332002'),
	(20, 33, '2332002'),
	(21, 34, '2332002'),
	(22, 35, '2332002'),
	(23, 36, '2332002'),
	(24, 37, '2332002'),
	(25, 38, '2332002'),
	(26, 39, '2332002'),
	(27, 40, '2332053'),
	(28, 41, '2332053'),
	(29, 42, '2332053'),
	(30, 43, '2332002'),
	(31, 44, '2332002'),
	(32, 45, '2332002');

-- Dumping structure for table logbook_skripsi.dosen
CREATE TABLE IF NOT EXISTS `dosen` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nidn` varchar(50) DEFAULT NULL,
  `nama_dosen` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nidn` (`nidn`),
  KEY `nama_dosen` (`nama_dosen`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table logbook_skripsi.dosen: ~4 rows (approximately)
INSERT INTO `dosen` (`id`, `nidn`, `nama_dosen`) VALUES
	(2, '1231313', 'Stefanus'),
	(3, '937182', 'Gautama'),
	(4, '010101', 'Hendi'),
	(5, '020202', 'Andik');

-- Dumping structure for procedure logbook_skripsi.insert_management_pembimbing
DELIMITER //
CREATE PROCEDURE `insert_management_pembimbing`(
    IN p_nidn VARCHAR(50),
    IN p_npm VARCHAR(10),
    IN p_id_bimbingan_mahasiswa INT(10),
    IN p_tanggal DATE,
    IN p_konsultasi_pembimbing VARCHAR(255),
    IN p_status_validasi ENUM('approved', 'pending', 'rejected')
)
BEGIN
    DECLARE v_nama_mahasiswa VARCHAR(50);


    -- Fetch nama_mahasiswa from mahasiswa table
    SELECT nama INTO v_nama_mahasiswa
    FROM mahasiswa
    WHERE npm = p_npm;

    -- Insert into management_pembimbing table
    INSERT INTO management_pembimbing (
        nidn,
        npm,
        nama_mahasiswa,
        id_bimbingan_mahasiswa,
        tanggal,
        konsultasi_pembimbing,
        status_validasi
    ) VALUES (
        p_nidn,
        p_npm,
        v_nama_mahasiswa,
        p_id_bimbingan_mahasiswa,
        p_tanggal,
        p_konsultasi_pembimbing,
        p_status_validasi
    );
END//
DELIMITER ;

-- Dumping structure for table logbook_skripsi.logbook
CREATE TABLE IF NOT EXISTS `logbook` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `npm` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `tanggal` date NOT NULL,
  `nama_dosen` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `tugas` varchar(255) NOT NULL,
  `tujuan` varchar(255) DEFAULT NULL,
  `permasalahan_skripsi` varchar(255) DEFAULT NULL,
  `solusi` varchar(255) DEFAULT NULL,
  `tugas_minggu_depan` varchar(255) NOT NULL,
  `progress_skripsi` longblob NOT NULL,
  `status_validasi` enum('approved','pending','rejected') NOT NULL,
  `tanggal_submit` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `npm` (`npm`),
  KEY `FK_logbook_mahasiswa` (`nama`),
  KEY `FK_logbook_dosen` (`nama_dosen`),
  CONSTRAINT `FK_logbook_dosen` FOREIGN KEY (`nama_dosen`) REFERENCES `dosen` (`nama_dosen`),
  CONSTRAINT `FK_logbook_mahasiswa` FOREIGN KEY (`nama`) REFERENCES `mahasiswa` (`nama`),
  CONSTRAINT `logbook_ibfk_1` FOREIGN KEY (`npm`) REFERENCES `mahasiswa` (`npm`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table logbook_skripsi.logbook: ~16 rows (approximately)
INSERT INTO `logbook` (`id`, `nama`, `npm`, `tanggal`, `nama_dosen`, `tugas`, `tujuan`, `permasalahan_skripsi`, `solusi`, `tugas_minggu_depan`, `progress_skripsi`, `status_validasi`, `tanggal_submit`) VALUES
	(8, 'Gabriel Tarikh Omar', '2332053', '2024-06-09', 'Hendi', 'tugas', 'tujuan', 'masalah', 'solusi', 'mingdep', _binary 0x443a2f646f776e6c6f61645f6e752f323032335f5541532050424f2e706466, 'pending', '2024-06-09 16:39:34'),
	(9, 'Gabriel Tarikh Omar', '2332053', '2024-06-10', 'Stefanus', 'tugasasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd', 'asdasdasdasdasdasdasdzxczxczxczxczxczxczxczxc', 'zxczxcasdwqeqweqweqweqweqweqweqwe', 'qweqweqweqweqweqweqweqwe', 'qweqweqweqweasdasfsdfsdfsdfsdfsd', _binary 0x443a2f646f776e6c6f61645f6e752f4761627269656c20546172696b68204f6d6172283233333230353329207362642074756761735f6d616e6469726920342e706466, 'rejected', '2024-06-10 07:39:35'),
	(10, 'kelvin', '2332002', '2024-06-10', 'Stefanus', 'asdasdasdasd', 'asdasdasdasdasda', 'sdasdasdasdasd', 'asdasdasdasdasdasdasd', 'asdasdasdasdasdasd', _binary 0x443a2f646f776e6c6f61645f6e752f35372d41727469636c6520546578742d35382d312d31302d32303138303732352e706466, 'approved', '2024-06-10 08:06:23'),
	(11, 'Aleser Tarikh Omar', '2332005', '2024-06-10', 'Gautama', 'asdasdasdasd', 'asdasdasd', 'asdasdasd', 'asdasdasd', 'asdasdasd', _binary 0x443a2f646f776e6c6f61645f6e752f4761627269656c20546172696b68204f6d61722028323333323035332920627261696e7374726f6d696e672e706466, 'rejected', '2024-06-10 08:22:45'),
	(12, 'kelvin', '2332002', '2024-06-10', 'Hendi', 'asdasdasd', 'asdasdasd', 'asdasdasd', 'asdasdasdasdasdasd', 'asdasdasd', _binary 0x443a2f646f776e6c6f61645f6e752f4761627269656c20546172696b68204f6d6172202832333332303533292070726573656e746173692063617265657220706c616e732e706466, 'approved', '2024-06-10 08:24:05'),
	(13, 'aleser tarikh omar', '2332005', '2024-06-09', 'Gautama', 'asdasdasdasdasdasdasd', 'asdasd', 'asdasdasd', 'asdasd', 'asdasdasd', _binary 0x443a2f646f776e6c6f61645f6e752f31323933302d41727469636c6520546578742d36343036382d312d31302d32303233303330332e706466, 'approved', '2024-06-10 09:09:23'),
	(14, 'radahn', '2332003', '2024-06-10', 'Andik', 'asdasd', 'asdasdasd', 'asdasdasd', 'asdasd', 'asdasdasd', _binary 0x443a2f646f776e6c6f61645f6e752f4761627269656c20546172696b68204f6d61722028323333323035332920534244207475676173206d616e6469726920352e706466, 'pending', '2024-06-10 09:32:03'),
	(15, 'radahn', '2332003', '2024-06-10', 'Andik', 'asdasdasd', 'asdasdasd', 'asdasdasd', 'asdasdasd', 'asdasdasd', _binary 0x443a2f646f776e6c6f61645f6e752f31323933302d41727469636c6520546578742d36343036382d312d31302d32303233303330332e706466, 'rejected', '2024-06-10 09:36:14'),
	(16, 'kelvin', '2332002', '2024-06-10', 'Hendi', 'dasdasdasdasdasd', 'asdasd', 'asdasdasd', 'asdasdasd', 'asdasdasdas', _binary 0x443a2f646f776e6c6f61645f6e752f323032335f5541532050424f2e706466, 'pending', '2024-06-10 14:01:12'),
	(17, 'Gabriel Tarikh Omar', '2332053', '2024-06-11', 'Hendi', 'asdasdasd', 'asdasdasd', 'asdasdas', 'dasdasd', 'asdasdasd', _binary 0x443a2f646f776e6c6f61645f6e752f4761627269656c20546172696b68204f6d61722028323333323035332920736264207475676173206d616e64697269203220646d6c2061647620312e706466, 'approved', '2024-06-10 18:06:50'),
	(18, 'kelvin', '2332002', '2024-06-11', 'Stefanus', 'asdasdasd', 'asdasdasd', 'asdasdas', 'dasdasdas', 'dasdasdasd', _binary 0x443a2f646f776e6c6f61645f6e752f4761627269656c20546172696b68204f6d6172283233333230353329207362642074756761735f6d616e6469726920342e706466, 'approved', '2024-06-11 07:43:24'),
	(19, 'kelvin', '2332002', '2024-06-12', 'Hendi', 'asdasd', 'asdasdasd', 'asdasdas', 'dasdasd', 'asdasdasdasd', _binary 0x433a2f55736572732f757365722f446f63756d656e74732f4761627269656c20546172696b68204f6d6172202832333332303533292074756761732070626f20342e342e706466, 'approved', '2024-06-12 12:42:16'),
	(23, 'kelvin', '2332002', '2024-06-12', 'Hendi', 'asdasdasdasd', 'asdasdasd', 'asdasda', 'sdasdas', 'dasdasd', _binary 0x433a2f55736572732f757365722f446f63756d656e74732f4761627269656c20546172696b68204f6d6172202832333332303533292073697374656d206f706572617369206c61742032206d61792074676c20322e706466, 'pending', '2024-06-12 15:15:53'),
	(24, 'Gabriel Tarikh Omar', '2332053', '2024-06-12', 'Hendi', 'asdasd', 'asdasd', 'asdasd', 'asdasd', 'asdasd', _binary 0x433a2f55736572732f757365722f446f776e6c6f6164732f4761627269656c20546172696b68204f6d617228323333323035332920736264207475676173206d616e6469726920342e706466, 'pending', '2024-06-12 15:51:03'),
	(25, 'kelvin', '2332002', '2024-06-13', 'Hendi', 'tugasa', 'tujuan', 'masalah', 'solusi', 'tugas minggu depan', _binary 0x433a2f55736572732f757365722f446f776e6c6f6164732f4761627269656c20546172696b68204f6d617228323333323035332920736264207475676173206d616e6469726920342e706466, 'pending', '2024-06-12 18:26:15'),
	(26, 'kelvin', '2332002', '2024-06-13', 'Hendi', 'tugas', 'tujuan', 'permasalah', 'solusi', 'mingdep', _binary 0x433a2f55736572732f757365722f446f776e6c6f6164732f4761627269656c20546172696b68204f6d6172283233333230353329207362642074756761735f6d616e6469726920342e706466, 'approved', '2024-06-12 19:09:18');

-- Dumping structure for table logbook_skripsi.mahasiswa
CREATE TABLE IF NOT EXISTS `mahasiswa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `npm` varchar(10) NOT NULL,
  `prodi` varchar(50) NOT NULL,
  `nama` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `npm` (`npm`),
  KEY `prodi` (`prodi`),
  KEY `nama` (`nama`) USING BTREE,
  CONSTRAINT `mahasiswa_ibfk_1` FOREIGN KEY (`prodi`) REFERENCES `program_studi` (`prodi`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table logbook_skripsi.mahasiswa: ~4 rows (approximately)
INSERT INTO `mahasiswa` (`id`, `npm`, `prodi`, `nama`) VALUES
	(1, '2332053', 'Teknologi Informasi', 'Gabriel Tarikh Omar'),
	(2, '2332002', 'Teknologi Informasi', 'kelvin'),
	(3, '2332005', 'Sistem Informasi', 'Aleser Tarikh Omar'),
	(4, '2332003', 'Management', 'radahn');

-- Dumping structure for table logbook_skripsi.management_pembimbing
CREATE TABLE IF NOT EXISTS `management_pembimbing` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nidn` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `npm` varchar(10) NOT NULL,
  `nama_mahasiswa` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `id_bimbingan_mahasiswa` int DEFAULT NULL,
  `tanggal` date DEFAULT NULL,
  `konsultasi_pembimbing` varchar(255) NOT NULL,
  `status_validasi` enum('approved','pending','rejected') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `npm` (`npm`),
  KEY `fk_nidn` (`nidn`),
  KEY `FK_management_pembimbing_mahasiswa` (`nama_mahasiswa`),
  KEY `FK_management_pembimbing_bimbingan_mahasiswa` (`id_bimbingan_mahasiswa`),
  CONSTRAINT `FK_management_pembimbing_bimbingan_mahasiswa` FOREIGN KEY (`id_bimbingan_mahasiswa`) REFERENCES `bimbingan_mahasiswa` (`id`),
  CONSTRAINT `FK_management_pembimbing_mahasiswa` FOREIGN KEY (`nama_mahasiswa`) REFERENCES `mahasiswa` (`nama`),
  CONSTRAINT `fk_nidn` FOREIGN KEY (`nidn`) REFERENCES `dosen` (`nidn`),
  CONSTRAINT `management_pembimbing_ibfk_1` FOREIGN KEY (`npm`) REFERENCES `mahasiswa` (`npm`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table logbook_skripsi.management_pembimbing: ~32 rows (approximately)
INSERT INTO `management_pembimbing` (`id`, `nidn`, `npm`, `nama_mahasiswa`, `id_bimbingan_mahasiswa`, `tanggal`, `konsultasi_pembimbing`, `status_validasi`) VALUES
	(11, '010101', '2332002', 'kelvin', 4, '2024-06-11', 'Initial consultation', 'pending'),
	(12, '020202', '2332053', 'Gabriel Tarikh Omar', 7, '2024-06-11', 'Initial consultation', 'approved'),
	(13, '020202', '2332053', 'Gabriel Tarikh Omar', 7, '2024-06-11', 'blablbal', 'pending'),
	(14, '010101', '2332002', 'kelvin', 5, '2024-06-11', 'blablbal', 'rejected'),
	(15, '010101', '2332002', 'kelvin', 8, '2024-06-12', 'blablbal', 'rejected'),
	(17, '010101', '2332002', 'kelvin', 6, '2024-06-12', 'blablbal', 'rejected'),
	(18, '020202', '2332053', 'Gabriel Tarikh Omar', 7, '2024-06-12', 'blablbal', 'rejected'),
	(19, '010101', '2332002', 'kelvin', 6, '2024-06-12', 'blablbal', 'rejected'),
	(22, '010101', '2332002', 'kelvin', 4, '2024-06-12', 'asdasdasdasdasdasd', NULL),
	(23, '010101', '2332002', 'kelvin', 6, '2024-06-12', 'asdasdasdasdasd', 'approved'),
	(24, '937182', '2332002', 'kelvin', 9, '2024-06-12', 'asdasdasdasdasdasdasd', 'approved'),
	(25, '010101', '2332002', 'kelvin', 6, '2024-06-12', 'asdasdasdasdasd', 'pending'),
	(26, '010101', '2332002', 'kelvin', 6, '2024-06-12', 'catatan', NULL),
	(27, '010101', '2332002', 'kelvin', 5, '2024-06-12', 'catatan btl', 'approved'),
	(28, '937182', '2332002', 'kelvin', 9, '2024-06-12', 'kurang mantap', 'pending'),
	(29, '937182', '2332002', 'kelvin', 10, '2024-06-12', 'wow', 'approved'),
	(30, '937182', '2332002', 'kelvin', 10, '2024-06-12', 'kuranging', 'pending'),
	(31, '010101', '2332002', 'kelvin', 6, '2024-06-12', 'asdasdasdasd', 'rejected'),
	(32, '937182', '2332002', 'kelvin', 9, '2024-06-12', 'wow', 'rejected'),
	(33, '937182', '2332002', 'kelvin', 10, '2024-06-12', 'yg baru kek', 'pending'),
	(34, '937182', '2332002', 'kelvin', 10, '2024-06-12', 'kapan', 'approved'),
	(35, '937182', '2332002', 'kelvin', 9, '2024-06-12', 'abel', 'approved'),
	(36, '937182', '2332002', 'kelvin', 10, '2024-06-12', 'omal', 'pending'),
	(37, '937182', '2332002', 'kelvin', 10, '2024-06-12', 'alhamdullilah', 'approved'),
	(38, '937182', '2332002', 'kelvin', 10, '2024-06-12', 'lme', 'pending'),
	(39, '010101', '2332002', 'kelvin', 11, '2024-06-12', 'omal', 'rejected'),
	(40, '010101', '2332053', 'Gabriel Tarikh Omar', 13, '2024-06-12', 'gj', 'approved'),
	(41, '937182', '2332053', 'Gabriel Tarikh Omar', 12, '2024-06-12', 'lemao', 'approved'),
	(42, '937182', '2332053', 'Gabriel Tarikh Omar', 12, '2024-06-13', 'asdasdasdasd', 'approved'),
	(43, '010101', '2332002', 'kelvin', 14, '2024-06-13', 'lemao', 'pending'),
	(44, '937182', '2332002', 'kelvin', 10, '2024-06-13', 'lemao', 'approved'),
	(45, '010101', '2332002', 'kelvin', 15, '2024-06-13', 'catanata', 'rejected');

-- Dumping structure for table logbook_skripsi.program_studi
CREATE TABLE IF NOT EXISTS `program_studi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `prodi` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `prodi` (`prodi`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table logbook_skripsi.program_studi: ~3 rows (approximately)
INSERT INTO `program_studi` (`id`, `prodi`) VALUES
	(5, 'Management'),
	(3, 'Sistem Informasi'),
	(2, 'Teknologi Informasi');

-- Dumping structure for table logbook_skripsi.skripsi
CREATE TABLE IF NOT EXISTS `skripsi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `judul_skripsi` varchar(255) NOT NULL,
  `npm` varchar(10) NOT NULL,
  `prodi` varchar(50) NOT NULL,
  `konsultasi_pembimbing` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `judul_skripsi` (`judul_skripsi`),
  KEY `npm` (`npm`),
  KEY `prodi` (`prodi`),
  CONSTRAINT `skripsi_ibfk_1` FOREIGN KEY (`npm`) REFERENCES `mahasiswa` (`npm`),
  CONSTRAINT `skripsi_ibfk_2` FOREIGN KEY (`prodi`) REFERENCES `program_studi` (`prodi`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table logbook_skripsi.skripsi: ~2 rows (approximately)
INSERT INTO `skripsi` (`id`, `judul_skripsi`, `npm`, `prodi`, `konsultasi_pembimbing`) VALUES
	(1, 'Ternak Ayam', '2332053', 'Teknologi Informasi', 'tidak jelas juga'),
	(3, 'Ternak Lele', '2332002', 'Teknologi Informasi', 'Gagal jadi anak TI');

-- Dumping structure for table logbook_skripsi.user
CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `npm` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `npm` (`npm`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`npm`) REFERENCES `mahasiswa` (`npm`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table logbook_skripsi.user: ~2 rows (approximately)
INSERT INTO `user` (`id`, `username`, `password`, `npm`) VALUES
	(2, 'mahasiswa', '123', '2332002'),
	(3, 'mahasiswa_2', '123', '2332053');

-- Dumping structure for trigger logbook_skripsi.after_management_pembimbing_insert
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO';
DELIMITER //
CREATE TRIGGER `after_management_pembimbing_insert` AFTER INSERT ON `management_pembimbing` FOR EACH ROW BEGIN
    INSERT INTO detail_bimbingan_mahasiswa (id_mng_pembimbing, npm)
    VALUES (NEW.id, NEW.npm);
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

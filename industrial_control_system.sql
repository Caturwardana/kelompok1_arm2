# SQL-Front 5.1  (Build 4.16)

/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE */;
/*!40101 SET SQL_MODE='STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES */;
/*!40103 SET SQL_NOTES='ON' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;


# Host: localhost    Database: industrial_control_system
# ------------------------------------------------------
# Server version 5.5.60-log

#
# Source for table akun
#

DROP TABLE IF EXISTS `akun`;
CREATE TABLE `akun` (
  `user` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `level` varchar(50) NOT NULL,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Dumping data for table akun
#

LOCK TABLES `akun` WRITE;
/*!40000 ALTER TABLE `akun` DISABLE KEYS */;
INSERT INTO `akun` VALUES ('root_pc_lain','127616616root','all db');
INSERT INTO `akun` VALUES ('wemos','127616616','coba_wemosd1');
/*!40000 ALTER TABLE `akun` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table hvac
#

DROP TABLE IF EXISTS `hvac`;
CREATE TABLE `hvac` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `temperature` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Dumping data for table hvac
#

LOCK TABLES `hvac` WRITE;
/*!40000 ALTER TABLE `hvac` DISABLE KEYS */;
/*!40000 ALTER TABLE `hvac` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table motor
#

DROP TABLE IF EXISTS `motor`;
CREATE TABLE `motor` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `temperature` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Dumping data for table motor
#

LOCK TABLES `motor` WRITE;
/*!40000 ALTER TABLE `motor` DISABLE KEYS */;
/*!40000 ALTER TABLE `motor` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table pompa
#

DROP TABLE IF EXISTS `pompa`;
CREATE TABLE `pompa` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `temperature` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Dumping data for table pompa
#

LOCK TABLES `pompa` WRITE;
/*!40000 ALTER TABLE `pompa` DISABLE KEYS */;
/*!40000 ALTER TABLE `pompa` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table users_admin
#

DROP TABLE IF EXISTS `users_admin`;
CREATE TABLE `users_admin` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` char(60) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

#
# Dumping data for table users_admin
#

LOCK TABLES `users_admin` WRITE;
/*!40000 ALTER TABLE `users_admin` DISABLE KEYS */;
INSERT INTO `users_admin` VALUES (1,'catur','catur@register.co','$2b$12$vcmr8jukLx8GtH3C2lLjPOwlss66Zjvc1t6jYvUhRA4boUHtpYile');
INSERT INTO `users_admin` VALUES (3,'kelompok1','kelompok1.admin@arm2.tik','$2b$12$SPsOowYgzZp4Sh90B/xNseSfatqLzCeK1Br/NHp2BB/s6bCITsJ/e');
/*!40000 ALTER TABLE `users_admin` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table users_management
#

DROP TABLE IF EXISTS `users_management`;
CREATE TABLE `users_management` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` char(60) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;

#
# Dumping data for table users_management
#

LOCK TABLES `users_management` WRITE;
/*!40000 ALTER TABLE `users_management` DISABLE KEYS */;
INSERT INTO `users_management` VALUES (1,'management','management@management.co','$2b$12$9NYn10olMmE05Jrptf9./ejhaMfwbGVdWKf.bg3goUBShqRotV0.K');
INSERT INTO `users_management` VALUES (2,'catur','catur@m.co','$2b$12$4nThTB0DBZzA5C99YLOJ/..un2CWMgT.N5jTgDY220z1BpDXkEg9.');
INSERT INTO `users_management` VALUES (3,'kelompok1','kelompok1.management@arm2.tik','$2b$12$vVcctvpi6fg7fUyurhBl5OpJb.KP4sDWNTjkBg6k7DU5KVGsCVwXe');
/*!40000 ALTER TABLE `users_management` ENABLE KEYS */;
UNLOCK TABLES;

/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;

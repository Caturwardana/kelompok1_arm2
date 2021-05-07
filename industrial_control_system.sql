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
INSERT INTO `hvac` VALUES (1,'08/05/2021 05:02:58','ON',53);
INSERT INTO `hvac` VALUES (2,'08/05/2021 05:03:01','ON',57);
INSERT INTO `hvac` VALUES (3,'08/05/2021 05:03:04','ON',63);
INSERT INTO `hvac` VALUES (4,'08/05/2021 05:03:07','ON',64);
INSERT INTO `hvac` VALUES (5,'08/05/2021 05:03:10','ON',55);
INSERT INTO `hvac` VALUES (6,'08/05/2021 05:03:13','ON',67);
INSERT INTO `hvac` VALUES (7,'08/05/2021 05:03:16','ON',56);
INSERT INTO `hvac` VALUES (8,'08/05/2021 05:03:19','ON',65);
INSERT INTO `hvac` VALUES (9,'08/05/2021 05:03:22','ON',52);
INSERT INTO `hvac` VALUES (10,'08/05/2021 05:03:25','ON',59);
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
INSERT INTO `motor` VALUES (1,'08/05/2021 05:02:58','ON',56);
INSERT INTO `motor` VALUES (2,'08/05/2021 05:03:01','ON',56);
INSERT INTO `motor` VALUES (3,'08/05/2021 05:03:04','ON',57);
INSERT INTO `motor` VALUES (4,'08/05/2021 05:03:07','ON',67);
INSERT INTO `motor` VALUES (5,'08/05/2021 05:03:10','ON',65);
INSERT INTO `motor` VALUES (6,'08/05/2021 05:03:13','ON',63);
INSERT INTO `motor` VALUES (7,'08/05/2021 05:03:16','ON',59);
INSERT INTO `motor` VALUES (8,'08/05/2021 05:03:19','ON',70);
INSERT INTO `motor` VALUES (9,'08/05/2021 05:03:22','ON',59);
INSERT INTO `motor` VALUES (10,'08/05/2021 05:03:25','ON',55);
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
INSERT INTO `pompa` VALUES (1,'08/05/2021 05:02:58','ON',53);
INSERT INTO `pompa` VALUES (2,'08/05/2021 05:03:01','ON',54);
INSERT INTO `pompa` VALUES (3,'08/05/2021 05:03:04','ON',51);
INSERT INTO `pompa` VALUES (4,'08/05/2021 05:03:07','ON',59);
INSERT INTO `pompa` VALUES (5,'08/05/2021 05:03:10','ON',55);
INSERT INTO `pompa` VALUES (6,'08/05/2021 05:03:13','ON',63);
INSERT INTO `pompa` VALUES (7,'08/05/2021 05:03:16','ON',69);
INSERT INTO `pompa` VALUES (8,'08/05/2021 05:03:19','ON',61);
INSERT INTO `pompa` VALUES (9,'08/05/2021 05:03:22','ON',51);
INSERT INTO `pompa` VALUES (10,'08/05/2021 05:03:25','ON',66);
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

#
# Dumping data for table users_admin
#

LOCK TABLES `users_admin` WRITE;
/*!40000 ALTER TABLE `users_admin` DISABLE KEYS */;
INSERT INTO `users_admin` VALUES (1,'catur','catur@register.co','$2b$12$vcmr8jukLx8GtH3C2lLjPOwlss66Zjvc1t6jYvUhRA4boUHtpYile');
INSERT INTO `users_admin` VALUES (3,'kelompok1','kelompok1.admin@arm2.tik','$2b$12$SPsOowYgzZp4Sh90B/xNseSfatqLzCeK1Br/NHp2BB/s6bCITsJ/e');
INSERT INTO `users_admin` VALUES (4,'yeyen','yeyen@karunia.co','$2b$12$nn3K/CLa0Kaenl4dZvJSVunLQoXk3K9IxDUtowRVpVsO4emV8UMcW');
INSERT INTO `users_admin` VALUES (5,'catur','catur@register.co','$2b$12$0aDxWw4S33rNWAhrk5sYveROrUCyOI6.ZFD/IWhtegLtWcfRABUci');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;

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

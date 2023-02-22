-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: cosmetic_shop
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `appointmentservicetype`
--

DROP TABLE IF EXISTS `appointmentservicetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointmentservicetype` (
  `appointment_id` varchar(45) NOT NULL,
  `service_type_id` varchar(45) NOT NULL,
  PRIMARY KEY (`appointment_id`,`service_type_id`),
  KEY `service_type_id` (`service_type_id`),
  CONSTRAINT `appointmentservicetype_ibfk_1` FOREIGN KEY (`appointment_id`) REFERENCES `appointment` (`id`),
  CONSTRAINT `appointmentservicetype_ibfk_2` FOREIGN KEY (`service_type_id`) REFERENCES `servicetype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointmentservicetype`
--

LOCK TABLES `appointmentservicetype` WRITE;
/*!40000 ALTER TABLE `appointmentservicetype` DISABLE KEYS */;
INSERT INTO `appointmentservicetype` VALUES ('1a8b7454-6023-4546-80e7-bc59bbed2b40','1a36e6ae-1b3d-428a-8acd-335241ed40db'),('2393b970-84f6-4c1c-8fa9-1b20b3cc7329','1a36e6ae-1b3d-428a-8acd-335241ed40db'),('51ab0929-e08d-4ba5-86be-e324e36e8a9a','1a36e6ae-1b3d-428a-8acd-335241ed40db'),('536a9ace-15f3-4b07-b35f-416fa60ebfc3','1a36e6ae-1b3d-428a-8acd-335241ed40db'),('afca3949-9727-4871-a80a-22222c82a300','1a36e6ae-1b3d-428a-8acd-335241ed40db'),('b463c6f7-88c9-4a6d-8403-611c3c65058e','1a36e6ae-1b3d-428a-8acd-335241ed40db'),('e7330a8a-2a38-4efa-a772-3d7489f72aa7','1a36e6ae-1b3d-428a-8acd-335241ed40db'),('eb709cfa-ea9d-44ff-af80-75162942a85e','1a36e6ae-1b3d-428a-8acd-335241ed40db'),('f72e0068-7996-4c40-9a6f-0aea95bbd358','1a36e6ae-1b3d-428a-8acd-335241ed40db'),('2393b970-84f6-4c1c-8fa9-1b20b3cc7329','460c5bf4-c595-470c-80f0-5db9b7351fda'),('309a10c5-4b2b-48d1-9675-61b7599ef61e','460c5bf4-c595-470c-80f0-5db9b7351fda'),('536a9ace-15f3-4b07-b35f-416fa60ebfc3','460c5bf4-c595-470c-80f0-5db9b7351fda'),('a5b8029a-0055-411b-8412-643b22bf65f4','460c5bf4-c595-470c-80f0-5db9b7351fda'),('afca3949-9727-4871-a80a-22222c82a300','460c5bf4-c595-470c-80f0-5db9b7351fda'),('b463c6f7-88c9-4a6d-8403-611c3c65058e','460c5bf4-c595-470c-80f0-5db9b7351fda'),('cab8c9ac-9903-4791-982e-08b4851b9694','460c5bf4-c595-470c-80f0-5db9b7351fda'),('e25f21e5-5794-46c9-af59-4d15c1b2643c','460c5bf4-c595-470c-80f0-5db9b7351fda'),('e7330a8a-2a38-4efa-a772-3d7489f72aa7','460c5bf4-c595-470c-80f0-5db9b7351fda'),('eb709cfa-ea9d-44ff-af80-75162942a85e','460c5bf4-c595-470c-80f0-5db9b7351fda'),('a66ebce7-d7d8-4d17-b0e1-47c79b2d232a','6316f304-c930-43ff-903f-58126fa79e88'),('309a10c5-4b2b-48d1-9675-61b7599ef61e','ba7adfc1-522b-441f-84aa-ceb7f616ecc3'),('eb709cfa-ea9d-44ff-af80-75162942a85e','ba7adfc1-522b-441f-84aa-ceb7f616ecc3');
/*!40000 ALTER TABLE `appointmentservicetype` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 18:05:27

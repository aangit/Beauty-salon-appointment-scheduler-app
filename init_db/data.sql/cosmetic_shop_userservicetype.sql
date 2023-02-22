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
-- Table structure for table `userservicetype`
--

DROP TABLE IF EXISTS `userservicetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userservicetype` (
  `user_id` varchar(45) NOT NULL,
  `service_type_id` varchar(45) NOT NULL,
  PRIMARY KEY (`user_id`,`service_type_id`),
  KEY `service_type_id` (`service_type_id`),
  CONSTRAINT `userservicetype_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `userservicetype_ibfk_2` FOREIGN KEY (`service_type_id`) REFERENCES `servicetype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userservicetype`
--

LOCK TABLES `userservicetype` WRITE;
/*!40000 ALTER TABLE `userservicetype` DISABLE KEYS */;
INSERT INTO `userservicetype` VALUES ('5603e74e-c12b-4979-809c-1c013c7d5e43','01401bc5-5e69-4b21-9a48-eca641a120bc'),('febb9803-513a-4c16-b5cd-bbf4db1e11e7','1a36e6ae-1b3d-428a-8acd-335241ed40db'),('f2e8429a-7eb5-4a68-b2b3-66685cea779c','2b3bfba2-8fda-442f-bedb-14305bf09c26'),('f2e8429a-7eb5-4a68-b2b3-66685cea779c','47bfff7b-3f16-4cbd-9931-f102ea9854e9'),('f2e8429a-7eb5-4a68-b2b3-66685cea779c','6316f304-c930-43ff-903f-58126fa79e88'),('4d81e7dd-5d3c-42ef-ac77-a595f35300b1','7ea87821-fe53-456d-9dbe-70e8f5578241');
/*!40000 ALTER TABLE `userservicetype` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 18:05:25

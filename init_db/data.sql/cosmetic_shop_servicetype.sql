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
-- Table structure for table `servicetype`
--

DROP TABLE IF EXISTS `servicetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicetype` (
  `id` varchar(50) NOT NULL,
  `service_name` varchar(100) DEFAULT NULL,
  `approximate_duration` time DEFAULT NULL,
  `price` float DEFAULT NULL,
  `available_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicetype`
--

LOCK TABLES `servicetype` WRITE;
/*!40000 ALTER TABLE `servicetype` DISABLE KEYS */;
INSERT INTO `servicetype` VALUES ('01401bc5-5e69-4b21-9a48-eca641a120bc','Depilacija nogu','00:00:30',1000,'2023-02-21 17:14:23'),('1a36e6ae-1b3d-428a-8acd-335241ed40db','farbanje','01:00:00',1000,'2023-02-17 15:00:00'),('2b3bfba2-8fda-442f-bedb-14305bf09c26','depilacija ruku','00:00:30',600,'2023-02-21 16:31:14'),('460c5bf4-c595-470c-80f0-5db9b7351fda','manikir','01:00:00',1200,'2023-02-19 19:00:00'),('47bfff7b-3f16-4cbd-9931-f102ea9854e9','sminkanje','00:00:30',1500,'2023-02-21 19:00:00'),('6316f304-c930-43ff-903f-58126fa79e88','sminkanje i vestacke trepavice','00:00:45',2500,'2023-02-20 04:20:38'),('7ea87821-fe53-456d-9dbe-70e8f5578241','prosfesionalno sminakanje','00:00:45',2000,'2023-02-21 12:32:09'),('a005fd2e-f85c-4698-a06d-91da7094310c','trajna depilacija nogu','03:00:00',6000,'2023-02-21 13:16:57'),('ba7adfc1-522b-441f-84aa-ceb7f616ecc3','feniranje srednje duzine','00:30:00',750,'2023-02-16 14:00:00');
/*!40000 ALTER TABLE `servicetype` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 18:05:26

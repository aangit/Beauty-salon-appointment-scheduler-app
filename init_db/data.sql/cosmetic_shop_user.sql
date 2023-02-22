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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `user_type_id` (`user_type_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`user_type_id`) REFERENCES `usertype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','rodja@example.com','8bb0cf6eb9b17d0f7d22b456f121257dc1254e1f01665370476383ea776df414','0ea671f4-a66a-4ac3-bcfa-e2a27eeabbac'),('0f99f257-0b24-4e73-8cda-696a692eca48','bla@example.com','473287f8298dba7163a897908958f7c0eae733e25d2e027992ea2edc9bed2fa8','0ea671f4-a66a-4ac3-bcfa-e2a27eeabbac'),('236b5b4d-df9f-459b-9608-7f967fbdf7b4','andjela@example.com','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','0ea671f4-a66a-4ac3-bcfa-e2a27eeabbac'),('2bb6178f-3449-4d4e-ac3f-567f5aefa021','ang@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3','0ea671f4-a66a-4ac3-bcfa-e2a27eeabbac'),('3d1b887a-c64d-4489-ad23-2e980abd2b28','user2@example.com','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','0ea671f4-a66a-4ac3-bcfa-e2a27eeabbac'),('4d81e7dd-5d3c-42ef-ac77-a595f35300b1','kozmeticar@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3','27d2354b-7bc3-417a-a810-2224679960de'),('53089808-d836-47ec-970c-cd2e26fba454','andj@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3','7995fcc2-efa6-446c-85c3-37e5448ef8bc'),('5603e74e-c12b-4979-809c-1c013c7d5e43','depilator@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3','27d2354b-7bc3-417a-a810-2224679960de'),('64532ea1-b841-43ea-afc7-fe4cfa5064bc','dojcinovic@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3','0ea671f4-a66a-4ac3-bcfa-e2a27eeabbac'),('823cd39c-b2cf-43ea-9c86-722e4d3dcf6c','nikola2@example.com','8bb0cf6eb9b17d0f7d22b456f121257dc1254e1f01665370476383ea776df414','0ea671f4-a66a-4ac3-bcfa-e2a27eeabbac'),('bb3c0dc4-689d-459a-9039-4e8f0772cae9','nikola@example.com','8bb0cf6eb9b17d0f7d22b456f121257dc1254e1f01665370476383ea776df414','0ea671f4-a66a-4ac3-bcfa-e2a27eeabbac'),('e26ae2b2-0c27-4f21-a0ee-a3cb8ab93133','rodja2@example.com','8bb0cf6eb9b17d0f7d22b456f121257dc1254e1f01665370476383ea776df414','0ea671f4-a66a-4ac3-bcfa-e2a27eeabbac'),('f2e8429a-7eb5-4a68-b2b3-66685cea779c','sminker@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3','27d2354b-7bc3-417a-a810-2224679960de'),('febb9803-513a-4c16-b5cd-bbf4db1e11e7','frizer1@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3','27d2354b-7bc3-417a-a810-2224679960de');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
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

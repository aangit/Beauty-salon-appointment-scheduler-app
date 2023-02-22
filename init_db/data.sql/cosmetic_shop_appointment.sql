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
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment` (
  `id` varchar(50) NOT NULL,
  `appointment_datetime` datetime DEFAULT NULL,
  `client_id` varchar(45) DEFAULT NULL,
  `employee_id` varchar(45) DEFAULT NULL,
  `status_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `client_id` (`client_id`),
  KEY `employee_id` (`employee_id`),
  KEY `status_id` (`status_id`),
  CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `user` (`id`),
  CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `user` (`id`),
  CONSTRAINT `appointment_ibfk_3` FOREIGN KEY (`status_id`) REFERENCES `status` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` VALUES ('0262ded2-ec0d-4155-bba5-b3dc560d822b','2023-02-17 10:30:14','0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','febb9803-513a-4c16-b5cd-bbf4db1e11e7','97b0e4f9-d716-4e33-b761-3e2b21490d42'),('1a8b7454-6023-4546-80e7-bc59bbed2b40','2023-02-20 10:04:36','e26ae2b2-0c27-4f21-a0ee-a3cb8ab93133','febb9803-513a-4c16-b5cd-bbf4db1e11e7','0de32b85-ba39-423e-bee5-befa4c3a7a1d'),('2393b970-84f6-4c1c-8fa9-1b20b3cc7329','2023-02-19 18:00:32','0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','febb9803-513a-4c16-b5cd-bbf4db1e11e7','97b0e4f9-d716-4e33-b761-3e2b21490d42'),('309a10c5-4b2b-48d1-9675-61b7599ef61e','2023-02-17 14:08:49','0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','febb9803-513a-4c16-b5cd-bbf4db1e11e7','97b0e4f9-d716-4e33-b761-3e2b21490d42'),('3ae95af8-2a39-4814-8e05-861d4ede92aa','2023-02-19 19:00:32','0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','febb9803-513a-4c16-b5cd-bbf4db1e11e7','97b0e4f9-d716-4e33-b761-3e2b21490d42'),('4ed85597-247e-4446-8002-44ba94d27a00','2023-02-18 19:26:52','e26ae2b2-0c27-4f21-a0ee-a3cb8ab93133','febb9803-513a-4c16-b5cd-bbf4db1e11e7','39e0b0ad-9b7a-4f02-8149-30017f1eeb0d'),('51ab0929-e08d-4ba5-86be-e324e36e8a9a','2023-02-20 06:29:36','236b5b4d-df9f-459b-9608-7f967fbdf7b4','f2e8429a-7eb5-4a68-b2b3-66685cea779c','0de32b85-ba39-423e-bee5-befa4c3a7a1d'),('536a9ace-15f3-4b07-b35f-416fa60ebfc3','2023-02-19 19:00:32','0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','febb9803-513a-4c16-b5cd-bbf4db1e11e7','0de32b85-ba39-423e-bee5-befa4c3a7a1d'),('55dfc283-2f84-41a7-8782-922f64f7ba33','2023-02-17 13:37:08','0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','febb9803-513a-4c16-b5cd-bbf4db1e11e7','97b0e4f9-d716-4e33-b761-3e2b21490d42'),('641489bb-6ce2-47b7-a916-e5936a3ca332','2023-02-20 04:44:07','64532ea1-b841-43ea-afc7-fe4cfa5064bc','febb9803-513a-4c16-b5cd-bbf4db1e11e7','0de32b85-ba39-423e-bee5-befa4c3a7a1d'),('74666d94-2353-4695-a5d8-c5a2f47ce6be','2023-02-17 14:00:21','0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','febb9803-513a-4c16-b5cd-bbf4db1e11e7','0de32b85-ba39-423e-bee5-befa4c3a7a1d'),('a5b8029a-0055-411b-8412-643b22bf65f4','2023-02-20 06:10:01','e26ae2b2-0c27-4f21-a0ee-a3cb8ab93133','febb9803-513a-4c16-b5cd-bbf4db1e11e7','0de32b85-ba39-423e-bee5-befa4c3a7a1d'),('a66ebce7-d7d8-4d17-b0e1-47c79b2d232a','2023-02-20 05:44:07','64532ea1-b841-43ea-afc7-fe4cfa5064bc','febb9803-513a-4c16-b5cd-bbf4db1e11e7','0de32b85-ba39-423e-bee5-befa4c3a7a1d'),('afca3949-9727-4871-a80a-22222c82a300','2023-02-19 19:00:32','0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','febb9803-513a-4c16-b5cd-bbf4db1e11e7','0de32b85-ba39-423e-bee5-befa4c3a7a1d'),('b463c6f7-88c9-4a6d-8403-611c3c65058e','2023-02-19 19:00:32','0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','febb9803-513a-4c16-b5cd-bbf4db1e11e7','0de32b85-ba39-423e-bee5-befa4c3a7a1d'),('c0cfdf0f-b452-4d88-8335-77e74ed34e2f','2023-02-18 19:26:52','e26ae2b2-0c27-4f21-a0ee-a3cb8ab93133','febb9803-513a-4c16-b5cd-bbf4db1e11e7','97b0e4f9-d716-4e33-b761-3e2b21490d42'),('cab8c9ac-9903-4791-982e-08b4851b9694','2023-02-20 06:03:44','bb3c0dc4-689d-459a-9039-4e8f0772cae9','e26ae2b2-0c27-4f21-a0ee-a3cb8ab93133','0de32b85-ba39-423e-bee5-befa4c3a7a1d'),('db19b295-4940-4f66-ac6c-0944e67ec086','2023-02-17 13:37:08','0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','febb9803-513a-4c16-b5cd-bbf4db1e11e7','97b0e4f9-d716-4e33-b761-3e2b21490d42'),('dccc3067-f89f-49fd-b30f-a6b27ecd9551','2023-02-20 05:44:07','64532ea1-b841-43ea-afc7-fe4cfa5064bc','febb9803-513a-4c16-b5cd-bbf4db1e11e7','0de32b85-ba39-423e-bee5-befa4c3a7a1d'),('e25f21e5-5794-46c9-af59-4d15c1b2643c','2023-02-20 06:10:01','e26ae2b2-0c27-4f21-a0ee-a3cb8ab93133','f2e8429a-7eb5-4a68-b2b3-66685cea779c','0de32b85-ba39-423e-bee5-befa4c3a7a1d'),('e3d2c18f-9b91-47bc-9a5a-b527a4e6c7be','2023-02-17 13:46:27','0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','febb9803-513a-4c16-b5cd-bbf4db1e11e7','97b0e4f9-d716-4e33-b761-3e2b21490d42'),('e7330a8a-2a38-4efa-a772-3d7489f72aa7','2023-02-19 17:00:32','0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','febb9803-513a-4c16-b5cd-bbf4db1e11e7','97b0e4f9-d716-4e33-b761-3e2b21490d42'),('eb709cfa-ea9d-44ff-af80-75162942a85e','2023-02-19 15:00:32','0f5fa1fb-de1d-4a6b-84e0-e7de4fb7889f','febb9803-513a-4c16-b5cd-bbf4db1e11e7','97b0e4f9-d716-4e33-b761-3e2b21490d42'),('f72e0068-7996-4c40-9a6f-0aea95bbd358','2023-02-20 05:46:33','e26ae2b2-0c27-4f21-a0ee-a3cb8ab93133','bb3c0dc4-689d-459a-9039-4e8f0772cae9','0de32b85-ba39-423e-bee5-befa4c3a7a1d');
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
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

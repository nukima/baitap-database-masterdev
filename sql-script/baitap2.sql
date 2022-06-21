-- Create tabel users
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `fullname` varchar(45) DEFAULT NULL,
  `province` varchar(3) DEFAULT NULL,
  `age` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=1067458 DEFAULT CHARSET=utf8mb4

-- --------------------------------------------------------
-- --
-- top 10 users by age from SG
SELECT * from masterdev_manhnk9.users u WHERE u.province = "SG" ORDER BY u.age DESC LIMIT 10; 

-- search username ghtk
SELECT * from masterdev_manhnk9.users u where u.username = "ghtk";

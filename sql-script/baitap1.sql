-- Create tables
CREATE TABLE `lecturers` (
  `lec_id` int(10) unsigned NOT NULL,
  `lec_name` varchar(50) NOT NULL,
  `lec_sex` tinyint(4) DEFAULT NULL,
  `lec_email` varchar(50) DEFAULT NULL,
  `subject_id` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`lec_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

CREATE TABLE `students` (
  `stu_id` int(10) unsigned NOT NULL,
  `stu_name` varchar(50) NOT NULL,
  `stu_sex` tinyint(4) DEFAULT NULL,
  `stu_email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

CREATE TABLE `classes` (
  `class_id` int(10) unsigned NOT NULL,
  `lec_id` int(10) unsigned NOT NULL,
  `class_name` varchar(50) NOT NULL,
  PRIMARY KEY (`class_id`),
  UNIQUE KEY `class_name` (`class_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

CREATE TABLE `subjects` (
  `sub_id` int(10) unsigned NOT NULL,
  `sub_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`sub_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

CREATE TABLE `class_student` (
  `class_id` int(10) unsigned NOT NULL,
  `student_id` int(10) unsigned NOT NULL,
  `scores` float(3,1) unsigned DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1

-- --------------------------------------------------------
-- --
-- Get average score of all students
SELECT AVG(scores) FROM class_student;

-- Ratio of failed students
SELECT (
  (SELECT COUNT(*) FROM class_student WHERE scores < 4) / (SELECT COUNT(*) FROM class_student)
) AS fail_ratio;

-- Ratio of average students
SELECT (
  (SELECT COUNT(*) FROM class_student WHERE scores >= 4 AND scores < 6) / (SELECT COUNT(*) FROM class_student)
) AS avg_ratio;

-- Ratio of good students
SELECT (
  (SELECT COUNT(*) FROM class_student WHERE scores >= 6 AND scores < 8) / (SELECT COUNT(*) FROM class_student)
) AS good_ratio;

-- Ratio of very good students
SELECT (
  (SELECT COUNT(*) FROM class_student WHERE scores >= 8 AND scores < 9) / (SELECT COUNT(*) FROM class_student)
) AS very_good_ratio;

-- Ration of excellent students
SELECT (
  (SELECT COUNT(*) FROM class_student WHERE scores >= 9) / (SELECT COUNT(*) FROM class_student)
) AS excellent_ratio;

-- Get subject which has the highest average score
SELECT s.sub_id, s.sub_name 
FROM masterdev_manhnk9.subjects s 
    INNER JOIN masterdev_manhnk9.lecturers l 
    ON s.sub_id = l.subject_id 
    INNER JOIN masterdev_manhnk9.classes c 
    ON c.lec_id = l.lec_id 
    INNER JOIN masterdev_manhnk9.class_student cs 
    ON cs.class_id = c.class_id 
GROUP BY s.sub_id 
ORDER BY AVG(cs.scores) DESC 
LIMIT 1;

-- Get class which has the highest average score
SELECT cs.class_id, AVG(cs.scores) avg_score
FROM masterdev_manhnk9.class_student cs 
GROUP BY cs.class_id
ORDER BY avg_score DESC
LIMIT 1;

-- Get student which has the highest average score
SELECT s.stu_id , s.stu_name , s.stu_sex , s.stu_email , AVG(cs.scores) avg_score
FROM masterdev_manhnk9.students s 
	INNER JOIN masterdev_manhnk9.class_student cs 
	ON s.stu_id = cs.student_id 
GROUP BY s.stu_id 
ORDER BY avg_score DESC
LIMIT 1;

-- Get subject which has the highest ratio of failed students
SELECT s.sub_id, s.sub_name, COUNT(CASE WHEN cs.scores < 4 THEN 1 ELSE NULL END) / COUNT(cs.student_id) failed_ratio
FROM masterdev_manhnk9.subjects s 
	INNER JOIN masterdev_manhnk9.lecturers l 
	ON s.sub_id = l.subject_id 
	INNER JOIN masterdev_manhnk9.classes c 
	ON c.lec_id = l.lec_id 
	INNER JOIN masterdev_manhnk9.class_student cs 
	ON cs.class_id = c.class_id 
GROUP BY s.sub_id
LIMIT 1;

-- List students who don't fail in any class (errcode 28)
SELECT tmp.student_id
FROM
(SELECT cs.student_id, COUNT(cs.class_id) total_class, COUNT(CASE WHEN cs.scores >= 4 THEN 1 ELSE NULL END) passed
FROM masterdev_manhnk9.class_student cs 
GROUP BY cs.student_id) AS tmp
WHERE tmp.total_class = passed;


-- Top 10 difficult subjects
SELECT s.sub_id, s.sub_name 
FROM masterdev_manhnk9.subjects s 
    INNER JOIN masterdev_manhnk9.lecturers l 
    ON s.sub_id = l.subject_id 
    INNER JOIN masterdev_manhnk9.classes c 
    ON c.lec_id = l.lec_id 
    INNER JOIN masterdev_manhnk9.class_student cs 
    ON cs.class_id = c.class_id 
GROUP BY s.sub_id 
ORDER BY AVG(cs.scores) ASC 
LIMIT 10;


CREATE DATABASE favoritesData;
use favoritesData;

CREATE TABLE userData (
  `user_id` VARCHAR(30) NOT NULL,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`user_id`)
);

CREATE TABLE favorits (
  `id` int AUTO_INCREMENT,
  `user_id` VARCHAR(30),
  `song_name` VARCHAR(255),
  `song_link` VARCHAR(512) CHARACTER SET 'ascii' COLLATE 'ascii_general_ci',
  `song_image` VARCHAR(512) CHARACTER SET 'ascii' COLLATE 'ascii_general_ci',
  `artist_name` varchar(255),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES userData(`user_id`)
);


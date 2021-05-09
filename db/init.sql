CREATE DATABASE favoritesData;
use favoritesData;

CREATE TABLE userData (
  `user_id` VARCHAR(30) NOT NULL,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`user_id`)
);

INSERT INTO userData (user_id,first_name,last_name) VALUES
    ('109613092934114349003', 'Aman', 'Hirpara');

CREATE TABLE favorits (
  `id` int AUTO_INCREMENT,
  `user_id` VARCHAR(30),
  `song_name` VARCHAR(255),
  `song_link` VARCHAR(512) CHARACTER SET 'ascii' COLLATE 'ascii_general_ci' NOT NULL,
  `song_image` VARCHAR(512) CHARACTER SET 'ascii' COLLATE 'ascii_general_ci' NOT NULL,
  `artist_name` varchar(255),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES userData(`user_id`)
);

INSERT INTO favorits (user_id,song_name,song_link, song_image, artist_name) VALUES
    ('109613092934114349003', 'Khairiyat', 'https://p.scdn.co/mp3-preview/675f140e389a20b604070b22ea03d1bfefa70200?cid=ddec4b5bf0dc4e2890a68cf1fbd2adf2','https://i.scdn.co/image/ab67616d0000b273eaa6b4bfb5954ee5a5a8ce9e', 'Arijit Singh');

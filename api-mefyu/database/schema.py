users = (
  "CREATE TABLE `users` ("
  " `id` BIGINT NOT NULL AUTO_INCREMENT,"
  " `name` VARCHAR(100) NOT NULL,"
  " `username` VARCHAR(14) NOT NULL,"
  " `email` VARCHAR(50) NOT NULL,"
  " `password` VARCHAR(255) NOT NULL,"
  " PRIMARY KEY (`id`),"
  " UNIQUE (`email`)"
  ") ENGINE=InnoDB"
)

posts = (
  "CREATE TABLE `posts` ("
  " `id` BIGINT NOT NULL AUTO_INCREMENT,"
  " `user_id` BIGINT NOT NULL,"
  " `description` TEXT NOT NULL,"
  " `image_or_video` VARCHAR(255) DEFAULT NULL,"
  " PRIMARY KEY (`id`),"
  " FOREIGN KEY (`user_id`) REFERENCES users(id)"
  ") ENGINE=InnoDB"
)
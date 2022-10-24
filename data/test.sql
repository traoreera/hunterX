CrEATE DATABASE users
CREATE TABLE `users`.`information` (
    `id` INT(100) NOT NULL AUTO_INCREMENT ,
    `user_name` VARCHAR(100) NOT NULL , 
    `gmail` VARCHAR(100) NULL , 
    `passwords` VARCHAR(100) NOT NULL , 
    PRIMARY KEY (`id`)
)ENGINE = MyISAM;
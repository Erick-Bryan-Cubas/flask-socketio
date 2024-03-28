CREATE TABLE `testingdb`.`tbl_user` (
  `userid` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NULL DEFAULT 'utf8_general_ci',
  `useremail` VARCHAR(100) NULL DEFAULT 'utf8_general_ci',
  `userpassword` VARCHAR(50) NULL DEFAULT 'utf8_general_ci',
  PRIMARY KEY (`userid`));

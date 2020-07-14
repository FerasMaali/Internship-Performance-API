CREATE DATABASE IF NOT EXISTS `performance_api_app`;
USE `performance_api_app`;

CREATE TABLE IF NOT EXISTS `cpu_usage`(
  `usage`     DECIMAL(5,2) NOT NULL,
  `taken_at`  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  INDEX(`taken_at`)
);

CREATE TABLE IF NOT EXISTS `mem_usage`(
  `used`     BIGINT NOT NULL,
  `free`     BIGINT NOT NULL,
  `taken_at`  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  INDEX(`taken_at`)
);

CREATE TABLE IF NOT EXISTS `disk_usage`(
  `used`     BIGINT NOT NULL,
  `free`     BIGINT NOT NULL,
  `taken_at`  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  INDEX(`taken_at`)
);


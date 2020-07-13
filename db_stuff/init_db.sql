CREATE DATABASE `performance_api_app`;
USE `performance_api_app`;

CREATE TABLE `cpu_usage`(
  `usage`     DECIMAL(5,2) NOT NULL,
  `taken_at`  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  INDEX(`taken_at`)
);

CREATE TABLE `mem_usage`(
  `used`     BIGINT NOT NULL,
  `free`     BIGINT NOT NULL,
  `taken_at`  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  INDEX(`taken_at`)
);

CREATE TABLE `disk_usage`(
  `used`     BIGINT NOT NULL,
  `free`     BIGINT NOT NULL,
  `taken_at`  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  INDEX(`taken_at`)
);


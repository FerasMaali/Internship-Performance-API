# Internship-Performance-API

## Introduction
In this task, I implemented an API that provides info about the system it is running on

## General Structure
- The system we are deploying to is assumed to be Centos7
- Used Python 3 and Flask to build the API
- Used Mysql to store the collected data
- Used cron jobs and shell scripts to collect data and store it in the DB
- Each one of the web server and Mysql server was deployed to a separate Docker container
- Used Docker Compose to manage running these two containers
- Used Ansible to deploy our API
- Used Ansible Vault to manage our secrets (Mysql & Github credentials)

## The API
| API              | Description                                                                                              | Example Output                                                                       |
|------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| /cpu             | Returns the CPU usage metrics retrieved from the database for the last week                              |                                                                                      |
| /cpu_average     | Returns cpu average usage as a percentage                                                                | { "cpu_avg_usage": 11.468966 }                                                       |
| /memory          | Returns the memory usage metrics retrieved from the database for the last week (free and used in bytes)  |                                                                                      |
| /memory_average  | Returns memory average free and used space in bytes                                                      | { "memory_avg_free_space": 237231668.2449, "memory_avg_used_space": 623844916.2449 } |
| /storage         | Returns the storage usage metrics retrieved from the database for the last week (free and used in bytes) |                                                                                      |
| /storage_average | Returns storage average free and used space in bytes                                                     | { "disk_avg_free_space": 4436898619.4747, "disk_avg_used_space": 6290033860.5253 }   |

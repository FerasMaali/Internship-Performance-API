# Internship-Performance-API

## Introduction
In this task, I implemented an API that provides info about the system it is running on. See [Demo](#Demo)

## General Structure

### Assumptions
- The system we are setting our app on is assumed to be Centos7
- We have root privileges on that system

### Web App
- Used Python 3 and Flask framework to build the API
- The web app works on a Docker container and was built using [Dockerfile.web](https://github.com/FerasMaali/Internship-Performance-API/blob/master/Dockerfile.web)
- Used this [script](https://github.com/ufoscout/docker-compose-wait) to make web app wait until db is ready (since it needs some initiallization time)

### Database
- Used Mysql to store the collected data about the system
- Used cron jobs and shell scripts to collect data and store it in the DB
- Mysql server was set up using a separate Docker container which was built using [Dockerfile.db](https://github.com/FerasMaali/Internship-Performance-API/blob/master/Dockerfile.db)

### Data collection
- Used a script that collects current usage of system resources and stores info in the database
- Created a cron job to call this script every specific period of time

### Miscellaneous
- Used Docker Compose to manage running these two containers
- Used Ansible to set up our API
- Used Ansible Vault to manage our secrets (Mysql & Github credentials)

## The API
| API              | Description                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------|
| /cpu             | Returns the CPU usage metrics retrieved from the database for the last week                              |
| /cpu_average     | Returns cpu average usage as a percentage                                                                |
| /memory          | Returns the memory usage metrics retrieved from the database for the last week (free and used in bytes)  |
| /memory_average  | Returns memory average free and used space in bytes                                                      |
| /storage         | Returns the storage usage metrics retrieved from the database for the last week (free and used in bytes) |
| /storage_average | Returns storage average free and used space in bytes                                                     |
| /current         | returns the current CPU/Memory/Disk usage currently(run the commands on the node in the API call)        |

## Demo

### Control Node (Click to watch)
[![Control node asciicast](https://asciinema.org/a/uNvlcmlpMzNq8DGDOpUBCtwD6.png)](https://asciinema.org/a/uNvlcmlpMzNq8DGDOpUBCtwD6)

### Target Node (Click to watch)
[![Target node asciicast](https://asciinema.org/a/s7i1omhQPUX0r2c8S5HG1A962.png)](https://asciinema.org/a/s7i1omhQPUX0r2c8S5HG1A962)

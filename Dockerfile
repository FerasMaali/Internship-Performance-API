# The base image
FROM python:3

# the base directory for our code
RUN mkdir /code
WORKDIR /code

# install the dependencies
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

## Add the wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

VOLUME ["/code"]
EXPOSE 5000

COPY startup.sh /startup.sh
RUN chmod +x /startup.sh
CMD ["/startup.sh"]

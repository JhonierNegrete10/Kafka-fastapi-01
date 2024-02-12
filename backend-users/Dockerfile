#Dockerfile
FROM python:3.9

RUN apt-get update -y \
    && apt-get install -y iputils-ping \
    && apt-get install -y net-tools

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# Add docker-compose-wait tool -------------------
# ENV WAIT_VERSION 2.7.2
# ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait ./wait
# RUN chmod +x ./wait

CMD [ "python", "main.py"]
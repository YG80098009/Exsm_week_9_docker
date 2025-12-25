# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume

### Create the volume

```bash
docker volume create fastapi-db
```

## Server 1
cd server1
### Build the image

```bash
docker build -t shopping-server1:v1 .
```

### Run the container

```bash
docker run -d --name server1 -p 8001:8000 -v fastapi-db:/app/db shopping-server1:v1

```

## Server 2
cd ..
cd server2
### Build the image

```bash
docker build -t shopping-server2:v1 .
```

### Run the container

```bash
docker run -d --name server2 -p 8002:8000 -v fastapi-db:/app/db -v ${PWD}/data:/app/data shopping-server2:v1

```


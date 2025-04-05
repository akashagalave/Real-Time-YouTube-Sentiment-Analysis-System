#!/bin/bash
# Log everything to start_docker.log
exec > /home/ubuntu/start_docker.log 2>&1

echo "Logging in to ECR..."
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 868402157267.dkr.ecr.us-east-1.amazonaws.com

echo "Pulling Docker image..."
docker pull 868402157267.dkr.ecr.us-east-1.amazonaws.com/youtube-comments-analysis:latest

echo "Checking for existing container..."
if [ "$(docker ps -q -f name=akash-app)" ]; then
    echo "Stopping existing container..."
    docker stop akash-app
fi

if [ "$(docker ps -aq -f name=akash-app)" ]; then
    echo "Removing existing container..."
    docker rm akash-app
fi

echo "Starting new container..."
docker run -d -p 80:5000 --name akash-app 868402157267.dkr.ecr.us-east-1.amazonaws.com/youtube-comments-analysis:latest

echo "Container started successfully."
#!bin/bash

cd ~/docker_compose
echo "Pulling latest code"
git pull origin main
echo "Stopping old container...."
sudo docker compose down
echo "Starting updated containers..."
sudo docker compose up -d --build
echo "Deployment Successful !!!!!!"

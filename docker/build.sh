#!/bin/sh

docker  build -t dyservice-api:1.0.0  .
docker run -d --name dyservice-api --network host -v /etc/localtime:/etc/localtime:ro -v /etc/dyservice:/etc/dyservice  --restart unless-stopped dyservice-api:1.0.0




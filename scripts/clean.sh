#!/bin/bash

docker service update --image robertsiberry/service_1:latest service_1
docker service update --image robertsiberry/service_2:latest service_2
docker service update --image robertsiberry/service_3:latest service_3
docker service update --image robertsiberry/service_4:latest service_4
docker rmi $(docker images -f "dangling=true" -q) -f

docker system prune -f
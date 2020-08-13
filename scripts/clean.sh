#!/bin/bash

docker service update --image robertsiberry/service_1:latest fopnpservice_service_1
docker service update --image robertsiberry/service_2:latest fopnpservice_service_2
docker service update --image robertsiberry/service_3:latest fopnpservice_service_3
docker service update --image robertsiberry/service_4:latest fopnpservice_service_4
docker rmi $(docker images -f "dangling=true" -q) -f

docker system prune -f
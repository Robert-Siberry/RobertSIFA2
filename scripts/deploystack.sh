#!/bin/bash
source /var/lib/jenkins/.bashrc
docker stack deploy --compose-file docker-compose.yaml fopnpservice

#updated the name of the file
#!/bin/bash

#build planner
docker build -t planner -f planner/planner.dockerfile planner
#docker compose up

#x-terminal-emulator -e /bin/bash

#buid worker
docker build -t worker -f worker/worker.dockerfile worker

#buide network
docker network create spider

#create containers running
bash planner-run.sh
bash worker-run.sh
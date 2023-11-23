docker stop server4 server3 server2 server1
docker rm $(docker ps -a -q)
docker system prune -a
docker network rm pingpongnet
docker images

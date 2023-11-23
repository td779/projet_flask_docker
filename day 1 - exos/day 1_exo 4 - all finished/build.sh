docker build -t server4 -f server_4.dockerfile .
docker build -t server3 -f server_3.dockerfile .
docker build -t server2 -f server_2.dockerfile .
docker build -t server1 -f server_1.dockerfile .
docker network create pingpongnet
docker images


docker stop personal_landing
docker rm personal_landing
docker run -it -d -v $(pwd):/opt/app --restart=always -p 8081:80 --name=personal_landing $(docker build -q .)
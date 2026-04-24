docker stop personal_landing
docker rm personal_landing
docker build -t personal_landing .
docker run -it -d --restart=always -p 80:80 --name=personal_landing personal_landing

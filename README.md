# Docker Flask Hello World Application

## Clone with:  

git clone https://github.com/gerdmestdagh/docker_flask_helloworld.github

## Build docker with:

docker build -t helloworld .

## run Hello world on outside port 8888 in development :

docker run -t -i -e FLASK_ENV=Development -p 8888:5000 helloworld


## run Hello world on outside port 8888 in testing :

docker run -t -i -e FLASK_ENV=Testing -p 8888:5000 helloworld


## run Hello world on outside port 8888 in production :

docker run -t -i -e FLASK_ENV=Production -p 8888:5000 helloworld

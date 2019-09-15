## docker image build

```
# docker build -t <container_name> .
$ docker build -t container-base .

# docker build -t <container_name> . -f Dockerfile_base
$ docker build -t container-base . -f Dockerfile_base

# docker container 실행하고 쉘 진입
# docker run --rm -it <container_name>
$ docker run --rm -it container-base

# docker connect port
# docker run -p <local port:docker port> <container_name>
$ docker run -p 8080:4567 container

# delete all docker container
$ docker rm $(docker ps -a -q)

# delete none images(build failed images)
$ docker rmi -f $(docker images --filter "dangling=true" -q)
```

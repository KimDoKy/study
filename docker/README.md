# Docker commands

## Docker Image Commands

### DCT

```
export DOCKER_CONTENT_TRUST=1 (1: enable / 0: diable)
```

설정시 DCTS에서 인증을 통해서 다운

#### docker image directory
`/var/lib/docker/overlay`


### image detail info

```
> docker image inspect imagename   p.100
 ->  return json
```

### inspect filltering

```
> docker inspect --format="{{.Os}}" centos:6 
> docker inspect --format="{{.ContainerConfig.Image}}" centos:6
```

### tag

```
> docker image tag origing_image tag_name
> docker image tag nginx test_nginx/nginx:1.0
```

### docker search

````
> docker search nginx
```

### delete image

- `-f` : 강제 옵션 (구동중인 컨테이너가 있어도 삭제됨 / 우선 컨테이너부터 확인하고 해야함)
- 컨테이너 중지: `> docker container stop [container id]` # 레퍼런스 이미지도 같이 삭제됨
```
> docker image rm image_name/tag
> docker image rm -f image_id (3글자 이상)
> docker image prune [option]
> docker rmi image_id
> docker rm $(docker ps -a -q)   # 컨테이너 전체 삭제
> docker rmi $(docker images -q)  # 이미지 전체 삭제
```

## Docker image upload (docker hub) / public

### docker hub login
```
> docker login  # 이메일 주소가 아님
```

### push
image에 대해 태그를 먼저 지정하고 push
```
> docker tag [image_name:tag] [repo:tag]
> docker push [repo:tag]
ex.
> docker tag mysql:5.7 leafunk/docker-practice:mysql_v1
> docker push leafunk/docker-practice:mysql_v1
```

### pull
```
> docker pull leafunk/docker-practice:mysql_v1
```


```
> docker container stats conainer_id
```

!! 이미지가 잘못 되었다면 컨테이너가 생성되지 않음

## 이미지 구조
```
> sudo su -
> cd /var/lib/docker/overlay2/image_num/diff/
```

### Docker container run = create + start + sttach
```
> docker create -it --name myubuntu ubuntu:16.04
> docker ps -a
> docker start myubuntu
> docker attach myubuntu
```

### 내부에서 실행
```
> docker container run -d centos /bin/ping localhost
> docker logs -t [container_id]  # -f 옵션은 실시간
> docker container stop [container id]
> docker container ps
> docker logs -t [container id]  # ping  멈춘거 확인

> docker run -it --restart=always centos /bin/bash
> exit   # shutdown을 하더라도 container 가 멈추지 않는다.
```

## container monitoring
```
# apt-get install htop
 ```

## container network(bridge network)
```
# apt-get install bridge-utils
# brctl show
```

## docker network create (대역대를 바꾸기)

- 동일 네트워크에 대해 여러 container를 연결할 수 있다.
- container 의 이름이나 MAC, IP 주소로 서로 통신

```
> docker network create -d [network] [network_name]
> docker network create -d bridge websp-net
> docker run --net=[network_name] -it centos
# yum -y install net-tools && ifconfig
> docker network ls
> brctl show
> docker network inspect bridge
> ifconfig   # 172.18.0.1 으로 다른 대역대의 br-XXX 의 네트워크 확인
```

```
> ip route
> in link
```

```
> sudo ip link set dev docker0 down
> sudo ip addr add 192.168.99.0/24 dev docker0  (docker0의 ip를 변경할 수 있다.)
> sudo ip link set dev docker0 up
```

---

### 커스텀한 네트워크 서로 통신 확인
```
> docker network create appdb-net
> docker network ls
> sudo apt-get install bridge-utils
> brctl show
T2 > docker run --name ubuntu1 -it --network=appdb-net ubunt:16.04 /bin/bash
T3 > docker run --name ubuntu2 -it --network=appdb-net ubunt:16.04 /bin/bash
> brctl show
# apt-get update
# apt-get install net-tools && ifconfig
# apt-get install -y iputils-ping
# ifconfig
# ping ubuntu2   # 상대방과 ping 확인

> docker stats
```

---

```
> docker run -d --expose=1212 -p 80 nginx
> docker container ps
> docker run -d -P - p 80 nginx
> docker container ps
> sudo netstat -nlp | grep port_num


ps -ef | grep docker-proxy
```

### docker container  외부 노출을 위한 간단한 포트 매핑

```
> docker run -it --name mywebserver -p 80:80 ubuntu:14.04
# apt-get install apache2 -y
# service apach2 start
# [CTR + P,Q]
```

### container DNS  server settings

```
> docker run -d -dns=192.168.1.1 nginx
> docker run -d --mac-address="92:d0:c5:d5:e4:66" centos   #임의의 mac address
> docker inspect --format="{{.Cofing.MacAddress}}" [container_id]
> docker run -it --add-host=test.com:192.168.1.1 centos
# cat /etc/hosts
# 호스트명과 추가 호스트명 설정
> docker run -it --hostname=www.test.com --add-host=node1.test.com:192.168.1.1 centos
# cat /etc/hosts
# ping 192.168.56.101
# ping 192.168.56.1
```

## monitoring tool: CAdvisor

```
> docker run \
> --volume=/:/rootfs:ro \
> --volume=/var/run:/var/run:rw \
> --volume=/sys:/sys:ro \
> --volume=/var/lib/docker/:/var/lib/docker:ro \
> --publish=8080:8080
> --detach=true \
> --name=cadvisor \
> google/cadvisor:latest

-> ip:8080 (chrome)
```
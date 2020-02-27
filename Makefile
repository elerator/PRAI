all: build run wait test
build: rm
	docker build --build-arg http_proxy=http://10.4.55.31:8080/ --build-arg https_proxy=http://10.4.55.31:8080/ -t prai_information_desk .
run:
	docker run --name prai_information_desk -d -p 31755:5000 prai_information_desk
stop:
	-docker stop prai_information_desk
rm: stop
	-docker rm prai_information_desk
rmi: stop rm
	-docker rmi prai_information_desk
wait:
	sleep 10
test:
	-curl http://localhost:31755/ping
	docker logs prai_information_desk


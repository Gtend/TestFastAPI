FROM ubuntu:latest
LABEL authors="gtend"

ENTRYPOINT ["top", "-b"]
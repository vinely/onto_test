FROM alpine:latest

LABEL maintainer="vinely@126.com"

ENV ONTOLOGY_PATH /var/ontology
#ARG ALPINE_MIRROR=https://mirror.tuna.tsinghua.edu.cn/alpine/v3.8/main/

RUN mkdir -p $ONTOLOGY_PATH
COPY ontology $ONTOLOGY_PATH
EXPOSE 20334 20335 20336 20337 20338 20339
WORKDIR $ONTOLOGY_PATH
ENTRYPOINT ["./ontology"]

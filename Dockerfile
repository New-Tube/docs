FROM --platform=linux/amd64 ubuntu:22.04 as builder

RUN apt-get update
RUN apt-get install -y wget python3

WORKDIR /build

RUN wget https://jsight.io/downloads/jsight-cli/1.0.0/linux-x64/jsight
RUN mv jsight /usr/local/bin
RUN chmod +x /usr/local/bin/jsight

COPY . . 

RUN mkdir static
RUN python3 generate.py



FROM nginx:stable-alpine3.17

COPY --from=builder /build/static /usr/share/nginx/html


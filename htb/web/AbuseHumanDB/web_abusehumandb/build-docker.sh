#!/bin/bash
docker rm -f web_abusehumandb
docker build --platform linux/amd64 -t web_abusehumandb . 
docker run --name=web_abusehumandb --rm -p1337:1337 -it web_abusehumandb

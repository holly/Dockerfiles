#!/bin/bash

set -e
set -u

TAG=holly/lambda_notification_console_login

docker build -t $TAG:latest  . 

echo "=============================="
echo "docker run --rm -it --mount type=bind,src=/data/lambda_notification_console_login,dst=/data -it $TAG"
echo "=============================="

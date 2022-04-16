#!/bin/bash

set -e
set -u

# 
# docker run --rm -it --mount type=bind,src=/path/to/host_directory,dst=/data holly/python

if [ -z "$LAMBDA_ZIP_ARCHIVE" ]; then
    LAMBDA_ZIP_ARCHIVE=/data/my-deployment-package.zip 
fi

if python lambda_function.py | grep ok; then
    pushd package
    zip -r $LAMBDA_ZIP_ARCHIVE .
    popd
    zip -r $LAMBDA_ZIP_ARCHIVE lambda_function.py 
    echo "lambda package saved to $LAMBDA_ZIP_ARCHIVE"
else
    echo "execute error."
    exit 1
fi

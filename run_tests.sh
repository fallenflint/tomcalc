#!/usr/bin/env bash

export PROJECT_IMAGE=flint/calculator_demo

export PROJECT_DIR=./

docker build ${PROJECT_DIR} -t ${PROJECT_IMAGE}


docker run --rm \
    -v $(pwd)/:/code/ \
    -w=/code \
    ${PROJECT_IMAGE} \

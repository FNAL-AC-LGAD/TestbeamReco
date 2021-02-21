#!/bin/bash

linkFrom=$1
name=$2
linkTo=$3

if [[ ! -d "${linkTo}/${name}" ]]; then
    ln -s ${linkFrom}/${name} ${linkTo}/${name}
fi

#!/bin/bash

link=$1

if [[ -d "${link}" ]]; then
    unlink ${link}
fi

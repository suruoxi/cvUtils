#!/bin/bash

if [ $# -lt 1];
then
  echo "Usage: $0 image"
  exit
fi

f=$1
echo "Image Format: "$(file ${f})
echo "Image Size: "$(identify -format "%wx%h" ${f})

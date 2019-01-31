#!/usr/bin/env bash

ARG=$1

# get the directory of the gapminder data
DIR="$PWD/../../data/gapminder/"

#create a temporary file to store the list of files
touch file

# populate the temp file with the list of files
ls $DIR | sort > file

i=1
if [[ $# -eq 0 ]]; then
  while read LINE; do
    echo "$i $(basename $LINE .cc.txt)"
    i=$(($i+1))
  done <file
else
  while read LINE; do
    if ${LINE:0:1} == "U"; then
      #echo "${LINE:0:1}" #"$i $(basename $LINE .cc.txt)"
      echo "$i $(basename $LINE .cc.txt)"
      i=$(($i+1))
    fi
  done <file
fi

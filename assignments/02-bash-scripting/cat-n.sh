#!/usr/bin/env bash

# set input arg to be $ARG
ARG=$1

# If no args given, explain usage
if [[ $# -ne 1 ]]; then
  printf "Usage: %s FILE\n" "$(basename "$0")"
  exit 1
fi

# if input arg isn't a file exit.
if [[ ! -f "$ARG" ]]; then
  echo "$ARG is not a file"
  exit 2
fi

#Iterate over lines in file, printing line number, and the line. 
i=0
while read -r LINE; do
  i=$((i+1))
  echo $i "$LINE"
done < "$ARG"

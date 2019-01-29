#!/usr/bin/env bash

ARG=$1
NUM=${2:-3}

# if no ARGS print Usage
if [[ $# -lt 1 ]]; then
  printf "Usage: %s FILE [NUM]\n" "$(basename "$0")"
  exit 1
fi

# if input arg isn't a file exit.
if [[ ! -f "$ARG" ]]; then
  echo "$ARG is not a file"
  exit 2
fi

# read the number of lines in NUM
i=0
while read -r LINE; do
  echo "$LINE"
  i=$((i+1))
  if [[ $i -eq NUM ]]; then
      break
  fi
done < "$ARG"

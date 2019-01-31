#!/usr/bin/env bash

GREETING=$1
NAME=${2:-Human}

# if no ARGS print Usage
if [[ $# -lt 1 ]]; then
  printf "Usage: %s GREETING [NAME]\n" "$(basename "$0")"
  exit 1
fi

# if > 2 ARGS print Usage
if [[ $# -gt 2 ]]; then
  printf "Usage: %s GREETING [NAME]\n" "$(basename "$0")"
  exit 1
fi


echo "$GREETING, $NAME!"

#!/bin/bash

if [ $# -ne 1 -o -z "$1" ]; then
  echo "Usage: $0 PROJECT_DIR"
  exit 1
fi

mpremote cp -r "$1" /sd/apps/
sleep 2
mpremote soft-reset

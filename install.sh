#!/bin/bash

if [ $# -ne 1 -o -z "$1" ]; then
  echo "Usage: $0 PROJECT_DIR"
  exit 1
fi

if [ ! -d "$1" ]; then
  echo "Usage: $0 PROJECT_DIR"
  exit 1
fi

# cp -r does not work :-/
# mpremote cp -r "$1" :/sd/apps/
mpremote mkdir :/sd/apps/"$1"
for f in "$1"/*; do
  mpremote cp "$f" :/sd/apps/"$1"/
done

sleep 2
# mpremote soft-reset

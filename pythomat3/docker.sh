#!/bin/sh
SOLUTION=$1
TARGET=$2
docker run -it -v $SOLUTION:/prod/solution -v $TARGET:/prod/target pythomat:3
firefox $TARGET/solution.html

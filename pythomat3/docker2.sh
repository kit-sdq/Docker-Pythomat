#!/bin/sh
PYTHOMAT=$1
SOLUTION=$2
TARGET=$3
docker run -it -v $SOLUTION:/prod/solution -v $TARGET:/prod/target pythomat:3
firefox $TARGET/solution.html

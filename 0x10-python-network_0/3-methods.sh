#!/bin/bash
# This script sends an OPTIONS request to a URL using curl and displays the allowed HTTP methods
curl -sI "$1" -X OPTIONS | awk '/Allow:/ {for (i=2; i<=NF; i++) printf $i" "; print ""}' | sed 's/ //' | tr -d '\n'

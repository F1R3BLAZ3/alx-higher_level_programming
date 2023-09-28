#!/bin/bash
# This script sends an OPTIONS request to a URL using curl and displays the allowed HTTP methods
curl -sI "$1" -X OPTIONS | grep "Allow:" | cut -d':' -f2 | sed 's/ //'

#!/bin/bash
# This script sends a GET request to a URL using curl, checks the response status code, and displays the response body for a 200 status code
curl -sL "$1" -X GET -D /dev/stdout -o /dev/stdout | (grep -q "200 OK" && cat /dev/stdin)

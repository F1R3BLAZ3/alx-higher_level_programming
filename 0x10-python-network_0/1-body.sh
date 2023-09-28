#!/bin/bash
# This script sends a GET request to a URL using curl and displays the body of a 200 status code response
curl -s -o /dev/stdout -w "%{http_code}" "$1" | (grep -q 200 && cat /dev/stdin)

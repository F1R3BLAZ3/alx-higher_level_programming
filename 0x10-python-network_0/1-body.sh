#!/bin/bash
# This script sends a GET request to a URL using curl and displays the response body for a 200 status code
curl -s -o /dev/stdout -w "%{http_code}" "$1" | (grep -q 200 && cat /dev/stdin)

#!/bin/bash
# This script sends a request to a URL using curl and displays the response body size in bytes
curl -sI "$1" | grep -iE 'Content-Length:' | awk '{print $2}' | tr -d '\r'

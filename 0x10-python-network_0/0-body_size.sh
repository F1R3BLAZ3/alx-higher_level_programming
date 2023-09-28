#!/bin/bash
# This script sends a request to a URL using curl and displays the response body size in bytes

url="$1"  # Get the URL from the command-line argument
response=$(curl -sI "$url")  # Send a HEAD request to get response headers
content_length=$(echo "$response" | grep -iE 'Content-Length:' | awk '{print $2}' | tr -d '\r')  # Extract Content-Length from headers
echo "Response Body Size: $content_length bytes"

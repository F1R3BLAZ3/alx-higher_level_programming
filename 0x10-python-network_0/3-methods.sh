#!/bin/bash
# This script sends an OPTIONS request to a URL using curl and displays the allowed HTTP methods
curl -s -i -X OPTIONS "$1" | grep -i Allow | cut -d ":" -f 2- | tr -d '[:space:]'

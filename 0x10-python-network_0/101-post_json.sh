#!/bin/bash
# getting the content of a respone with curl
curl -X POST -H "Content-Type: application/json" -d "$(cat $2)" $1

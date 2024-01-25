#!/bin/bash
# A script that sends a delete request to the URL passsed
curl -s -o -w "I'm a DELETE request" -X DELETE "$1"

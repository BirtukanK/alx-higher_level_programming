#!/bin/bash
# A script that takes a URL  and sends a request to that URL
curl -sI $1 | grep "Content-Length" | cut -d " " -f2

#!/bin/bash
# Takes URL and display HTTP methods
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-

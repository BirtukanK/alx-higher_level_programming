#!/bin/bash
# this script sends a GET request
curl -sX GET $1 -H "X-School-User-Id: 98" -L

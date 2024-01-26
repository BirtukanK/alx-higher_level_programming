#!/usr/bin/python3
""" Takes URL, send request and display value of id"""
import requests
import sys

url = sys.argv[1]
r = requests.get(url)
print(r.headers["X-Request-Id"])

#!/usr/bin/python3
""" takes URL and display the value of X-Request-Id"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.getheader("X-Request-Id")
        print(html)

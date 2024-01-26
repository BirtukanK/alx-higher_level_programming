#!/usr/bin/python3
""" takes URL and email, send POST requesr and display the body of response """
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    r = requests.post(url, data=value)
    print(r.text)

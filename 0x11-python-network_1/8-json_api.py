#!/usr/bin/python3
""" takes a letter and sends POST request"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(sys.argv) == 1:
        payload = {"q": q}
    else:
        payload = {"q": sys.argv[1]}
    r = requests.post(url, data=payload)
    try:
        r_json = r.json()
        if r_json:
            print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

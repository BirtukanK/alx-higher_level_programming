#!/usr/bin/python3
""" takes URL and email, send POST requesr and display the body of response """
import sys
import urllib.request
import urllib.parse

url = sys.argv[1]
value = {'email': sys.argv[2]}
data = urllib.parse.urlencode(value).encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   html = response.read()
   print(html.decode('utf-8'))

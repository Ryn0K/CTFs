#!/usr/bin/env python3
from requests import get
import sys
from bs4 import BeautifulSoup as bs
i=1
while True:
  try:
    r = get(f'http://challs.dvc.tf:51080/?MyTop5={i}&playlistTop={sys.argv[1]}')
    if(r.status_code == 200):
      soup = bs(r.text,'lxml')
      iframe=soup.findAll('iframe')[0]
      print(iframe['src'].replace('http://www.youtube.com/embed/',''))
    i+=1
  except KeyboardInterrupt:
    break

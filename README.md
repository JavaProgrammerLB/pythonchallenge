# pythonchallenge
Solve Problems in http://www.pythonchallenge.com

#### 18
- the obvious different between two picture is brightness.

```shell
gunzip deltas.gz
```

#### 17
result: http://www.pythonchallenge.com/pc/return/balloons.html

this is funny.

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

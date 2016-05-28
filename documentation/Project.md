# Project

```sh
root@edison:~# cd
root@edison:~# cd myproject
```

## 0x01

```sh
root@edison:~/myproject# nano main.py 
```

```python
#!/usr/bin/python

from core.xcamera import takePhoto
from core.xfacerecognition import recognizeFaces

takePhoto()
recognizeFaces()
```

## 0x02


```sh
root@edison:~/myproject# nano main.py 
```

```python
#!/usr/bin/python

from core.xcamera import takePhoto
from core.xfacerecognition import recognizeFaces
from core.xtalk import xtalk
from core.xwolfram import askWolfram

takePhoto()
faces = recognizeFaces()

question="What is the capital of Mexico"
answer = askWolfram(question)
xtalk("en-us", question)
xtalk("en-us", answer)
```
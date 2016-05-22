# Project

```sh
root@edison:~/myproject# nano main.py 
```

```python
from core.xcamera import takePhoto
from core.xfacerecognition import recognizeFaces

takePhoto()
recognizeFaces()
```
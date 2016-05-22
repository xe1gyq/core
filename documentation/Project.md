# Project

```sh
root@edison:~# cd
root@edison:~# cd myproject
root@edison:~/myproject# nano main.py 
```

```python
from core.xcamera import takePhoto
from core.xfacerecognition import recognizeFaces

takePhoto()
recognizeFaces()
```
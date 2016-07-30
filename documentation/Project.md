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
from core.xtalk import xtalk
from core.xwolfram import askWolfram

question="What is the capital of Mexico"
answer = askWolfram(question)
say("english", question)
say("english", answer)
```

## 0x03

```python
#!/usr/bin/python

from core.xspeechrecognition import recognizeSpeech
from core.xtalk import xtalk
from core.xvoice import recordAudio
from core.xvoice import playAudio

recordAudio()                                                                   
playAudio()                                                                     
print recognizeSpeech()
xtalk("en-us", text)
```

## 0x04

```python
#!/usr/bin/python

from core.xspeechrecognition import recognizeSpeech
from core.xsay import say
from core.xvoice import recordAudio
from core.xvoice import playAudio
from core.xwolfram import askWolfram

recordAudio()
playAudio()
question = recognizeSpeech()                                                    
say(question)                                                        
answer = askWolfram(question)                                                   
say(answer) 
```
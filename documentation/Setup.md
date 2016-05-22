# Setup

```sh
root@edison:~# cd
root@edison:~# mkdir myproject
root@edison:~# cd myproject/
root@edison:~/myproject# git clone https://github.com/xe1gyq/core.git
Cloning into 'core'...
remote: Counting objects: 1109, done.
remote: Compressing objects: 100% (171/171), done.
remote: Total 1109 (delta 93), reused 0 (delta 0), pack-reused 924
Receiving objects: 100% (1109/1109), 217.79 KiB | 0 bytes/s, done.
Resolving deltas: 100% (605/605), done.
Checking connectivity... done.
root@edison:~/myproject# 
```

```sh
root@edison:~/myproject# sh core/dependencies.shc
...
Successfully installed paho-mqtt wolframalpha matplotlib twython six numpy python-dateutil pytz cyclerb
Cleaning up...
root@edison:~/myproject# 
```


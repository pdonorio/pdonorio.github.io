
Who am I?

```ipython
$ipython
Python 3.6.1 (default, Apr  4 2017, 09:40:21)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: ! wget http://j.mp/pdonorio-python -O whoami.py
--2017-07-25 22:58:28--  http://j.mp/pdonorio-python
Resolving j.mp... 67.199.248.17, 67.199.248.16
Connecting to j.mp|67.199.248.17|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://raw.githubusercontent.com/pdonorio/pdonorio.github.io/master/scripts/whoami.py [following]
--2017-07-25 22:58:28--  https://raw.githubusercontent.com/pdonorio/pdonorio.github.io/master/scripts/whoami.py
Resolving raw.githubusercontent.com... 151.101.36.133
Connecting to raw.githubusercontent.com|151.101.36.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1427 (1.4K) [text/plain]
Saving to: ‘whoami.py’

whoami.py                       100%[======================================================>]   1.39K  --.-KB/s    in 0s

2017-07-25 22:58:29 (52.3 MB/s) - ‘whoami.py’ saved [1427/1427]


In [2]: %load_ext whoami

In [3]: %helloworld
Hello World!
    Who am i?

email: p.donoriodemeo@cineca.it
twitter: @paolo.donorio
github: @pdonorio
Out[3]: 42

In [4]:
```
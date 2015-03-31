# Installation #

No compilation or binary packages are needed, just download source code and execute it!

Currently, no external dependencies are required, but httplib2 (and eventually socksipy) could be used (instead of urllib2) if you need more performance or advanced HTTP features (proxies, ssl).

Of course, you need Python installed (at least version 2.4, untested with earlier versions).

## Download ##

Get a local copy of current development version (repository):
```
hg clone https://pysimplesoap.googlecode.com/hg/ pysimplesoap
```

Or get a more stable source archive (zip):

http://code.google.com/p/pysimplesoap/downloads/list

Or install from PyPI:

```
pip install pysimplesoap
```



## Prerequisites ##

Optionally, httplib2 is needed for the SoapClient (SoapServer doesn't need any dependencies) in order to get a better performance or advanced features:

In GNU/Linux (Debian), install its package:
```
apt-get install python-httplib2
```
In Windows, download [httplib2-0.4.0.zip](http://httplib2.googlecode.com/files/httplib2-0.4.0.zip), uncompress and run:
```
c:\python25\python.exe setup.py install
```

Additionaly, for proxy support, download [socksipy](http://sourceforge.net/projects/socksipy) and copy it to main folder and/or under the python path.

For a full stack solution using SoapDispatcher see Web2Py (you'll need http://www.web2py.com)
# SOAP Server #

SoapDispatcher is intended to be used from web frameworks (see Web2Py) to expose webservice functionalities.

Although, a minimal HTTP server is included to test basic features or show how to embed  it other applications if no web framework is available.

For testing, SOAPHandler (a minimal BaseHTTPRequestHandler implementation) can be used.
Following is some sample code.

**WARNING**: current release (**experimental**) of this server is in beta status, not intended to be used in production (exposed to Internet) by now . There are known [XML vulnerabilities](https://docs.python.org/2/library/xml.html#xml-vulnerabilities) of the Python's standard library implementation. If you need to parse untrusted or unauthenticated data, sanitize it with [defused xml](https://pypi.python.org/pypi/defusedxml/) package (PyPI).

## Example ##

This example expose an adder function that receive two integers and returns his sum.

Basic instrospection information about the webservice can be seen using a browser:
  * WSDL: http://localhost:8008/
  * Sample Request XML message: http://localhost:8008/Adder?request
  * Sample Response XML message: http://localhost:8008/Adder?response

For a nicer webpage with complete method help and esy interface, see Web2Py implementation.

### Server ###

Python's built-in HTTPServer can be used with SOAPHandler to expose a minimal SOAP Server:

```
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer

def adder(a,b):
    "Add two values"
    return a+b

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)

# register the user function
dispatcher.register_function('Adder', adder,
    returns={'AddResult': int}, 
    args={'a': int,'b': int})

print "Starting server..."
httpd = HTTPServer(("", 8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()
```

#### SoapDispatcher attributes ####

You can alter the location, action and namespace attributes of SoapDispatcher if you need to bind to several addresses or make a invariant namespace URI.

See [issue #79](https://code.google.com/p/pysimplesoap/issues/detail?id=#79) for more info and a tentative solution (thanks user ismaelgfk for the contribution).

Implementation in frameworks like web2py update this attributes automatically.

### Client ###
To test this minimal server, a minimal client can be used:

```
from pysimplesoap.client import SoapClient, SoapFault

# create a simple consumer
client = SoapClient(
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl", 
    soap_ns='soap',
    trace = True,
    ns = False)

# call the remote method
response = client.Adder(a=1, b=2)

# extract and convert the returned value
result = response.AddResult
print int(result)
```

The expected output should be:
```
--------------------------------------------------------------------------------
POST http://localhost:8008/
SOAPAction: "http://localhost:8008/Adder"
Content-length: 329
Content-type: text/xml; charset="UTF-8"

<?xml version="1.0" encoding="UTF-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soap:Body>
    <Adder xmlns="http://example.com/sample.wsdl">
    <a>1</a><b>2</b></Adder>
</soap:Body>
</soap:Envelope>

date: Tue, 20 Jul 2010 23:39:21 GMT
status: 200
content-type: text/xml
server: BaseHTTP/0.3 Python/2.5.4
<?xml version="1.0" encoding="UTF-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body><AdderResponse xmlns="http://example.com/sample.wsdl"><AddResult>3</AddResult></AdderResponse></soap:Body>
</soap:Envelope>
================================================================================
3
```
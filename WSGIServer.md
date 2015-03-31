# WSGI Server #

WSGI is a specification for web servers and application servers to communicate with web applications (though it can also be used for more than that)

Using WSGI it is possible to host your services in many servers like Apache, IIS (through NWSGI), use FASTCGI or use pythons servers like twisted.

SoapDispatcher is intended to be used from web frameworks (see Web2Py) to expose webservice functionalities.

**WARNING**: current release (**experimental**) of WSGI support is in beta status and does not have many tests for now.

## Example ##

This example expose an adder function that receive two integers and returns his sum.

Basic instrospection information about the webservice can be seen using a browser:
  * WSDL: http://localhost:8008/
  * Sample Request XML message: http://localhost:8008/Adder?request
  * Sample Response XML message: http://localhost:8008/Adder?response

### Server ###

Python's built-in WSGI server can be used with WSGISOAPHandler to expose a minimal SOAP Server:

```
from pysimplesoap.server import SoapDispatcher, WSGISOAPHandler

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

application = WSGISOAPHandler(dispatcher)

if __name__=="__main__":
    print "Starting server..."
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8008, application)
    httpd.serve_forever()
```

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
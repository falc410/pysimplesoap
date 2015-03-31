# Support of WSDL #

This library supports (but do not requires) WSDL parsing/generation.

Either SoapClient or SoapServer can be done totally dynamic without WSDL at all, using SimpleXMLElement (see raw example below).

For introspection, third party tools and ease of use, this library provides both WSDL parsing (at client side), and WSDL generation (at server side):

## Client Support of WSDL ##

SoapClient supports WSDL parsing and instrospection. It's automatically called when the client is created using `wsdl` parameter at the constructor, or calling `client.wsdl(url)`

It can be used to extract webservice properties (namespace, action, and input/output type declarations), to speed-up SOAP calls.

For example, to list operations (methods) available use:
```
from pysimplesoap.client import SoapClient
client = SoapClient(wsdl="http://127.0.0.1:8000/webservices/sample/call/soap?WSDL",trace=False)
print "Target Namespace", client.namespace
for service in client.services.values():
    for port in service['ports'].values():
        print port['location']
        for op in port['operations'].values():
            print 'Name:', op['name']
            print 'Docs:', op['documentation'].strip()
            print 'SOAPAction:', op['action']
            print 'Input', op['input'] # args type declaration
            print 'Output', op['output'] # returns type declaration
            print
```

Should ouptut:
```
Target Namespace: http://127.0.0.1:8000/webservices/sample/call/soap

Name: Dummy
Docs: Just does nothing
SOAPAction: http://127.0.0.1:8000/webservices/sample/call/soap
Input {'Dummy': None}
Output {'DummyResponse': None}

Name: AddIntegers
Docs: Add two values
SOAPAction: http://127.0.0.1:8000/webservices/sample/call/soap
Input {'AddIntegers': {u'a': <type 'int'>, u'b': <type 'int'>}}
Output {'AddIntegersResponse': {u'AddResult': <type 'int'>}}

Name: SubIntegers
Docs: Substract two values
SOAPAction: http://127.0.0.1:8000/webservices/sample/call/soap
Input {'SubIntegers': {u'a': <type 'int'>, u'b': <type 'int'>}}
Output {'SubIntegersResponse': {u'SubResult': <type 'int'>}}

Name: Echo
Docs: Copy request->response (generic, any type)
SOAPAction: http://127.0.0.1:8000/webservices/sample/call/soap
Input {'Echo': {u'value': None}}
Output {'EchoResponse': {u'value': None}}

Name: AddStrings
Docs: Add two values
SOAPAction: http://127.0.0.1:8000/webservices/sample/call/soap
Input {'AddStrings': {u'a': <type 'unicode'>, u'b': <type 'unicode'>}}
Output {'AddStringsResponse': {u'AddResult': <type 'unicode'>}}

```

For a full printout, use pretty print:
```
import pprint
pprint.pprint(client.services)
```

## Server WSDL support ##

SoapDispatcher can generate WSDL on the fly.
See above example, or look at Web2Py.

## Raw Example ##

When no type declaration is given, any values can be passed.
Both at client and server, request and response messages are parser using SimpleXMLElement, allowing managing XML messages with no limitations (this includes: using custom/complex types, unsupported features, etc).

For example, a echo Server:
```
@service.soap('Echo')
def echo(request):
    "Copy request->response (generic, any type)"
    return request.value
```

And the echo Client:
```
from pysimplesoap.client import SoapClient, SimpleXMLElement
from client import SoapClient
from simplexml import SimpleXMLElement
client = SoapClient(
    location = "http://127.0.0.1:8000/webservices/sample/call/soap",
    action = 'http://127.0.0.1:8000/webservices/sample/call/soap', # SOAPAction
    namespace = "http://127.0.0.1:8000/webservices/sample/call/soap", 
    soap_ns='soap', trace = True, ns = False)
params = SimpleXMLElement("""<?xml version="1.0" encoding="UTF-8"?>
<Echo><value>Hello world</value></Echo>""") 
response = client.call('Echo',params)
result = response.value 
print str(result) # manually convert returned type
```
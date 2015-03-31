# Soap Client #

## Introduction ##

A simple, minimal and functional HTTP SOAP webservice consumer, using httplib2 for the connection ad SimpleXmlElement for the XML request/response manipulation.

It allows to control the requests and to make the xml in a compatible way (ie. using several dialects and protocol versions, like .NET and Java Axis ones)

No WSDL parsing is required, it only needs Location, SOAPAction and namespaces to use.
But also, a WSDL parser is available to extracts this properties from service description files, and doing introspection (listing operation, messages, services/ports, etc.), see WsdlSupport.

By using SimpleXmlELement, it can do simple serialization converting passed values to strings, and des-serialization can be done automatically (using WSDL declared types), or manually (specifying convertions from xml to python types).

## Usage ##

  1. Create a SoapClient object: `client = SoapClient(location, action, namespace, ns, trace)`
    * wsdl: URL of the webservice description file
    * location: URL of the webservice
    * action: SOAPAction
    * namespace: custom namespace used by the webservice
    * ns: xml tags namespace prefix (False to disable)
    * soap\_ns: soap namespace prefix (dialect):
      * soap11="http://schemas.xmlsoap.org/soap/envelope/",
      * soap="http://schemas.xmlsoap.org/soap/envelope/",
      * soapenv="http://schemas.xmlsoap.org/soap/envelope/",
      * soap12="http://www.w3.org/2003/05/soap-env",
    * soap\_server="axis" _see source code for more information_
    * trace: print request and response (debugging)
    * proxy: dict containing user,pass,server,port for proxy (optional)
    * exceptions: enable raise of (SoapFault)
  1. Set up any header using python dict-like syntax: `client['header_name'] = 'header_value'`. For WS-Security, use `'wsse:Security'` header (see bellow). Also below are more ways of setting headers.
  1. Call webservice methods. Ie., `client.loginCms(in0=cms)` calls `loginCms` with parameter `in0`
  1. Analyze the result object (see SimpleXmlElement) or dictionary (using WSDL)
  * Attributes `client.xml_request` and `client.xml_response` holds sent ad received XML messages

## Examples ##

### Basic example using WSDL ###
```
from pysimplesoap.client import SoapClient
client = SoapClient(wsdl="http://127.0.0.1:8000/webservices/sample/call/soap?WSDL",trace=False)
response = client.AddIntegers(a=1,b=2)
result = response['AddResult']
print result
```

See [client\_tests.py](http://code.google.com/p/pysimplesoap/source/browse/tests/client_tests.py) for more examples.

### Basic example not using WSDL ###
Same example not using WSDL (manual deserialization of return values):
```
from pysimplesoap.client import SoapClient
client = SoapClient(
    location = "http://127.0.0.1:8000/webservices/sample/call/soap",
    action = 'http://127.0.0.1:8000/webservices/sample/call/soap', # SOAPAction
    namespace = "http://127.0.0.1:8000/webservices/sample/call/soap", 
    soap_ns='soap', trace = False, ns = False, exceptions=True)
response = client.AddIntegers(a=1,b=2)
result = response.AddResult # manually convert returned type
print int(result)
```

See [client\_tests.py](http://code.google.com/p/pysimplesoap/source/browse/tests/client_tests.py) for more examples.

### WSDL SOAP Headers Example ###

Setup `AuthHeaderElement` authentication header with username and password (requires a valid WSDL!):
```
client = SoapClient(wsdl=WSDL, ns="web", trace=True)
client['AuthHeaderElement'] = {'username': 'mariano', 'password': 'clave'}
result = client.PersonaSearch(numero_documento='99999999')
```

See [licencias\_tests.py](http://code.google.com/p/pysimplesoap/source/browse/tests/licencias_tests.py) for more examples.

### WSDL SOAP WSSE Example ###

Setup WebService Security (WSSE) credentials header with username and password:
```
client = SoapClient(wsdl = WSDL, cache = None, ns="tzmed", soap_ns="soapenv", soap_server="jbossas6", trace=True)
                       
# Set WSSE security credentials
self.client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'testwservice',
                'wsse:Password': 'testwservicepsw',
                }
            }}}}
```

See [trazamed\_test.py](http://code.google.com/p/pysimplesoap/source/browse/tests/trazamed_tests.py) for more examples.

### Raw/arbitrary SOAP Header Example ###

You can send custom headers with the data you want, regardless of WSDL specification, creating an SimpleXMLElement object and passing it in the header parameter to the remote call:
```
client = SoapClient(location="https://localhost:666/",
                    namespace='http://localhost/api', trace=True)

headers = SimpleXMLElement("<Headers/>")
my_test_header = headers.add_child("MyTestHeader")
my_test_header['xmlns'] = "service"
my_test_header.marshall('username', 'test')
my_test_header.marshall('password', 'password')
client.methodname(headers=headers)
```

This will generate the following xml:
```
<soap:Header><MyTestHeader xmlns="service"><username>test</username><password>password</password></MyTestHeader></soap:Header>
```

This is equivalent to the following code (if you were using a WSDL, see previos sections):
```
client['MyTestHeader'] = {'username': 'test', 'password': 'test'}
```

See [issues\_test.py](http://code.google.com/p/pysimplesoap/source/browse/tests/issues_tests.py) for more examples.

### SimpleXMLElement headers and wsdl ###
From 1.07b on you can use SimpleXMLElement headers with WSDL.

When the WSDL requires a certain namespace being used in the header, or  the server requires a namespaced tag inside the header - this is a way to fix it.
```
client = SoapClient(wsdl='http://someserver/some.asmx?wsdl')
namespace = 'http://unfriendly.products/hardwsdl'
ns='ufp'
header = SimpleXMLElement('<Headers/>', namespace=namespace, prefix=ns)
security = header.add_child("Security")
security['xmlns:'+ns]=namespace
security.marshall('ClientID','NAME',ns=ns)
security.marshall('Checksum','PASSWORD',ns=ns)
client['Security']=security
```
The header sent will now be:
```
<soap:Header><ufp:Security xmlns:ufp="http://unfriendly.products/hardwsdl"><ufp:ClientID>NAME</ufp:ClientID><ufp:Checksum>PASSWORD</ufp:Checksum></ufp:Security></soap:Header>
```

This header is inserted with every method call. So there is no need for the special `headers=` parameter to a function. Just use:
```
client.someMethod()
```

### Fixing broken WSDL ###

To fix a broken wsdl, you can do it directly using `services` attribute of `SoapClient`.

For example, if the `location` address doesn't work (uses _http_ instead of _https_, _localhost_ instead of a valid _IP_, etc), you can change it after creating the client:

```
# fix location (localhost:9050 is erroneous in the WSDL)
client.services['IWebServiceService']['ports']['IWebServicePort']['location'] = "https://186.153.145.2:9050/trazamed.WebService"
```

Also, you can fix element names so they can be marshalled, unmarshalled correctly, as in this example:
```
# fix bad wsdl: server returns "getValidLanguagesResponse" instead of "getValidLanguages12Response"
output = client.services['MetDataService']['ports']['MetDataServicePort']['operations']['getValidLanguages']['output']['getValidLanguages12Response']
client.services['MetDataService']['ports']['MetDataServicePort']['operations']['getValidLanguages']['output'] = {'getValidLanguagesResponse': output}
```

See [trazamed\_test.py](http://code.google.com/p/pysimplesoap/source/browse/tests/trazamed_tests.py) and http://code.google.com/p/pysimplesoap/source/browse/tests/issues_tests.py for more examples.

### Raw example ###
Same example but without type conversion -RAW full control- (manual serialization of parameters and desserialization of return values)):
```
from pysimplesoap.simplexml import SimpleXMLElement
client = SoapClient(
    location = "http://127.0.0.1:8000/webservices/sample/call/soap",
    action = 'http://127.0.0.1:8000/webservices/sample/call/soap', # SOAPAction
    namespace = "http://127.0.0.1:8000/webservices/sample/call/soap", 
    soap_ns='soap', trace = True, ns = False)
params = SimpleXMLElement("""<?xml version="1.0" encoding="UTF-8"?>
<AddIntegers><a>3</a><b>2</b></AddIntegers>""") # manually make request msg
response = client.call('AddIntegers',params)
result = response.AddResult 
print int(result) # manully convert returned type
```

**Note**: There is not hidden code required to use this client (nor autogenerated boilerplate code nor xml WSDL nor type declaration nor third-party tools).

The request/response output (if trace=True) will be something like:
```
POST http://127.0.0.1:8000/webservices/sample/call/soap
SOAPAction: "http://127.0.0.1:8000/webservices/sample/call/soapAddIntegers"
Content-length: 362
Content-type: text/xml; charset="UTF-8"

<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soap:Body>
    <AddIntegers xmlns="http://127.0.0.1:8000/webservices/sample/call/soap">
    <a>3</a><b>2</b></AddIntegers>
</soap:Body>
</soap:Envelope>

status: 200
content-length: 314
set-cookie: session_id_webservices=127-0-0-1-5ef40faf-c29e-4078-81b0-c344b12df03b; Path=/
expires: Tue, 27 Jul 2010 05:28:54 GMT
server: Rocket 1.0.6 Python/2.5.4
connection: keep-alive
pragma: no-cache
cache-control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
date: Tue, 27 Jul 2010 05:28:54 GMT
content-type: text/xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><soap:Body><AddIntegersResponse><AddResult>5</AddResult></AddIntegersResponse></soap:Body></soap:Envelope>
================================================================================
5
```
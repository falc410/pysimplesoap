# web2py and SOAP Webservices #

Web2py already supports a common infrastructure to expose webservices in a simple way, using the Service tool (rss, json, jsonrpc, xmlrpc, jsonrpc, amfrpc, amfrpc3)

This library aims to add SOAP support extending the current filosophy.



## web2py SOAP Server Example ##

Serving operations using SOAP is as easy as decorating a function using `@service.soap` declaring:
  * Exposed operation method (camel case by convention)
  * Return types
  * Parameters types

Types are declared using a dictionary, mapping the parameter/result name with the standard python conversion functions (`str`,`int`,`float`,`bool`, etc.).

For more information see SimpleXmlElement, SoapDispatcher and SoapServer.

**Note**: pysimplesoap is included with web2py since version #1.82.1

**WARNING**: as of 2010-08-06, SOAP server support is in alpha status.

### web2py SOAP controller ###

Create a application (like 'webservices'), and in a controller ('sample.py') add the following code:
```
from gluon.tools import Service
service = Service(globals())

@service.xmlrpc
@service.soap('AddStrings',returns={'AddResult':str},args={'a':str, 'b':str})
@service.soap('AddIntegers',returns={'AddResult':int},args={'a':int, 'b':int})
def add(a,b): 
    "Add two values"
    return a+b

@service.xmlrpc
@service.soap('SubIntegers',returns={'SubResult':int},args={'a':int, 'b':int})
def sub(a,b): 
    "Substract two values"
    return a-b

def call():
    return service()
```

### Testing web2py SOAP introspection user interface ###

Additionally, web2py can dynamically generate help webpages (list of operations, xml message examples) and the WSDL xml:

  * List of operations: http://127.0.0.1:8000/webservices/sample/call/soap
  * Operation help (ie. for SubIntegers): http://127.0.0.1:8000/webservices/sample/call/soap?op=SubIntegers
  * Service Description (WSDL): http://127.0.0.1:8000/webservices/sample/call/soap?wsdl

#### Sample operations list page ####

Welcome to Web2Py SOAP webservice gateway

The following operations are available

See WSDL for webservice description

  * AddIntegers: Add two values
  * SubIntegers: Substract two values
  * AddStrings: Add two values

_Notes:_ WSDL is linked to URL retriving the full xml.
Each operation is linked to its help page.

#### Sample operation help page ####

**AddIntegers**

Add two values

  * Location: http://127.0.0.1:8000//webservices/sample/call/soap
  * Namespace: http://127.0.0.1:8000/webservices/sample/soap
  * SoapAction: -N/A by now-

Sample SOAP XML Request Message:
```
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	<soap:Body>
		<AddIntegers xmlns="http://127.0.0.1:8000/webservices/sample/soap">
			<a>
				<!--integer-->
			</a>
			<b>
				<!--integer-->
			</b>
		</AddIntegers>
	</soap:Body>
</soap:Envelope>
```
Sample SOAP XML Response Message:
```
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	<soap:Body>
		<AddIntegersResponse xmlns="http://127.0.0.1:8000/webservices/sample/soap">
			<AddResult>
				<!--integer-->
			</AddResult>
		</AddIntegersResponse>
	</soap:Body>
</soap:Envelope>
```

## web2py SOAP Client example ##

You can test the webservice exposed by web2py using this library:

```

def test_soap_sub():
    from gluon.contrib.pysimplesoap.client import SoapClient, SoapFault
    # create a SOAP client
    client = SoapClient(wsdl="http://localhost:8000/webservices/sample/call/soap?WSDL")       
    # call SOAP method
    response = client.SubIntegers(a=3,b=2)
    try:
        result = response['SubResult']
    except SoapFault:
        result = None
    return dict(xml_request=client.xml_request, 
                xml_response=client.xml_response,
                result=result)
```

**Note:** pysimplesoap is included since recent releases of web2py. check version frequently.
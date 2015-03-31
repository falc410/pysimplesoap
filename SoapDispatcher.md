# SOAP Dispatcher #

SOAPDispatcher is a python class to serve SOAP webservices using this library.

Its goal is to expose python methods in a simple, flexible and compatible way, resembling python Simple XML RPC implementation.

SimpleXmlElement is used to convert from and to XML, so operations (methods) are normal Python functions, that can be shared with other webservices protocols (ie. XMLRPC).
Same function can be registered several times, according its arguments and return types.

No boilerplate code is required (neither special classes, artifacts or external tools), the types definition is a python structure mapping tag names with python covertion function, ie: `args={'p': {'a': int,'b': int}, 'c': [{'d':str}]} ` defines two parameters (p and c), the first with two integers and the second with a list of strings. In runtime, the function receives a similar structure, but with actual values, ie.: `kwargs={'p': {'a':1,'b':2}, 'c': [{'d': 'foo'}, {'d': 'bar'}]`}

No previuos WSDL is required (the python types definition is used insead), and the goal is to dinamically generate that service description for static languages and SOAP tools.
In fact, this type declaration is needed only to adapt existing normal python functions, if you could make a custom server method that reads an returns SimpleXmlElement objects dynamically, this will not be required (as in SoapClient).

The idea is to detect and respond in the correct SOAP dialect (looking at the SOAP headers, namespace and prefix, ie. for Java AXIS or .Net clients).

**WARNING**: the initial release (**experimental**) of this dispatcher is in alpha status, not intended to be used in production by now.

## Usage ##

This class is intended to be used from web frameworks (see Web2Py).
Look at SoapServer example to embed it in your applications if no web framework is available.

## Methods ##

SOAPDispatcher Constructor parameters:
  * namespace: custom tag xml namespace to be used (if any)
  * prefix: custom namespace prefix (if used)

Methods:
  * register\_function(method, function, returns, args): register the python fuction, its return and parameter types under the given method name
  * dispatch(xml): Receive and proccess SOAP call. Parses xml request message, calls the corresponding function, and generates the xml response message with the result.
  * list\_methods(): Return a list of registered operations and its documentation.
  * help(method=None): Generate sample xml request and response messages
  * wsdl(): Generates webservice definition

## Example ##

For testing, SOAPHandler (a minimal BaseHTTPRequestHandler implementation) can be used: see SoapServer, but for a more complete implementation see Web2Py (including user interface webpages)
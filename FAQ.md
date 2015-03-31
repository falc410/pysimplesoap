

Apologies in advance: Spanish is our main language, so there may be errors or inaccuracies with our written English.

## Motivation: Why another python SOAP webservice implementation? ##

First, a little of our history: when we started a project to consume AFIP (Argentina IRS) webservices related to electronic invoice (late 2008), we tested some python SOAP implementations:
  * SOAPPy: after initial successfully tests with some webservices, it failed in some enviroments (we have to deal with booth Java Axis and .NET). The effort was to big to fix the issues, mainly related to xml generation and namespaces.
  * ZSI: we even could get this library to compile, this was not encouraging as we were planning develop our application in many enviroments (we didn't dedicated too much time for this task either).
  * suds, soaplib, etc.: we didn't tried them, I don't remember the exact reasons, maybe they were relatively new (in general, we give up seeing the status/complexity of those implementations at that time for our case)

In front of this difficulties, specially seeing how hard was to implement/adapt/maintain a simple SOAP webservice client in Python, we decided start our own SOAP library, aimed to be very simple but functional.

As the official (AFIP) webservices examples, that we based on, were programmed in PHP, and as SOAP and Simple XML extensions for that language seemed very intuitive, we take that path, so our library resembles that extensions (including method names an general usage).

With this approach, we could manage to write a SOAP client in fewer lines, allowing us to customize and adapt it to talk to several servers.

As time elapsed, the library stabilized and got more features, so it may be useful to other people now.

Of course, the other libraries have evolved too, incorporating features we even don't expect to have ever (like abstract object serializers, WSDL stub generators, XML schema validation or fancy SOAP features and data types). Other features are not so advanced in this library (server/dispatcher is in alpha state currently, WSDL support functional but partially implemented, etc.)

Our intent is to keep this library as small as possible (ie. <200LOC client) for the sake of readability, maintenance and easy usage.

This approach has proven ability to support our use cases, allowing to extend it when exotic or unsupported features are required.

Look at the following answers for a wider snapshot of the state of this library.

Anyway, we encourage you to analize and/or test the other webservices libraries too.

## Features: How this library is compared to suds, soaplib, ZSI? ##

Following the guidelines published by [Doug Hellmann at Sept 2009 Python Magazine](http://www.doughellmann.com/articles/pythonmagazine/features/building-soap-service/index.html), here is an analysis of this library (compare it to ZSI and soaplib in the original article):

  * **Installing**: Very simple, no compilation required (see [Installation](Installation.md)). Just extract zip archive and run it!. Optionally, install a fewer pure-python dependencies (httplib2 for advanced encrypted connections, socks for proxy support). This contrast with other libraries that requires advanced extensions like lxml/pyxml (some hard to compile/install in some enviroments)
  * **Feature Completeness**: Integrated Full Stack SoapClient & SoapDispatcher solution (used on top of Web2Py or standalone/embedded, similar to XML RPC python library). This allow to expose the same methods (with the same unchanged source code) using diferent protocols, ie., with Web2Py built-in tools (currently rss, json, jsonrpc, xmlrpc, jsonrpc, amfrpc, amfrpc3). Additionally, Web2Py easily allows to expose html web pages as a user interface suitable for testing (with a list of operations available and the respective help / xml message samples). Eventually, this interface would be extended with simple html forms to provide online testing and debugging without requiring to write a single line of code.
  * **Interoperability**: this library was designed to work with different SOAP dialects (like Java AXIS, .NET 2.0, JBoss, etc., see TestingCompliance). This includes support for both SOAP specifications (1.1 and 1.2), several XML generators and parsers (ie. using or not using namespaces prefixes), etc. Also, this library is simple enough to be easily adaptable to new webservices environments/platforms.
  * **Elegance**: This library is very pythonic in the sense that doesn't not require WSDL (XML) service description at all (just pure dynamic python code, no need to use even automatic generated classes/artifacts or boilerplate code/xml, see SimpleXmlElement). This is a distinction from others libraries (citing the original article: "SOAP toolkits tend to fall in one of two camps: Those that generate source from a WSDL file and those that generate a WSDL document from source"). IMHO, we think this approach support most python features truly enabling flexible and rapid webservice development/prototiping/testing. Additionally, WSDL could be dynamically generated for third-party tools and languages or parsed to do introspection (see WsdlSupport), but that is not really required by this library. Also, as we manage almost all aspects of webservice communication, most times we can raise helpfull error messages, and in general, the library should be very intuitive to use.
  * **Freshness**: this is a brand-new library born to resolve recent webservices enviroments.
  * **Documentation**: IMHO, the code is very simple and self documented, and this wiki is provided as a collaborative documentation. Fell free to ask us if you need something else.
  * **Deployment complexity**: for testing, a basic HTTP server is provided (see SoapServer), for production, it can be used on top of Web2Py (taking advantage of an existing WSGI, Apache, HTTPS, etc. infrastructure) or embedded in a custom aplication/server.
  * **Packaging complexity**: redistribution should be very easy (as no complex/compiled C extension are used), we already packaged this library using py2exe, and even the source package can be used for distribution. Web2Py is in fact distributed packaged with py2exe too.
  * **Licencing**: This library is published under the LGPL licence, so it can be integrated into propietary software or open source projects. Web2Py can be used to serve non GPL applications.
  * **Testing**: we have simple tests in each source file, although further integration is planned. Unittest or equivalent infrastructure to tests servers or clients made with this library will not be developed (but using third party tools like SoapUI or web2py doctests would be supported).
  * **Performance**: we have no extensive tests about this. This will largely depend on the webservice being consumed or served, as xml.dom.minidom speed to parse XML messages may be irrelevant in most scenarios. As we do little overhead (no caching needed, no WSDL parsing mandatory, nor schema validation nor complicated data type conversion), performance shouldn't be a problem. See PerformanceBenchmarks for a comparative.

Of course, this is our perception, you should do your own analysis.

YMMV

## Status: Is this library suitable for production use? ##

This library has some code in early development stages.

Said that, SoapClient is working successfully and is commercially supported since late 2008 with many AFIP (Argentina IRS) webservices (electronic invoice, tax bonus, foreing trade, agriculture, customs, etc.), in several environments (Java AXIS, .NET 2.0, JBoss, etc.).

It was introduced at Argentina Conferences and Courses: a lighting talk at PyCon Argentina 2009, a lecture at Conurbania 2009 and specific tutorials in 2009/2010.

For further information see:
  * http://www.pyafipws.com.ar/
  * http://code.google.com/p/pyafipws/
  * http://groups.google.com/group/pyafipws

In contrast, SoapDispatcher, SoapServer, Web2Py and WSDL support were recently released, so they must be considered in beta state.

## Where to get help? ##

  * For discussions, announces and general topics use soap@python.org mailing list
  * See issues to report bugs, feature requests or tasks (free)
  * Contact project owners for advanced commercial support (paid)
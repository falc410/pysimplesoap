<a href='https://github.com/pysimplesoap/pysimplesoap'><img src='https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png' alt='Fork me on GitHub' border='0' align='right' /></a>

# PySimpleSOAP / soap2py #

Python simple and lightweigh SOAP library for client and server webservices interfaces, aimed to be as small and easy as possible, supporting most common functionality.
Initially it was inspired by [PHP Soap Extension](http://php.net/manual/en/book.soap.php) (mimicking it functionality, simplicity and ease of use), with many advanced features added.

**Supports Python 3** (same codebase, no need to run 2to3)

## Goals ##
  * Simple: less than 200LOC client/server concrete implementation for easy maintainability and enhancments.
  * Flexible: adapted to several SOAP dialects/servers (Java Axis, .Net, WCF, JBoss, "jetty"), with the posibility of fine-tuning XML request and responses
  * Pythonic: no artifacts, no class generation, no special types, RPC calls parameters and return values are simple python structures (dicts, list, etc.)
  * Dynamic: no definition (WSDL) required, dynamic generation and parsing supported (cached in a pickle file for performance, supporting fixing broken WSDL)
  * Easy: simple xml manipulation, including basic serialization and raw object-like access to SOAP messages
  * Extensible: supports several HTTP wrappers (httplib2, pycurl, urllib2) for special transport needs over SSL and proxy (ISA)
  * WSGI compilant: server dispatcher can be integrated to other python frameworks (web2py, django, etc.)
  * Backwards compatible: stable API, no breaking changes between releases
  * Lightweight: low memory footprint and fast processing (an order of magnitude in some situations, relative to other implementations)

## History ##

Client initially developed for AFIP (Argentina's IRS) web services: electronic invoice, tax bonus, insurance, foreing trade, agriculture, customs, etc. (http://code.google.com/p/pyafipws/wiki/ProjectSummary)

Now it has been extended to support other webservices like Currency Exchange Control and TrazaMed (National Traceability of Medical Drugs Program)

Also, includes Server side support (a generic dispatcher, in order to be exposed from web2py service framework, adaptable to other webservers)

Source Code also available on [GitHub](https://github.com/pysimplesoap/pysimplesoap)

## Support ##

For community support, please fell free to fill an [issue](https://code.google.com/p/pysimplesoap/issues/list) or send a email to [soap@python.org](https://mail.python.org/mailman/listinfo/soap).
Please do not add comment to wiki pages if you have technical questions.

For priority technical support, you can contact [Mariano Reingart](mailto:reingart@gmail.com) (project creator and main maintainter, see [AUTHORS](https://code.google.com/p/pysimplesoap/source/browse/AUTHORS.md) for more info).
Online payments accepted through PayPal.

### Pre-paid priority tech support plans ###

  * <a href='https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=QAQUG78GQ89WL&on0=Coverage+plan&os0=per+email%3A+1+day%2C+up+to+15+min&currency_code=USD&submit.x=89&submit.y=8'>per email: 1 day coverage, up to 15 min $10,00 USD</a>
  * <a href='https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=QAQUG78GQ89WL&on0=Coverage+plan&os0=per+incident%3A+1+week%2C++up+to+2+hs&currency_code=USD&submit.x=112&submit.y=15'>per incident: 1 week coverage, up to 2 hs $50,00 USD</a>
  * <a href='https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=QAQUG78GQ89WL&on0=Coverage+plan&os0=per+feature%3A+1+month%2C+up+to+6+hs&currency_code=USD&submit.x=64&submit.y=18'>per feature: 1 month coverage, up to 6 hs $150,00 USD</a>
  * <a href='https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=QAQUG78GQ89WL&on0=Coverage+plan&os0=per+project%3A+3+month%2C+up+to+15+hs&currency_code=USD&submit.x=87&submit.y=14'>per project: 3 month coverage, up to 15 hs $350,00 USD</a>
  * <a href='https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=QAQUG78GQ89WL&on0=Coverage+plan&os0=extended%3A+9+month%2C+up+to+30hs&currency_code=USD&submit.x=90&submit.y=9'>extended: 9 month coverage, up to 30hs $750,00 USD</a>

<a href='https://www.paypal.com/ar/cgi-bin/webscr?cmd=xpt/Marketing/general/WIPaypal-outside'><img src='https://www.paypal.com/es_XC/Marketing/i/logo/bnr_international_buyer3_347x41.gif' alt='Vendedor internacional' border='0' /></a>
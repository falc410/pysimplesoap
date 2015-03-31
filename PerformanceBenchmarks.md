# WSDL Parser Benchmarks #

As WSDL is a complex XML document, parsing it can be useful to estimate overall performance.

Test conditions:
  * real webservices (some actually quite complex)
  * WSDL saved to disk
  * average 10 loops (time in seconds)
  * only parsing (no HTTP call)

Web services tested are AFIP (Argentina' IRS):
  * wsaa (authentication): Apache Axis version: 1.4 (2006, Java) [WSDL](https://wsaahomo.afip.gov.ar/ws/services/LoginCms?wsdl)
  * wsfe (electronic invoice): ASP.NET 2.0.50727 Microsoft-IIS/6.0 [WSDL](https://wswhomo.afip.gov.ar/wsfe/service.asmx?WSDL)
  * wsfex (foreing trade): ASP.NET 2.0.50727 Microsoft-IIS/6.0 [WSDL](https://wswhomo.afip.gov.ar/wsfex/service.asmx?WSDL)
  * wsctg (agriculture): Servlet 2.4; JBoss-4.2.1.GA Tomcat-5.5 - Apache/2.0.52 (Red Hat) [WSDL](https://fwshomo.afip.gov.ar/wsctg/services/CTGService?wsdl)
  * wdigdepfiel (customs): ASP.NET 2.0.50727 Microsoft-IIS/6.0 [WSDL](https://testdia.afip.gov.ar/Dia/Ws/wDigDepFiel/wDigDepFiel.asmx?wsdl)

Enviroment:
  * SW: python-2.5.4, lxml-2.2.6, pyxml-0.8.4
  * OS: Windows XP SP3
  * HW: Asus EeePC Atom N270 @ 1.60Hz 1GB

## Results ##

PySimpleSOAP seems to be as fast as the other compared python solutions (sometimes faster), without tunning (code is not optimized by now) nor external C libraries.

**Note**: some libraries failed our tests:
  * ZSI failed with soap1.2 (a custom wsfex.wsdl must be modified)
  * soaplib cannot parse wsdl at all

See TestingCompliance for more integration tests.

YMMV

### PySimpleSOAP (1.0.1a) ###
  * wsaa: 0.250s
  * wsfex: 3.703s (3.328s removed soap1.2)
  * wsctg: 1.171s
  * all: 7.438s

### suds (0.3.9) ###
  * wsaa: 0.625s
  * wsfex: 10.3s (9.89s removed soap1.2)
  * wsctg: 2.921s
  * all: 20.047s

### soappy (0.11.6 pyxml?) ###
  * wsaa: 0.234s
  * wsfex: 4.420s (4.015s removed soap1.2)
  * wsctg: 1.297s
  * all: 8.875s

### soaplib (0.8.1 libxml) ###
  * fails all tests (cannot read wsdl)

### szi (2.0.0-rc3) ###
  * wsaa: 0.265s
  * wsfex. fail (4.157s removed soap1.2)
  * wsctg: 1.359s
  * all: fail

## Sample Source Code ##

```
from pysimplesoap.client import SoapClient
import time
t0 = time.time()
loops = 10
for i in range(loops):
    print "loop", i, time.time() -t0
    client = SoapClient(wsdl='file:wsaa.wsdl')
    client = SoapClient(wsdl='file:wsfe.wsdl')
    client = SoapClient(wsdl='file:wsfex.wsdl')
    client = SoapClient(wsdl='file:wsctg.wsdl')
    client = SoapClient(wsdl='file:wdigdepfiel.wsdl')
t1 = time.time()
print "time elapsed (% i loops): %0.4f sec %0.4f avg" % (loops, t1- t0, (t1-t0)/loops)

```
##  ##
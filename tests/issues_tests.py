import unittest
from pysimplesoap.client import SoapClient, SoapFault, SimpleXMLElement

class TestIssues(unittest.TestCase):

    def test_issue19(self):
        "Test xsd namespace found under schema elementes"
        client = SoapClient(wsdl='http://www.destin8.co.uk/ISLInterface/ISLInterface?WSDL')

    def test_issue34(self):
        "Test soap_server SoapClient constructor parameter"
        client = SoapClient(wsdl="http://eklima.met.no/metdata/MetDataService?WSDL", soap_server="oracle", trace=True, cache=None)
        ##print client.help("getStationsProperties")
        ##print client.help("getValidLanguages")

        # fix bad wsdl: server returns "getValidLanguagesResponse" instead of "getValidLanguages12Response"
        output = client.services['MetDataService']['ports']['MetDataServicePort']['operations']['getValidLanguages']['output']['getValidLanguages12Response']
        client.services['MetDataService']['ports']['MetDataServicePort']['operations']['getValidLanguages']['output'] = {'getValidLanguagesResponse': output}

        lang = client.getValidLanguages()

        self.assertEqual(lang, {'return': [{'item': u'no'},{'item': u'en'}, {'item': u'ny'}]})

    def test_issue35_raw(self):    

        url = 'http://wennekers.epcc.ed.ac.uk:8080/axis/services/MetadataCatalogue'
        client = SoapClient(location=url,action="", trace=False)
        response = client.call("doEnsembleURIQuery", ("queryFormat", "Xpath"), ("queryString", "/markovChain"), ("startIndex", 0), ("maxResults", -1))
        self.assertEqual(str(response.statusCode), "MDC_INVALID_REQUEST")
        #print str(response.queryTime)
        self.assertEqual(int(response.totalResults), 0)
        self.assertEqual(int(response.startIndex), 0)
        self.assertEqual(int(response.numberOfResults), 0)

        for result in response.results:
            print str(result)

    def test_issue35_wsdl(self):
        "Test positional parameters, multiRefs and axis messages"
    
        url = 'http://wennekers.epcc.ed.ac.uk:8080/axis/services/MetadataCatalogue?WSDL'
        client = SoapClient(wsdl=url,trace=False, soap_server="axis")
        response = client.doEnsembleURIQuery(queryFormat="Xpath", queryString="/markovChain", startIndex=0, maxResults=-1)

        ret = response['doEnsembleURIQueryReturn']
        self.assertEqual(ret['statusCode'], "MDC_INVALID_REQUEST")
        self.assertEqual(ret['totalResults'], 0)
        self.assertEqual(ret['startIndex'], 0)
        self.assertEqual(ret['numberOfResults'], 0)


    def test_issue8(self):
        "Test europa.eu tax service (WSDL namespace)"

        VIES_URL='http://ec.europa.eu/taxation_customs/vies/services/checkVatService.wsdl'

        client = SoapClient(
                    location = "http://ec.europa.eu/taxation_customs/vies/services/checkVatService",
                    action = '', # SOAPAction
                    namespace = "urn:ec.europa.eu:taxud:vies:services:checkVat:types",
                    trace = False
                    )
        vat = 'BE0897290877'
        code = vat[:2]
        number = vat[2:]
        res = client.checkVat(countryCode=code, vatNumber=number)
        self.assertEqual(str(res('countryCode')), "BE")
        self.assertEqual(str(res('vatNumber')), "0897290877")
        self.assertEqual(str(res('name')), "SPRL B2CK")
        self.assertEqual(str(res('address')), "RUE DE ROTTERDAM 4 B21\n4000  LIEGE")

    ##def test_ups(self):
    ##    "Test UPS tracking service"
    ##    WSDL = "file:ups.wsdl"
    ##    client = SoapClient(wsdl=WSDL, ns="web", trace=True)
    ##    print client.help("ProcessTrack")

    def test_issue43(self):
        from pysimplesoap.client import SoapClient

        client = SoapClient(wsdl="https://api.clarizen.com/v1.0/Clarizen.svc",trace=False)

        print client.help("Login")
        print client.help("Logout")
        print client.help("Query")
        print client.help("Metadata")
        print client.help("Execute")

    def test_issue46(self):
        "Example for sending an arbitrary header using SimpleXMLElement"
        
        # fake connection (just to test xml_request):
        client = SoapClient(location="https://localhost:666/",namespace='http://localhost/api',trace=True)

        # Using WSDL, the equivalent is:
        # client['MyTestHeader'] = {'username': 'test', 'password': 'test'}

        headers = SimpleXMLElement("<Headers/>")
        my_test_header = headers.add_child("MyTestHeader")
        my_test_header['xmlns'] = "service"
        my_test_header.marshall('username', 'test')
        my_test_header.marshall('password', 'password')

        try:
            client.methodname(headers=headers)
        except:
            open("issue46.xml", "wb").write(client.xml_request)
            self.assert_("""<soap:Header><MyTestHeader xmlns="service"><username>test</username><password>password</password></MyTestHeader></soap:Header>""" in client.xml_request,
                        "header not in request!")


if __name__ == '__main__':
    test_issue35()
    unittest.main()
    

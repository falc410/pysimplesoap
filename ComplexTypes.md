# Introduction #

This is a complete example with complex types, used to develop a "simulator" of  AFIP (Argentina IRS) Electronic Invoice new webservices.

A live example is at:
**http://www.sistemasagiles.com.ar/simulador/wsfev1/call/soap**

# Simple Example #

## Xml Messages ##

### Request ###

```
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	<soap:Body>
		<FEDummy xmlns="https://www.sistemasagiles.com.ar/simulador/wsfev1/call/soap"/>
	</soap:Body>
</soap:Envelope>
```
### Response ###

```
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

	<soap:Body>
		<FEDummyResponse xmlns="https://www.sistemasagiles.com.ar/simulador/wsfev1/call/soap">
			<FEDummyResult>
				<AppServer>
					<!--string-->
				</AppServer>
				<AuthServer>
					<!--string-->
				</AuthServer>
				<DbServer>
					<!--string-->
				</DbServer>
			</FEDummyResult>
		</FEDummyResponse>
	</soap:Body>

</soap:Envelope>
```

## Server ##

```

@service.soap('FEDummy',returns={'FEDummyResult': {'AppServer': str, 'DbServer': str, 'AuthServer': str}},args={})
def dummy(): 
    "Metodo dummy para verificacion de funcionamiento"
    db.request.insert(method='dummy')
    return {'AppServer': 'OK', 'DbServer': 'OK', 'AuthServer': 'OK'}
```

## Client ##

```
def test_dummy():
    from gluon.contrib.pysimplesoap.client import SoapClient

    WSDL="https://www.sistemasagiles.com.ar/simulador/wsfev1/call/soap?WSDL=None"
    client = SoapClient(wsdl = WSDL)
    
    response.view = "generic.html"
    ret = client.FEDummy()
    
    return ret
```

## More complex example ##

## XML Messages ##

### Request ###
```
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	

	<soap:Body>
		<FECAESolicitar xmlns="https://www.sistemasagiles.com.ar/simulador/wsfev1/call/soap">
			<FeCAEReq>
				<FeCabReq>
					<CbteTipo>
						<!--int-->
					</CbteTipo>
					<PtoVta>
						<!--int-->
					</PtoVta>
					<CantReg>
						<!--int-->
					</CantReg>
				</FeCabReq>
				<FeDetReq>
					<!--Repetitive array of:-->
					<FECAEDetRequest>
						<ImpTotal>
							<!--float-->
						</ImpTotal>
						<MonId>
							<!--string-->
						</MonId>
						<ImpOpEx>
							<!--float-->
						</ImpOpEx>
						<Iva>
							<!--Repetitive array of:-->
							<AlicIva>
								<BaseImp>
									<!--float-->
								</BaseImp>
								<Id>
									<!--int-->
								</Id>
								<Importe>
									<!--float-->
								</Importe>
							</AlicIva>
						</Iva>
						<ImpIVA>
							<!--float-->
						</ImpIVA>
						<Tributos>
							<!--Repetitive array of:-->
							<Tributo>
								<Importe>
									<!--float-->
								</Importe>
								<Alic>
									<!--float-->
								</Alic>
								<BaseImp>
									<!--float-->
								</BaseImp>
								<Id>
									<!--int-->
								</Id>
								<Desc>
									<!--string-->
								</Desc>
							</Tributo>
						</Tributos>
						<CbteDesde>
							<!--long-->
						</CbteDesde>
						<Concepto>
							<!--int-->
						</Concepto>
						<FchServDesde>
							<!--string-->
						</FchServDesde>
						<DocNro>
							<!--long-->
						</DocNro>
						<ImpNeto>
							<!--float-->
						</ImpNeto>
						<FchVtoPago>
							<!--string-->
						</FchVtoPago>
						<CbteHasta>
							<!--long-->
						</CbteHasta>
						<DocTipo>
							<!--int-->
						</DocTipo>
						<FchServHasta>
							<!--string-->
						</FchServHasta>
						<MonCotiz>
							<!--float-->
						</MonCotiz>
						<ImpTrib>
							<!--float-->
						</ImpTrib>
						<ImpTotConc>
							<!--float-->
						</ImpTotConc>
						<CbteFch>
							<!--string-->
						</CbteFch>
						<CbtesAsoc>
							<!--Repetitive array of:-->
							<CbteAsoc>
								<Nro>
									<!--long-->
								</Nro>
								<PtoVta>
									<!--int-->
								</PtoVta>
								<Tipo>
									<!--int-->
								</Tipo>
							</CbteAsoc>
						</CbtesAsoc>
					</FECAEDetRequest>
				</FeDetReq>
			</FeCAEReq>
			<Auth>
				<Token>
					<!--string-->
				</Token>
				<Cuit>
					<!--string-->
				</Cuit>
				<Sign>
					<!--string-->
				</Sign>
			</Auth>
		</FECAESolicitar>
	</soap:Body>
	

</soap:Envelope>
```

### Response ###

```
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
	

	<soap:Body>
		<FECAESolicitarResponse xmlns="https://www.sistemasagiles.com.ar/simulador/wsfev1/call/soap">
			<FECAESolicitarResult>
				<Errors>
					<!--Repetitive array of:-->
					<Err>
						<Msg>
							<!--string-->
						</Msg>
						<Code>
							<!--int-->
						</Code>
					</Err>
				</Errors>
				<FeCabResp>
					<Resultado>
						<!--string-->
					</Resultado>
					<Cuit>
						<!--long-->
					</Cuit>
					<CbteTipo>
						<!--int-->
					</CbteTipo>
					<PtoVta>
						<!--int-->
					</PtoVta>
					<Reproceso>
						<!--string-->
					</Reproceso>
					<FchProceso>
						<!--string-->
					</FchProceso>
					<CantReg>
						<!--int-->
					</CantReg>
				</FeCabResp>
				<FeDetResp>
					<!--Repetitive array of:-->
					<FECAEDetResponse>
						<Resultado>
							<!--string-->
						</Resultado>
						<CbteDesde>
							<!--long-->
						</CbteDesde>
						<Concepto>
							<!--int-->
						</Concepto>
						<CAEFchVto>
							<!--string-->
						</CAEFchVto>
						<DocNro>
							<!--long-->
						</DocNro>
						<CAE>
							<!--string-->
						</CAE>
						<CbteHasta>
							<!--long-->
						</CbteHasta>
						<DocTipo>
							<!--int-->
						</DocTipo>
						<Observaciones>
							<!--Repetitive array of:-->
							<Obs>
								<Msg>
									<!--string-->
								</Msg>
								<Code>
									<!--int-->
								</Code>
							</Obs>
						</Observaciones>
						<CbteFch>
							<!--string-->
						</CbteFch>
					</FECAEDetResponse>
				</FeDetResp>
				<Events>
					<!--Repetitive array of:-->
					<Evt>
						<Msg>
							<!--string-->
						</Msg>
						<Code>
							<!--int-->
						</Code>
					</Evt>
				</Events>
			</FECAESolicitarResult>
		</FECAESolicitarResponse>
	</soap:Body>
	

</soap:Envelope>
```

## Client ##
```

WSDL="https://www.sistemasagiles.com.ar/simulador/wsfev1/call/soap?WSDL=None"
client = SoapClient(wsdl = WSDL)

ret = client.FECAESolicitar(
            Auth={'Token': token, 'Sign': sign, 'Cuit': CUIT},
            FeCAEReq={
                'FeCabReq': {'CantReg':1, 'PtoVta': 1, 'CbteTipo': 10},
                'FeDetReq': [{'FECAEDetRequest': {
                    'Concepto': 0,
                    'DocTipo': 80,
                    'DocNro': 20111111119,
                    'CbteDesde': 1,
                    'CbteHasta': 2,
                    'CbteFch': '20101006',
                    'ImpTotal': '1000.10',
                    'ImpTotConc': "10.00",
                    'ImpNeto': "100.00",
                    'ImpOpEx': "0.00",
                    'ImpTrib':  "1.00",
                    'ImpIVA': "21.00",
                    'FchServDesde': '20101101',
                    'FchServHasta': '20101130',
                    'FchVtoPago': '20101014',
                    'MonId': 'DOL',
                    'MonCotiz': '3.985',
                    'CbtesAsoc': [
                    {'CbteAsoc': {'Tipo': 19, 'PtoVta': 2, 'Nro': 1234}}
                    ],
                    'Tributos': [
                    {'Tributo': {
                        'Id': 0, 
                        'Desc': 'Impuesto Municipal Matanza',
                        'BaseImp': 150,
                        'Alic': 5.2,
                        'Importe': 5.8,
                        }}
                    ],
                    'Iva': [ 
                    {'AlicIva': {
                        'Id': 5,
                        'BaseImp': 100,
                        'Importe': 21,
                        }}
                    ],
                    }
                }]
            })
```

## Server ##

```
@service.soap('FECAESolicitar',
    returns={'FECAESolicitarResult': {
        'FeCabResp': {'Cuit': long, 'PtoVta': int, 'CbteTipo': int, 
                      'FchProceso': str, 'CantReg': int, 'Resultado': unicode, 
                      'Reproceso': unicode}, 
        'FeDetResp': [{'FECAEDetResponse': 
            {'Concepto': int, 'DocTipo': int, 'DocNro': long, 
             'CbteDesde': long, 'CbteHasta': long, 'CbteFch': unicode, 
             'CAE': str, 'CAEFchVto': str,
             'Resultado': str, 
             'Observaciones': [{'Obs': {'Code': int, 'Msg': unicode}}]}}], 
         'Events': [{'Evt': {'Code': int, 'Msg': unicode}}], 
         'Errors': [{'Err': {'Code': int, 'Msg': unicode}}]}},
    args={
        'Auth': {'Token': str, 'Sign': str, 'Cuit': str},
        'FeCAEReq': {
            'FeCabReq': {'CantReg': int, 'PtoVta': int, 'CbteTipo': int},
            'FeDetReq': [{'FECAEDetRequest': {
                'Concepto': int,
                'DocTipo': int,
                'DocNro': long,
                'CbteDesde': long,
                'CbteHasta': long,
                'CbteFch': str,
                'ImpTotal': float,
                'ImpTotConc': float,
                'ImpNeto': float,
                'ImpOpEx': float,
                'ImpTrib':  float,
                'ImpIVA': float,
                'FchServDesde': str,
                'FchServHasta': str,
                'FchVtoPago': str,
                'MonId': str,
                'MonCotiz': float,
                'CbtesAsoc': [
                {'CbteAsoc': {'Tipo': int, 'PtoVta': int, 'Nro': long}}
                ],
                'Tributos': [
                {'Tributo': {
                    'Id': int, 
                    'Desc': unicode,
                    'BaseImp': float,
                    'Alic': float,
                    'Importe': float,
                    }}
                ],
                'Iva': [ 
                {'AlicIva': {
                    'Id': int,
                    'BaseImp': float,
                    'Importe': float,
                    }}
                ],
                }
            }]
        }})
def cae_solicitar(Auth, FeCAEReq): 
    "Solicitud de Codigo de Autorizacion Electronico (CAE)"
    try:
        FeCabReq = FeCAEReq['FeCabReq']
        FeDetReq = FeCAEReq['FeDetReq']
        db.request.insert(method='cae_solicitar', args=repr({'Auth': Auth, 'FeCAEReq': FeCAEReq}))
        return {
            'FeCabResp': {'Cuit': Auth['Cuit'], 
                          'PtoVta': FeCabReq['PtoVta'], 'CbteTipo': FeCabReq['CbteTipo'], 
                          'CantReg': FeCabReq['CantReg'], 
                          'FchProceso': "20101006", 
                          'Resultado': "A", 
                          'Reproceso': "N"}, 
            'FeDetResp': [{'FECAEDetResponse': 
                {'Concepto': f['FECAEDetRequest']['Concepto'], 
                 'DocTipo': f['FECAEDetRequest']['DocTipo'], 'DocNro': f['FECAEDetRequest']['DocNro'], 
                 'CbteDesde': f['FECAEDetRequest']['CbteDesde'], 'CbteHasta': f['FECAEDetRequest']['CbteHasta'], 
                 'CAE': "123456789012345",
                 'CbteFch': f['FECAEDetRequest']['CbteFch'], 
                 'CAEFchVto': f['FECAEDetRequest']['CbteFch'], 
                 'Resultado': "A", 
                 'Observaciones': [{'Obs': {'Code': 00, 'Msg': "Todo bien"}}]}} 
                      for f in FeDetReq], 
             'Events': [{'Evt': {'Code': 0, 'Msg': 'Esto es una SIMULACION!!!'}}], 
             'Errors': [{'Err': {'Code': 10001, 'Msg': 'Datos no validos - simulados'}}]}
    except Exception, e:
        raise RuntimeError("%s" % f['FECAEDetRequest'].keys())
```
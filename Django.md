# Introduction #

This page describes how to create a SOAP server using Django.
Please see [issue 5](https://code.google.com/p/pysimplesoap/issues/detail?id=5), SoapDispatcher, and Web2Py for more information.
Thanks d4rk92 for the contributed example.


# Details #

```

# A simple views.py file sample for dispatcher
from pysimplesoap.server import SoapDispatcher
from django.http import HttpResponse

# just a remote function ;)
def func(data):
    return data

# dispatcher declaration: however you like to declare it ;)
dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8000/soap",
    action = 'http://localhost:8000/soap',
    namespace = "http://blah.blah.org/blah/blah/local",
    prefix="bl1",
    ns = "bl2")

# register func
dispatcher.register_function('func', func,
    returns={'result': str}, 
    args={'data': str})

def dispatcher_handler(request):
    if request.method == "POST":
        response = HttpResponse(mimetype="application/xml")
        response.write(dispatcher.dispatch(request.raw_post_data))
    else:
        response = HttpResponse(mimetype="application/xml")
        response.write(dispatcher.wsdl())
    response['Content-length'] = str(len(response.content))
    return response

```
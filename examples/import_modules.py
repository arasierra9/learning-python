import datetime as dt
print(dt.datetime.now())

from datetime import datetime as dt
print(dt.now())

import tornado.web as web
request = web.RequestHandler

from tornado import web
request = web.RequestHandler


try:
    import modulo
except ImportError:
    modulo = None

print(modulo)


if modulo is not None:
    modulo()
if callable(modulo):
    modulo()


try:
    import modulo
except ImportError:
    def modulo():
        print('it is my module...')


print(modulo)

if modulo is not None:
    print('Modulo ok.')
    modulo()
if callable(modulo):
    print('Modulo ok.')
    modulo()

#!/usr/bin/env python3

from aiohttp import web
from jsonrpcserver.aio import methods
from jsonrpcserver.exceptions import InvalidParams
import datetime
import json
import os
from kaleidoscope.state import KaleidoscopeStateManager

APP_DIRECTORY = '/app'

class KaleidoscopeHTTPServer(object):

    def __init__(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs
        self.storageengine = kwargs.get('storagedriver',None)
        self.state = KaleidoscopeStateManager(self.storageengine)
        self.version = self._app_version()
        self.app = web.Application()

    def _app_version(self):
        p = os.path.join(APP_DIRECTORY, "gitversion.txt")
        if os.path.isfile(p):
            with open(p,"r") as f:
                return f.read().rstrip()
        else:
            return 'unknown'

    def serve(self):
        async def handle(request):
            request = await request.text()
            response = await methods.dispatch(request)
            if response.is_notification:
                return web.Response()
            else:
                return web.json_response(response, status=response.http_status)

        async def healthcheck(request):
            #request = await request.text()
            return web.Response(text=json.dumps({
                'service': 'kaleidoscope',
                'ok': True,
                'version': self.version,
                'date': utcisodatestr()
            }))

        self.app.router.add_get('/.well-known/healthcheck.json', healthcheck)
        self.app.router.add_post('/', handle)
        # app.router.add_get('/', serveapp) TODO
        web.run_app(self.app, port=os.environ.get('PORT',8080))

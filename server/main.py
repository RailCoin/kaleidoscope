#!/usr/bin/env python3

from aiohttp import web
from jsonrpcserver.aio import methods
import datetime
import json
import os

APP_DIRECTORY = '/var/kaleidoscope'

def app_version():
    p = os.path.join(APP_DIRECTORY, "gitversion.txt")
    if os.path.isfile(p):
        with open(p,"r") as f:
            return f.read().rstrip()
    else:
        return 'unknown'

APP_VERSION = app_version()

@methods.add
async def ping():
    return 'pong'

def utcisodatestr():
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()

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
        'version': APP_VERSION,
        'date': utcisodatestr()
    }))

def main():
    app = web.Application()
    app.router.add_get('/.well-known/healthcheck.json', healthcheck)
    app.router.add_post('/', handle)
    # app.router.add_get('/', serveapp) TODO

    web.run_app(app, port=os.environ.get('PORT',8080))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

from jsonrpcserver.aio import methods
from jsonrpcserver.exceptions import InvalidParams
import datetime
import json
import os
from kaleidoscope.state import KaleidoscopeState

from kaleidoscope.server import APP_STATE as state

@methods.add
async def propose_new_transaction(**kwargs):
    if 'tx' not in kwargs:
        raise InvalidParams()
    # FIXME(sneak) write new transaction into app state

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

if __name__ == '__main__':
    main()

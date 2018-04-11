#!/usr/bin/env python3

from jsonrpcserver.aio import methods
from jsonrpcserver.exceptions import InvalidParams
from kaleidoscope.state import KaleidoscopeStateManager

@methods.add
async def propose_new_transaction(**kwargs):
    if 'tx' not in kwargs:
        raise InvalidParams()
    # FIXME(sneak) write new transaction into app state

@methods.add
async def ping():
    return 'pong'

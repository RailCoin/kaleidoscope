#!/usr/bin/env python3

import os
import boto3

class KaleidoscopeState(object):
    def __init__(self,storagedriver):
        self._storage = storagedriver()
        self._state = {}

    def save(self):
        self._storage.save(self)

#!/usr/bin/env python3

import os
import boto3

class KaleidoscopeStateManager(object):
    def __init__(self,storagedriver):
        self._storage = storagedriver()
        self._state = {}

    def save(self):
        self._storage.save(self)

    def load(self):
        self._state = self._storage.load()

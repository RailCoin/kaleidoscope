#!/usr/bin/env python3

from kaleidoscope.server import KaleidoscopeHTTPServer
from kaleidoscope.storage import QuickDirtyS3Storage, SimpleLocalStorage

def main():
    #s = KaleidoscopeHTTPServer(storagedriver=QuickDirtyS3Storage)
    s = KaleidoscopeHTTPServer(storagedriver=SimpleLocalStorage)
    s.serve()

if __name__ == '__main__':
    main()

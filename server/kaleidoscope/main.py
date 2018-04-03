#!/usr/bin/env python3

from kaleidoscope.server import KaleidoscopeHTTPServer
from kaleidoscope.storage import QuickDirtyStorage

def main():
    s = KaleidoscopeHTTPServer(storagedriver=QuickDirtyStorage)
    s.serve()

if __name__ == '__main__':
    main()

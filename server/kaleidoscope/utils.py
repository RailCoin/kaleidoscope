#!/usr/bin/env python3
import datetime

def utcisodatestr():
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()

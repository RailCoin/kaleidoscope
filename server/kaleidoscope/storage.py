#!/usr/bin/env python3

import os
import boto3
import StringIO

class QuickDirtyStorage(object):
    def __init__(self):
        self.bucketname = os.environ.get('KALEIDOSCOPE_S3_BUCKET')
        self.filename = 'kaleidoscope-appstate.json'
        resource = boto3.resource('s3')
        self.bucket = resource.Bucket(self.bucketname)

    def load(self):
        buf = StringIO.StringIO()
        self.bucket.download_fileobj(self.filename, buf)
        return json.loads(str(buf))

    def save(self,obj):
        buf = StringIO.StringIO(json.dumps(obj))
        self.bucket.upload_fileobj(buf, self.filename)

#!/usr/bin/env python
# Delete files older than 30 days that ends with .tif
import os
import datetime
import sys

if len(sys.argv) != 2:
    print("Usage: python deleteOldFiles.py /path/to/folder")
    exit()

workdir = sys.argv[1]
olderThanDays = 30

for dirpath, dirnames, filenames in os.walk(workdir):
    for file in filenames:
        curpath = os.path.join(dirpath, file)
        file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))
        if datetime.datetime.now() - file_modified > datetime.timedelta(days=olderThanDays) and curpath.endswith('.tif'):
            os.unlink(curpath)
            print("removed {}".format(curpath))

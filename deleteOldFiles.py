#!/usr/bin/env python
# Delete files older than 30 days that ends with .tif
import os
import datetime
import logging
import sys

if len(sys.argv) != 2:
    print("Usage: python deleteOldFiles.py /path/to/folder")
    exit()

OLDERTHANDAYS = 30
WORKDIR = sys.argv[1]

logging.basicConfig(filename=WORKDIR + os.sep + 'deleteOldFiles.log', level=logging.DEBUG)

for dirpath, dirnames, filenames in os.walk(WORKDIR):
    for file in filenames:
        curpath = os.path.join(dirpath, file)
        file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))
        if datetime.datetime.now() - file_modified > datetime.timedelta(days=OLDERTHANDAYS) and curpath.endswith('.TIF'):
            os.unlink(curpath)
            logging.info("[{}] removed file: {}".format(datetime.date.strftime(datetime.datetime.now(), '%c'), curpath))

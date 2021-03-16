# Description
I hate windoze but still have to touch it at work. So here is a repo where I can put stuff I use on windoze.

# deleteOldFiles.py

This script will delete all the '.TIF' files older than 30 days in a given directory. This way you keep the folders and .nd, .mds or .stg files but remove the heavy and numerous .tif files.

## How to use

* Install python 3 from [Python website](https://www.python.org)
* Go to "Task scheduler" and create a new task
* Use the python executable for program to start and add the script as argument + path to folder to clean up

# copyFiles.py

The idea is to watch for filesystem events in a directory and copy the new files to another disk.

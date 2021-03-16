#!/usr/bin/env python
# Copy files to the Backup SSD
import os
import datetime
import logging
import sys
import time
from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler
from shutil import copy2


BACKUP_DIR = "G:\\backup_data"
SRC_DIR = "D:\\Users"

class ImagesWatcher:
    def __init__(self, src_path):
        self.__src_path = src_path
        self.__event_handler = ImagesEventHandler()
        self.__event_observer = Observer()

    def run(self):
        self.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=True
        )

class ImagesEventHandler:


    def __init__(self):
        pass

    def on_created(self, event):
        self.process(event)

    def dispatch(self, event):
        if event.event_type == "created" and event.is_directory == False:
            copy2(event.src_path, BACKUP_DIR)

if __name__ == "__main__":
    ImagesWatcher(SRC_DIR).run()

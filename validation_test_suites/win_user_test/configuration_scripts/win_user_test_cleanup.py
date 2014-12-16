#!/usr/bin/env python

__author__ = 'matt.kerr'
__copyright__ = "Copyright 2011, G2, Inc."
__credits__ = ["Matt Kerr"]
__license__ = "TODO"
__version__ = "TODO"
__maintainer__ = 'matt.kerr'
__email__ = "TODO"
__status__ = "Alpha"

from subprocess import *
import time

def performConfig(workingDir=None):
    # delete groups
    Popen(["net","localgroup","testgroup1","/delete"])
    Popen(["net","localgroup","testgroup2","/delete"])
    Popen(["net","localgroup","testgroup3","/delete"])
    # delete users
    Popen(["net","user","jdoe","/delete"])
    Popen(["net","user","jdoe1","/delete"])

    time.sleep(2)
    return

if __name__=="__main__":
    performConfig()
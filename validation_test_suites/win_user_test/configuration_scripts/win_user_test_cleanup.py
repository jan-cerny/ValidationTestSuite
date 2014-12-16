#!/usr/bin/env python

__author__ = 'matt.kerr'
__copyright__ = "Copyright 2011, G2, Inc."
__credits__ = ["Matt Kerr"]
__license__ = "TODO"
__version__ = "TODO"
__maintainer__ = 'matt.kerr'
__email__ = "TODO"
__status__ = "Alpha"

import subprocess
import time

def performConfig(workingDir=None):
    # delete groups
    subprocess.call(["net","localgroup","testgroup1","/delete"])
    subprocess.call(["net","localgroup","testgroup2","/delete"])
    subprocess.call(["net","localgroup","testgroup3","/delete"])
    # delete users
    subprocess.call(["net","user","jdoe","/delete"])
    subprocess.call(["net","user","jdoe1","/delete"])

    return

if __name__=="__main__":
    performConfig()
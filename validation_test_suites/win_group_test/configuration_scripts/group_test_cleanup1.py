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

def performConfig(workingDir=None):
    # remove from guests group
    Popen(["net","localgroup","guests","testuser","/delete"])
    Popen(["net","localgroup","guests","testsub1","/delete"])
    # delete groups
    Popen(["net","localgroup","testsub1","/delete"])
    Popen(["net","localgroup","testsub2","/delete"])
    # delete users
    Popen(["net","user","testuser","/delete"])
    Popen(["net","user","testuser2","/delete"])
    return

if __name__=="__main__":
    performConfig()
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
    #disable the administrator account
    Popen(["net","user","administrator","/active:no"])

if __name__ == "__main__":
    performConfig()
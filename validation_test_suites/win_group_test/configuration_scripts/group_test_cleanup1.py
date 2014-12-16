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


def performConfig(workingDir=None):
    # remove from guests group
    subprocess.call(["net","localgroup","guests","testuser","/delete"])
    subprocess.call(["net","localgroup","guests","testsub1","/delete"])
    # delete groups
    subprocess.call(["net","localgroup","testsub1","/delete"])
    subprocess.call(["net","localgroup","testsub2","/delete"])
    # delete users
    subprocess.call(["net","user","testuser","/delete"])
    subprocess.call(["net","user","testuser2","/delete"])
    return

if __name__=="__main__":
    performConfig()
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
    #Create users
    Popen(["net","user","testuser","Geek!234567","/add"])
    Popen(["net","user","testuser2","Geek!234567","/add"])
    time.sleep(2)

    #Create groups
    Popen(["net","localgroup","testsub1","/add"])
    Popen(["net","localgroup","testsub2","/add"])
    time.sleep(2)

    #add users to groups
    Popen(["net","localgroup","guests","testuser2","/add"])
    Popen(["net","localgroup","guests","testsub2","/add"])
    time.sleep(2)

    print("I'm done.")
	
	
if __name__=="__main__":
    performConfig()
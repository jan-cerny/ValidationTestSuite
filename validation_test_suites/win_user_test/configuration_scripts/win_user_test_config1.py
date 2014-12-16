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
    Popen(["net","user","jdoe","Geek!234567","/add" ,"/active:yes"])
    Popen(["net","user","jdoe1","Geek!234567","/add" ,"/active:yes"])

    time.sleep(2)

    #Create groups
    Popen(["net","localgroup","testgroup1","/add"])
    Popen(["net","localgroup","testgroup2","/add"])
    Popen(["net","localgroup","testgroup3","/add"])

    time.sleep(2)

    #add users to groups
    Popen(["net","localgroup","testgroup1","jdoe","/add"])
    Popen(["net","localgroup","testgroup2","jdoe","/add"])
    Popen(["net","localgroup","testgroup1","jdoe1","/add"])
    Popen(["net","localgroup","testgroup2","jdoe1","/add"])

    time.sleep(2)


if __name__=="__main__":
    performConfig()
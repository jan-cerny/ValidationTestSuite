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
import random
import string

def performCleanup(workingDir=None):
    # delete groups
    subprocess.call(["net","localgroup","testgroup1","/delete"])
    subprocess.call(["net","localgroup","testgroup2","/delete"])
    subprocess.call(["net","localgroup","testgroup3","/delete"])
    # delete users
    subprocess.call(["net","user","jdoe","/delete"])
    subprocess.call(["net","user","jdoe1","/delete"])
    return

def performGenPassword(workingDir=None):
    chars = string.ascii_letters + string.digits + string.punctuation
    newpasswdgen = ''
    length = 14
    for i in range(length):
        newpasswdgen = ''.join(random.choice(chars) for x in range(length))
    return newpasswdgen

def performConfig(workingDir=None):
    #Cleanup first
    print ("\n----------------------------------")
    print ("Deleting the existing configuration...")
    performCleanup()
    print ("\n----------------------------------")
    print ("Configuring the system...")
    newpass = performGenPassword()
    print ("Generated complex password: ", newpass)
    #Create users
    subprocess.call(["net","user","jdoe",newpass,"/add","/active:yes"])
    subprocess.call(["net","user","jdoe1",newpass,"/add","/active:no"])

    #Create groups
    subprocess.call(["net","localgroup","testgroup1","/add"])
    subprocess.call(["net","localgroup","testgroup2","/add"])
    subprocess.call(["net","localgroup","testgroup3","/add"])

    #add users to groups
    subprocess.call(["net","localgroup","testgroup2","jdoe","/add"])
    subprocess.call(["net","localgroup","testgroup3","jdoe","/add"])
    subprocess.call(["net","localgroup","testgroup1","jdoe1","/add"])
    subprocess.call(["net","localgroup","testgroup2","jdoe1","/add"])

if __name__=="__main__":
    performConfig()
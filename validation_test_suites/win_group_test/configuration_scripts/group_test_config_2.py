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
    # remove from guests group
    subprocess.call(["net","localgroup","guests","testuser","/delete"])
    subprocess.call(["net","localgroup","guests","testsub1","/delete"])
    # delete groups
    subprocess.call(["net","localgroup","testsub1","/delete"])
    subprocess.call(["net","localgroup","testsub2","/delete"])
    # delete users
    subprocess.call(["net","user","testuser","/delete"])
    subprocess.call(["net","user","testuser2","/delete"])
    # remove from guests group
    subprocess.call(["net","localgroup","guests","testuser2","/delete"])
    subprocess.call(["net","localgroup","guests","testsub2","/delete"])
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
    print ("creating user: 'testuser'")
    subprocess.call(["net","user","testuser",newpass,"/add"])
    print ("creating user: 'testuser2'")
    subprocess.call(["net","user","testuser2",newpass,"/add"])

    #Create groups
    print ("creating group: 'testsub1'")
    subprocess.call(["net","localgroup","testsub1","/add"])
    print ("creating group: 'testsub2'")
    subprocess.call(["net","localgroup","testsub2","/add"])

    #add users to groups
    subprocess.call(["net","localgroup","guests","testuser2","/add"])
    subprocess.call(["net","localgroup","guests","testsub2","/add"])
    print("I'm done.")
	
	
if __name__=="__main__":
    performConfig()
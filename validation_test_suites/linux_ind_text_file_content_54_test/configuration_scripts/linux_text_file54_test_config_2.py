#!/usr/bin/env python

__author__ = 'matt.kerr'
__copyright__ = "Copyright 2011, G2, Inc."
__credits__ = ["Matt Kerr"]
__license__ = "TODO"
__version__ = "TODO"
__maintainer__ = 'matt.kerr'
__email__ = "TODO"
__status__ = "Alpha"

import os

def performConfig(workingDir=None):
    if not os.path.exists(r"/scap_validation_content"):
        os.mkdir(r"/scap_validation_content")
    if not os.path.exists(r"/scap_validation_content/ind_tfc_53"):
        os.mkdir(r"/scap_validation_content/ind_tfc_53")
    file_path=r"/scap_validation_content/ind_tfc_53/a"
    #check to see if the validation program directory is present
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    createFile(r"/scap_validation_content/ind_tfc_53/a/1.txt","1234567890a\nabcdefghijklmnopqrstuvwxyz")
    createFile(r"/scap_validation_content/ind_tfc_53/a/2.txt","aaaaaaaaaaaa")
    return
def createFile(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    return

if __name__=="__main__":
    performConfig()

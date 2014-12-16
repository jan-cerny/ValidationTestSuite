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
    file_path=r"C:/scap_validation_content"
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_path = os.path.join(file_path,'ind_file_hash')
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    if not os.path.exists(os.path.join(file_path,r'e')):
        os.makedirs(os.path.join(file_path,r'e'))
    if not os.path.exists(os.path.join(file_path,r'1e')):
        os.makedirs(os.path.join(file_path,r'1e'))
    create_file(r"C:\scap_validation_content\ind_file_hash\e\test.bak",'OVAL Test')
    return
def create_file(filename, content):
    with open(filename,'w') as a:
        a.write(content)
    return

if __name__=="__main__":
    performConfig()
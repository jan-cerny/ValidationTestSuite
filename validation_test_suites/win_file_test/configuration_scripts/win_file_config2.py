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
    if not os.path.exists(r'\scap_validation_content'):
        os.mkdir(r'\scap_validation_content')
    if os.path.exists(r'c:\scap_validation_content\win_file\e\1.txt'):
        os.remove(r'c:\scap_validation_content\win_file\e\1.txt')
    if os.path.exists(r'c:\scap_validation_content\win_file\e\2.txt'):
        os.remove(r'c:\scap_validation_content\win_file\e\2.txt')
    if os.path.exists(r'c:\scap_validation_content\win_file\e\Skeleton.exe'):
        os.remove(r'c:\scap_validation_content\win_file\e\Skeleton.exe')
    if os.path.exists(r'c:\scap_validation_content\win_file'):
        os.removedirs(r'c:\scap_validation_content\win_file\e')
    return

if __name__ == "__main__":
    performConfig()
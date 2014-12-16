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
import shutil
import time
import datetime

def performConfig(workingDir=None):
    file1 = r'\scap_validation_content\win_file\e\1.txt'
    file2 = r'\scap_validation_content\win_file\e\2.txt'

    # check for existence of files and create if necessary
    if not os.path.exists(r'\scap_validation_content'):
        os.mkdir(r'\scap_validation_content')
    if not os.path.exists(r'\scap_validation_content\win_file'):
        os.mkdir(r'\scap_validation_content\win_file')
    if not os.path.exists(r'\scap_validation_content\win_file\e'):
        os.mkdir(r'\scap_validation_content\win_file\e')
    if not os.path.exists(file1):
        open(file1, "w").close()
    if not os.path.exists(file2):
        open(file2, "w").close()

    # copy the skeleton.exe file to c:\scap_validation_content\win_file
    if workingDir is not None:
        srcFile = os.path.join(workingDir, 'Skeleton.exe')
    else:
        srcFile = r'Skeleton.exe'
    dstFile = os.path.join(r'\scap_validation_content\win_file\e',r'Skeleton.exe')
    shutil.copy(srcFile, dstFile)
    t = makeTime(year=2011, day=29, month=6, hour=11, min=59, sec=0)
    os.utime(dstFile, (t,t))
    return

def makeTime(year = None, day=None, month=None, hour=None, min=None, sec=None):
    d = datetime.datetime(year, month, day, hour, min, sec, 0, None)
    t = time.mktime(d.utctimetuple())
    return t

if __name__ == "__main__":
    performConfig()
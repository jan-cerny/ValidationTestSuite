#!/usr/bin/env python

__author__ = 'matt.kerr'
__copyright__ = "Copyright 2011, G2, Inc."
__credits__ = ["Matt Kerr"]
__license__ = "TODO"
__version__ = "TODO"
__maintainer__ = 'matt.kerr'
__email__ = "TODO"
__status__ = "Alpha"

import shutil
import os

def performConfig(workingDir=None):
    file_path=r'/scap_validation_content/ind_file_hash'
    if os.path.exists(file_path):
        shutil.rmtree(file_path)
	
if __name__== "__main__":
    performConfig()
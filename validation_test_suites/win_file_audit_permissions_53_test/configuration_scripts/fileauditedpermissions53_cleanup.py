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

def performConfig(workingDir=None):
    print('Beginning Cleanup ...')
    shutil.rmtree(r'c:\scap_validation_content')
    print('Cleanup Complete ...')
    return

if __name__ == "__main__":
    performConfig()
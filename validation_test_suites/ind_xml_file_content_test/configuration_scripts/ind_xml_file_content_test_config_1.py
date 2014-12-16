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

def performConfig(workingDir=None):
    os.makedirs(r"C:\scap_validation_content\ind_xml\e", exist_ok=True)
    os.makedirs(r"C:\scap_validation_content\ind_xml\ne", exist_ok=True)
    createFile(r"C:\scap_validation_content\ind_xml\e\1.xml")
    createFile(r"C:\scap_validation_content\ind_xml\e\books.xml")
    createFile(r"C:\scap_validation_content\ind_xml\e\1.txt")
    return
def createFile(filename):
    with open(filename,'w') as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<bookstore>\n')
        file.write('\t<book category="food">\n')
        file.write('\t\t<title>Everyday Italian</title>\n')
        file.write('\t\t<author>Giada De Laurentiis</author>\n')
        file.write('\t\t<year>2005</year>\n')
        file.write('\t\t<price>29.99</price>\n')
        file.write('\t</book>\n')
        file.write('\t<book category="language">\n')
        file.write('\t\t<title>Teach Me Everyday German</title>\n')
        file.write('\t\t<author>Judy Mahoney</author>\n')
        file.write('\t\t<year>2008</year>\n')
        file.write('\t\t<price>39.95</price>\n')
        file.write('\t</book>\n')
        file.write('</bookstore>\n')
    return
if __name__ == "__main__":
    performConfig()
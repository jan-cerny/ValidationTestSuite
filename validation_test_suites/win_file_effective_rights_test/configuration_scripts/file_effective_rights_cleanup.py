__author__ = 'matt.kerr'

import os

def performConfig(workingDir=None):
    if os.path.exists(r'c:C:\scap_validation_content\win_fer\e\1.txt'):
        os.remove(r'c:C:\scap_validation_content\win_fer\e\1.txt')
    if os.path.exists(r'c:C:\scap_validation_content\win_fer\e\2.txt'):
        os.remove(r'c:C:\scap_validation_content\win_fer\e\2.txt')
    if os.path.exists(r'c:C:\scap_validation_content\win_fer'):
        os.removedirs(r'c:C:\scap_validation_content\win_fer\e')
    return

if __name__ == "__main__":
    performConfig()
  
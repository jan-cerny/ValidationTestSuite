__author__ = 'matt.kerr'

import os

def performConfig(workingDir=None):
    if os.path.exists(r'c:\scap_validation_content\win_fer53\e\1.txt'):
        os.remove(r'c:\scap_validation_content\win_fer53\e\1.txt')
    if os.path.exists(r'c:\scap_validation_content\win_fer53\e\2.txt'):
        os.remove(r'c:\scap_validation_content\win_fer53\e\2.txt')
    if os.path.exists(r'c:\scap_validation_content\win_fer53'):
        os.removedirs(r'c:\scap_validation_content\win_fer53\e')
    return

if __name__ == "__main__":
    performConfig()
  
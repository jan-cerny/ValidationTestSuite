#!/usr/bin/env python

__author__ = 'matt.kerr'
__copyright__ = "Copyright 2011, G2, Inc."
__credits__ = ["Matt Kerr"]
__license__ = "TODO"
__version__ = "TODO"
__maintainer__ = 'matt.kerr'
__email__ = "TODO"
__status__ = "Alpha"

import winreg

def performConfig(workingDir = None):
    # recursively delete
    recursiveRegDelete(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\MSMQ\\SCAP_Validation_Tests\\')
    return

def recursiveRegDelete(hive, key):
    # open key
    hKey = winreg.OpenKey(hive, key, 0, winreg.KEY_ALL_ACCESS)
    # enumerate values
    values = getValues(hKey)
    # delete values
    for value in values:
        winreg.DeleteValue(hKey, value)

    # enumerate subkeys
    keys = getKeys(hKey)
    # Call recursiveRegDelete on subkey
    for subkey in keys:
        recursiveRegDelete(hive, key + subkey + '\\' )
    # close the key
    winreg.CloseKey(hKey)
    #delete key
    winreg.DeleteKey(hive, key)
    return
def getKeys(handle):
    retValue = []
    done = False
    index = 0
    while done != True:
        try:
            key = winreg.EnumKey(handle, index)
            index += 1
            retValue.append(key)
        except:
            done = True
    return retValue
def getValues(handle):
    retValue = []
    index = 0
    done = False
    while done != True:
        try:
            value = winreg.EnumValue(handle, index)
            index += 1
            retValue.append(value[0])
        except:
            done = True
    return retValue

if __name__ == "__main__":
    performConfig()
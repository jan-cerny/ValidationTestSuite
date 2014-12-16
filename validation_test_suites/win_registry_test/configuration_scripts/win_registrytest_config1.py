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
import array

def performConfig(workingDir = None):
    # create the keys
    hCore = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, None)
    hSvt = winreg.CreateKeyEx(hCore, 'SOFTWARE\\Microsoft\\MSMQ\\SCAP_Validation_Tests\\win_reg\\',0, winreg.KEY_ALL_ACCESS)
    hExists = winreg.CreateKeyEx(hSvt, 'exists\\',0, winreg.KEY_ALL_ACCESS)
    # create the values
    winreg.SetValueEx(hExists, 'vBin', None, winreg.REG_BINARY, array.array('B', [128]))
    winreg.SetValueEx(hExists, 'vDword', None, winreg.REG_DWORD, -1)
    winreg.SetValueEx(hExists, 'vSZ', None, winreg.REG_SZ, 'this is a string')
    winreg.SetValueEx(hExists, 'vDwordLE', None, winreg.REG_DWORD_LITTLE_ENDIAN, -1)
    #winreg.SetValueEx(hExists, 'vDwordBE', None, winreg.REG_DWORD_BIG_ENDIAN, array.array('l', [-1]))
    winreg.SetValueEx(hExists, 'vExpandSz', None, winreg.REG_EXPAND_SZ, '%SYSTEMROOT%/temp')
    #winreg.SetValueEx(hExists, 'vLink', None, winreg.REG_LINK,  array.array('L', [1]))
    winreg.SetValueEx(hExists, 'vMultiSz', None, winreg.REG_MULTI_SZ, ['string1','string2','string3','string4'])
    winreg.SetValueEx(hExists, 'vNone', None, winreg.REG_NONE, array.array('B', [35]))
    

    # close the regostry keys
    winreg.CloseKey(hExists)
    winreg.CloseKey(hSvt)
    winreg.CloseKey(hCore)
    return

if __name__ == "__main__":
    performConfig()
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
import win32security
import ntsecuritycon as con
import winreg

def setObjectSecurity(obj, dacl):
    sd = win32security.GetSecurityInfo(obj, win32security.SE_REGISTRY_KEY, win32security.DACL_SECURITY_INFORMATION)
    #dacl = sd.GetSecurityDescriptorDacl()
    if dacl is None:
        dacl = win32security.ACL()
    win32security.SetSecurityInfo(obj, win32security.SE_REGISTRY_KEY, win32security.DACL_SECURITY_INFORMATION, None, None, dacl, None)
def performConfig(workingDir=None):
    # create the registry keys if necessary
    hCore = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, None)
    hSvt = winreg.CreateKeyEx(hCore, 'SOFTWARE\\Microsoft\\MSMQ\\SCAP_Validation_Tests\\win_rer53',0, winreg.KEY_ALL_ACCESS)
    hExists = winreg.CreateKeyEx(hSvt, 'exists\\',0, winreg.KEY_ALL_ACCESS)
    hPermissions = winreg.CreateKeyEx(hSvt, 'permissions\\',0, winreg.KEY_ALL_ACCESS)
    # find the sids for Administrators, System, Guest, Everyone
    adminSid, domain, type = win32security.LookupAccountName("","Administrators")
    systemSid, domain, type = win32security.LookupAccountName("","SYSTEM")
    guestSid,domain, type = win32security.LookupAccountName("","Guest")
    guestsSid,domain, type = win32security.LookupAccountName("","Guests")
    powerUsersSid,domain,type = win32security.LookupAccountName("","Power Users")

    #build the DACL
    rights = winreg.KEY_ALL_ACCESS | con.STANDARD_RIGHTS_ALL
    dacl1 = win32security.ACL()
    dacl1.AddAccessAllowedAce(win32security.ACL_REVISION, rights, adminSid)
    dacl1.AddAccessAllowedAce(win32security.ACL_REVISION, rights, systemSid)
    dacl1.AddAccessAllowedAce(win32security.ACL_REVISION, rights, guestSid)
    dacl1.AddAccessAllowedAce(win32security.ACL_REVISION, rights, guestsSid)
    dacl1.AddAccessDeniedAce(win32security.ACL_REVISION, rights, powerUsersSid)

    setObjectSecurity(hPermissions, dacl1)

    # close the regostry keys
    winreg.CloseKey(hPermissions)
    winreg.CloseKey(hExists)
    winreg.CloseKey(hSvt)
    winreg.CloseKey(hCore)
    return

if __name__ == "__main__":
    performConfig()
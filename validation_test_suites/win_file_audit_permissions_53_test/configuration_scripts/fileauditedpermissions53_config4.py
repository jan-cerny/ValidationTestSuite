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
import win32api
import win32con

def enablePrivileges(new_privs = None):
    if new_privs is None:
        new_privs = ((win32security.LookupPrivilegeValue('',win32security.SE_SECURITY_NAME),win32con.SE_PRIVILEGE_ENABLED),
                     (win32security.LookupPrivilegeValue('',win32security.SE_TCB_NAME),win32con.SE_PRIVILEGE_ENABLED),
                     (win32security.LookupPrivilegeValue('',win32security.SE_SHUTDOWN_NAME),win32con.SE_PRIVILEGE_ENABLED),
                     (win32security.LookupPrivilegeValue('',win32security.SE_RESTORE_NAME),win32con.SE_PRIVILEGE_ENABLED),
                     (win32security.LookupPrivilegeValue('',win32security.SE_TAKE_OWNERSHIP_NAME),win32con.SE_PRIVILEGE_ENABLED),
                     (win32security.LookupPrivilegeValue('',win32security.SE_CREATE_PERMANENT_NAME),win32con.SE_PRIVILEGE_ENABLED),
                     (win32security.LookupPrivilegeValue('',win32security.SE_ENABLE_DELEGATION_NAME),win32con.SE_PRIVILEGE_ENABLED),
                     (win32security.LookupPrivilegeValue('',win32security.SE_CHANGE_NOTIFY_NAME),win32con.SE_PRIVILEGE_ENABLED),
                     (win32security.LookupPrivilegeValue('',win32security.SE_DEBUG_NAME),win32con.SE_PRIVILEGE_ENABLED),
                     (win32security.LookupPrivilegeValue('',win32security.SE_PROF_SINGLE_PROCESS_NAME),win32con.SE_PRIVILEGE_ENABLED),
                     (win32security.LookupPrivilegeValue('',win32security.SE_SYSTEM_PROFILE_NAME),win32con.SE_PRIVILEGE_ENABLED),
                     (win32security.LookupPrivilegeValue('',win32security.SE_LOCK_MEMORY_NAME),win32con.SE_PRIVILEGE_ENABLED),
                     (win32security.LookupPrivilegeValue('',win32security.SE_AUDIT_NAME), win32con.SE_PRIVILEGE_ENABLED)
            )
    ph = win32api.GetCurrentProcess()
    th = win32security.OpenProcessToken(ph,win32security.TOKEN_ALL_ACCESS)
    return win32security.AdjustTokenPrivileges(th,0,new_privs)
def setSacl(filename, sacl):
    old_privs = enablePrivileges()
    sd = win32security.GetFileSecurity(filename, win32security.SACL_SECURITY_INFORMATION)
    sd.SetSecurityDescriptorSacl(1,sacl,1)
    win32security.SetFileSecurity(filename, win32security.SACL_SECURITY_INFORMATION, sd)
    enablePrivileges(new_privs=old_privs)
    return
def performConfig(workingDir = None):
    print('Beginning Configuration ...')
    file1 = r'\scap_validation_content\win_fap53\permissions\1.txt'
    file2 = r'\scap_validation_content\win_fap53\permissions\2.txt'

    # check for existence of files and create if necessary
    if not os.path.exists(r'\scap_validation_content'):
        os.mkdir(r'\scap_validation_content')
    if not os.path.exists(r'\scap_validation_content\win_fap53'):
        os.mkdir(r'\scap_validation_content\win_fap53')
    if not os.path.exists(r'\scap_validation_content\win_fap53\permissions'):
        os.mkdir(r'\scap_validation_content\win_fap53\permissions')
    if not os.path.exists(file1):
        open(file1, "w").close()
    if not os.path.exists(file2):
        open(file2, "w").close()

    # find the sids for Administrators, System, Guest, Everyone
    adminSid, domain, type = win32security.LookupAccountName("","Administrators")
    systemSid, domain, type = win32security.LookupAccountName("","SYSTEM")
    guestSid,domain, type = win32security.LookupAccountName("","Guest")
    guestsSid,domain, type = win32security.LookupAccountName("","Guests")

    # set file auditing
    sacl1 = win32security.ACL()
    sacl1.AddAuditAccessAce(win32security.ACL_REVISION, con.GENERIC_ALL | con.ACCESS_SYSTEM_SECURITY,adminSid, 1, 1)
    sacl1.AddAuditAccessAce(win32security.ACL_REVISION, con.GENERIC_ALL | con.ACCESS_SYSTEM_SECURITY,guestsSid, 1, 1)
    setSacl(file1, sacl1)

    # set auditing on the directory
    sacl2 = win32security.ACL()
    sacl2.AddAuditAccessAce(win32security.ACL_REVISION, con.GENERIC_ALL, adminSid, 1,1)
    sacl2.AddAuditAccessAce(win32security.ACL_REVISION, con.GENERIC_ALL, systemSid, 1,1)
    setSacl(r'\scap_validation_content\win_fap53\permissions', sacl2)
    print('Configuration Complete...')
if __name__ == "__main__":
    performConfig()
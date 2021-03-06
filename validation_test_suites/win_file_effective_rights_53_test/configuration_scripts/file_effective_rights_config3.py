__author__ = 'matt.kerr'

import os
import win32security
import ntsecuritycon as con


def setAcl(filename, dacl):
    sd = win32security.GetFileSecurity(filename, win32security.DACL_SECURITY_INFORMATION)
    sd.SetSecurityDescriptorDacl(1,dacl,0)
    win32security.SetFileSecurity(filename, win32security.DACL_SECURITY_INFORMATION, sd)
    return

def performConfig(workingDir=None):
    file1 = r'\scap_validation_content\win_fer53\e\1.txt'
    file2 = r'\scap_validation_content\win_fer53\e\2.txt'
    
    # check for existence of files and create if necessary
    if not os.path.exists(r'\scap_validation_content'):
        os.mkdir(r'\scap_validation_content')
    if not os.path.exists(r'\scap_validation_content\win_fer53'):
        os.mkdir(r'\scap_validation_content\win_fer53')
    if not os.path.exists(r'\scap_validation_content\win_fer53\e'):
        os.mkdir(r'\scap_validation_content\win_fer53\e')
    if not os.path.exists(file1):
        open(file1, "w").close()
    if not os.path.exists(file2):
        open(file2, "w").close()
    
    # find the sids for Administrators, System, Guest, Everyone
    adminSid, domain, type = win32security.LookupAccountName("","Administrators")
    systemSid, domain, type = win32security.LookupAccountName("","SYSTEM")
    guestSid,domain, type = win32security.LookupAccountName("","Guest")
    everyoneSid, domain, type = win32security.LookupAccountName("","Everyone")
    
    dacl1 = win32security.ACL()
    dacl1.AddAccessDeniedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS | con.ACCESS_SYSTEM_SECURITY | con.GENERIC_ALL, guestSid)
    dacl1.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS | con.ACCESS_SYSTEM_SECURITY | con.GENERIC_ALL, adminSid)
    dacl1.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS | con.ACCESS_SYSTEM_SECURITY | con.GENERIC_ALL, systemSid)
    dacl1.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS | con.ACCESS_SYSTEM_SECURITY | con.GENERIC_ALL, everyoneSid)
    
    setAcl(file1, dacl1)
    setAcl(file2, dacl1)
    return

if __name__ == "__main__":
    performConfig()






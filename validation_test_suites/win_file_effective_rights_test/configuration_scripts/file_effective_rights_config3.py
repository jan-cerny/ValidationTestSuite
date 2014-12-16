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
    file1 = r'C:\scap_validation_content\win_fer\e\1.txt'
    file2 = r'C:\scap_validation_content\win_fer\e\2.txt'
    
    # check for existence of files and create if necessary
    if not os.path.exists(r'\scap_validation_content'):
        os.mkdir(r'\scap_validation_content')
    if not os.path.exists(r'C:\scap_validation_content\win_fer'):
        os.mkdir(r'C:\scap_validation_content\win_fer')
    if not os.path.exists(r'C:\scap_validation_content\win_fer\e'):
        os.mkdir(r'C:\scap_validation_content\win_fer\e')
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
    dacl1.AddAccessDeniedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, guestSid)
    dacl1.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, adminSid)
    dacl1.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, systemSid)
    dacl1.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, everyoneSid)
    
    setAcl(file1, dacl1)
    setAcl(file2, dacl1)
    return

if __name__ == "__main__":
    performConfig()






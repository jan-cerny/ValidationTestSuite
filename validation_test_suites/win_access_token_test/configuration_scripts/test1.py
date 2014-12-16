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

lsaPolicy = win32security.LsaOpenPolicy('',win32security.POLICY_LOOKUP_NAMES | win32security.POLICY_VIEW_LOCAL_INFORMATION)
accts = win32security.LsaEnumerateAccountsWithUserRight(lsaPolicy, win32security.SE_AUDIT_NAME)
for acct in accts:
    print(win32security.LookupAccountSid(None, acct))
win32security.LsaClose(lsaPolicy)
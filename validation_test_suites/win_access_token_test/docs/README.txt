Content analysis complete

Testing Status
	Complete

Known Issues
	None
	
Additional Information	
	The following privileges are not defined on XP (see http://msdn.microsoft.com/en-us/library/windows/desktop/ee695867%28v=vs.85%29.aspx):
		- SeCreateSymbolicLinkPrivilege
		- SeIncreaseWorkingSetPrivilege
		- SereLabelPrivilege
		- SeTimezonePrivilege
		- SeTrustedCredManAccessPrivilege (setrustedcredmanaccessnameright in OVAL)
	
	The following XCCDF rules will return "notapplicable" on Windows XP:
		- xccdf_gov.nist_rule_secreatesymboliclinkprivilege-with-equals-operation-8
		- xccdf_gov.nist_rule_seincreaseworkingsetprivilege-with-equals-operation-15
		- xccdf_gov.nist_rule_serelabelprivilege-with-equals-operation-21
		- xccdf_gov.nist_rule_setimezoneprivilege-with-equals-operation-32
		- xccdf_gov.nist_rule_setrustedcredmanaccessnameright-with-equals-operation-45
		- xccdfgov.nist_rule_secreatesymboliclinkprivilege-with-equals-operation-143
		- xccdfgov.nist_rule_secreatesymboliclinkprivilege-with-equals-operation-98
		- xccdfgov.nist_rule_secreatesymboliclinkprivilege-with-equals-operation-53
		- xccdfgov.nist_rule_seincreaseworkingsetprivilege-with-equals-operation-150
		- xccdfgov.nist_rule_seincreaseworkingsetprivilege-with-equals-operation-60
		- xccdfgov.nist_rule_seincreaseworkingsetprivilege-with-equals-operation-105
		- xccdfgov.nist_rule_serelabelprivilege-with-equals-operation-156
		- xccdfgov.nist_rule_serelabelprivilege-with-equals-operation-66
		- xccdfgov.nist_rule_serelabelprivilege-with-equals-operation-111
		- xccdfgov.nist_rule_setimezoneprivilege-with-equals-operation-122
		- xccdfgov.nist_rule_setimezoneprivilege-with-equals-operation-77
		- xccdfgov.nist_rule_setimezoneprivilege-with-equals-operation-167
		- xccdfgov.nist_rule_setrustedcredmanaccessnameright-with-equals-operation-180
		- xccdfgov.nist_rule_setrustedcredmanaccessnameright-with-equals-operation-135
		- xccdfgov.nist_rule_setrustedcredmanaccessnameright-with-equals-operation-90	
	
	
Catalog.xml	
	suiteId="G2.access_token_tests_xp_config_1" - expected results for Windows XP
	suiteId="G2.access_token_tests_xp_config_2" - expected results for Windows XP
	suiteId="G2.access_token_tests_config_1" - expected results for Windows Vista and 7
	suiteId="G2.access_token_tests_config_2" - expected results for Windows Vista and 7

Scripts
	None

Configuration Instructions
	Configuration 1 - secedit.exe /configure /db test /cfg user_rightspolicy_config_1.inf /overwrite /quiet
	Configuration 2 - secedit.exe /configure /db test /cfg user_rightspolicy_config_2.inf /overwrite /quiet

Cleanup Instructions 
	secedit.exe /configure /db test /cfg Win7-BaseInstall.inf /overwrite /quiet
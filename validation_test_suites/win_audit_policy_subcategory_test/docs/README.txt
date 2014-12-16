Content Status
	Complete

Testing Status
	Complete

Known Issues
	None

Additional Information	
	1. The audit policy subcategories are available only in Windows Vista and later.
	   For more information please see the "Expanded Auditing Policy in Windows Vista and Windows Server 2008"
	   section (http://technet.microsoft.com/en-us/library/cc766468(v=ws.10).aspx).
		
	2. According to Microsoft documentation (http://support.microsoft.com/kb/947226) the audit subcategory 
	   "Detailed File Share" is not available on Windows Vista.
	   The following rules will return "notapplicable" on Windows Vista:
		   xccdf_gov.nist_rule_detailed-file-share-with-equals-operation-101
		   xccdf_gov.nist_rule_detailed-file-share-with-equals-operation-102
		   xccdf_gov.nist_rule_detailed-file-share-with-equals-operation-103
		   xccdf_gov.nist_rule_detailed-file-share-with-equals-operation-104
	   
Catalog.xml	
	suiteId="G2.audit_policy_subcategory_tests_wvista_config_1" - expected results for Windows Vista
	suiteId="G2.audit_policy_subcategory_tests_wvista_config_2" - expected results for Windows Vista
	suiteId="G2.audit_policy_subcategory_tests_wvista_config_3" - expected results for Windows Vista
	suiteId="G2.audit_policy_subcategory_tests_wvista_config_4" - expected results for Windows Vista

	suiteId="G2.audit_policy_subcategory_tests_w7_config_1" - expected results for Windows 7
	suiteId="G2.audit_policy_subcategory_tests_w7_config_2" - expected results for Windows 7
	suiteId="G2.audit_policy_subcategory_tests_w7_config_3" - expected results for Windows 7
	suiteId="G2.audit_policy_subcategory_tests_w7_config_4" - expected results for Windows 7
	   
Scripts
	auditeventsubcategoriespolicy_config_1.bat
	auditeventsubcategoriespolicy_config_2.bat
	auditeventsubcategoriespolicy_config_3.bat
	auditeventsubcategoriespolicy_config_4.bat

Configuration Instructions
	Configuration 1 - auditeventsubcategoriespolicy_config_1.bat
	Configuration 2 - auditeventsubcategoriespolicy_config_2.bat
	Configuration 3 - auditeventsubcategoriespolicy_config_3.bat
	Configuration 4 - auditeventsubcategoriespolicy_config_4.bat

Cleanup Instructions 
	None

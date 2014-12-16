This content covers the SCAP.R.2000.5 and it runs on Windows with IE and Red
Hat Enterprise Linux systems.

Instructions:	Follow the required Test Procedure described in SCAP.R.2000.5 
				section.

Files:
	For Windows:
		R2000-5-win-datastream.xml
			
	For RHEL:
		R2000-5-rhel-datastream.xml

Expected results:
	For Windows:
		xccdf_gov.nist_rule_rhel.validation_R2000.5_rule_1 - PASS
		xccdf_gov.nist_rule_rhel.validation_R2000.5_rule_2 - FAIL
			
	For RHEL:
		xccdf_gov.nist_rule_xccdf_gov.nist.validation_R2000.5_rule_1 - PASS
		xccdf_gov.nist_rule_xccdf_gov.nist.validation_R2000.5_rule_2 - FAIL		
	
Testing Status
The content has not been fully test it.

Known Issues
None

Scripts
None

Configuration Instructions
None

Cleanup Instructions 
None

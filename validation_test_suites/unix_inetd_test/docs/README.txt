STATUS
Testing complete. 

KNOWN ISSUES
None.

REQUIREMENTS
- this test requires inetd to be installed.
Note:	The inetd is not shipped with RHEL products and the inetd_test should be evaluated to “not applicable” on RHEL.
		Please see http://making-security-measurable.1364806.n2.nabble.com/inetd-test-td5432225.html#a5432245 

OVERVIEW OF SCRIPTS
inetd_config_script - TODO

inetd_cleanup_script - TODO

CONFIGURE SYSTEM
1.  Make sure inetd is installed on the system.
2.	Run chmod +x inetd_config_script 
3.	./inetd_config_script

CLEAN UP SYSTEM
1.	Run chmod +x inetd_cleanup_script
2.	./inetd_cleanup_script


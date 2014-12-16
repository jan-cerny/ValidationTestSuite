Content Status
	Complete

Testing Status
	Complete

Known Issues
	None

Scripts
	linux_file_hash_test_config_1.py - establishes configuration 1 on the system
	linux_file_hash_test_config_2.py - established configuration 2 on the system
	linux_file_hash_test_cleanup.py - cleans up the changes made by configuration scripts.

Configuration Instructions
	Configuration 1 - run linux_file_hash_test_config_1.py
	Configuration 2 - run linux_file_hash_test_config_2.py

Cleanup Instructions 
	run linux_file_hash_test_cleanup.py

Scanning instructions for the discrete data stream
	The ind_file_hash_test-datastream.xml data stream includes two profiles:
		"xccdf_gov.nist.validation.filehash_profile_filehash"
		"xccdf_gov.nist.validation.filehash_profile_filehash2"
	The first profile applies to Configuration 1 and the second profile applies to Configuration 2.
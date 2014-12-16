Content Status
	Complete

Testing Status
	Complete

Known Issues
	- Tests 31m 33m 36m and 39 had to be de-selected until dynamic content generation is possible.
	- The current version of ovaldi collects free blocks avail to non-superuser (f_bavail) instead
	  free blocks in file system (f_bfree). Affected tests: oval:nist.validation.linuxPartition:tst:95,
	  98, 99, 100, and 102.

Scripts
	Configuration 1: linux_partition_test_config1.sh

Configuration Instructions
	Note: the /tmp must be created as separate partition and not as a folder on the root partition.

Cleanup Instructions
	Configuration 1: linux_partition_test_cleanup.sh

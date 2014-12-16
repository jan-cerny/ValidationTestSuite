This content covers the SCAP.R.1900 and it runs on Windows with IE and Red Hat Enterprise Linux systems.

Instructions: Follow the required Test Procedure described in SCAP.R.1900 section.
  How to use the content:
	- Import the OVAL definitions and external variables files into to the product
	- Perform configuration scans for the Windows and\or RHEL target systems
	- Compare the produced results with the expected results listed bellow

Files:
1. OVAL only files
	For Windows:
		win-R1900-oval.xml
			oval:nist.validation.r1900:def:1 | class="vulnerability" | expected_result = TRUE
			oval:nist.validation.r1900:def:2 | class="vulnerability" | expected_result = FALSE
			oval:nist.validation.r1900:def:3 | class="vulnerability" | expected_result = ERROR
			
	For RHEL:
		rhel-R1900-oval.xml
			oval:nist.validation.r1900-rhel:def:1 | class="vulnerability" | expected_result = TRUE
			oval:nist.validation.r1900-rhel:def:2 | class="vulnerability" | expected_result = FALSE
			oval:nist.validation.r1900-rhel:def:3 | class="vulnerability" | expected_result = ERROR
			
2. OVAL only files with external variable
	For Windows:
		win-R1900-ext-var-oval.xml
			oval:nist.validation.r1900:def:4 | class="vulnerability" | expected_result = TRUE
		win-R1900-ext-var-variables.xml
			oval:nist.validation.r1900:var:2 | values: 1.1.1.1, 2.2.2.2, 3.3.3.3
		
	For RHEL:		
		rhel-R1900-ext-var-oval.xml
			oval:nist.validation.r1900-rhel:def:4 | class="vulnerability" | expected_result = TRUE
		rhel-R1900-ext-var-variables.xml
			oval:nist.validation.r1900-rhel:var:2 | values: 0:3Desktop-13.9.7, 0:3WS-13.9.7, 0:3ES-13.9.7
			
Content analysis complete

Testing Status
Complete

Known Issues
None

Scripts
None

Configuration Instructions
None

Cleanup Instructions 
None

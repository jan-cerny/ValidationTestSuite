SCAP 1.2 Public Validation Test Suite

Overview --
The validation test suite is composed of several components.
  - SCAP 1.2 content
  - Corresponding spreadsheet showing required test system configuration and expected results
  - Configuration scripts (optional)
  - Validation files – the SCAPVal results
The use of the data streams and the corresponding spreadsheet information are required. Use of the configuration scripts are optional and are provided for convenience.

SCAP 1.2 Content --
The SCAP 1.2 validation content is designed to exercise SCAP capabilities rather than testing for specific returned values as is the case with a checklist.  For example, instead of testing if the product correctly detects when a system has a minimum password length requirement configured to a value greater than 14 characters, the SCAP 1.2 validation content tests all possible values and operators associated with checking password length.  The intent of the new validation content is ensuring SCAP validated products are capable of processing all well-formed SCAP content.

The validation content is organized in sub-directories around specific OVAL test types. Each sub-directory contains an SCAP 1.2 data stream, spreadsheet, and optional configuration scripts. The SCAP 1.2 data streams are in the new SCAP 1.2 combined data stream file format. These files use the following naming convention:

	Optional_prefix-datastream.xml

The optional_prefix portion of the filename may vary, but the data stream file will always end with “datastream.xml”.

Content Spreadsheet (test system configurations and expected results) --
The spreadsheet associated with each data stream provides the required test system configurations and the expected results for the data stream. Each spreadsheet has two pages. The first identifies the expected results for each rule in the data stream. Each rule has an id number that corresponds with the rule id in the data stream. The spreadsheet shows the expected results for each rule.

The second page identifies the required configurations that must be used when using the data streams on a test system. The configuration page consists of a group of configurations and the associated value for each configuration. Test systems must be configured according to the spreadsheet; else the results of a scan using the data streams will not match the expected results. If the configurations page is blank or missing, then no special configuration is required for testing the data stream and the data stream may be tested on a default system installation.

Configuration Scripts --
The validation test suite includes configuration scripts for automating the configuration of test systems according to the configurations defined in the spreadsheets. Use of these scripts is optional and there is no support associated with these scripts. They are provided as a courtesy. Test systems may be manually configured according to the prescribed configurations defined in the spreadsheets.

The configuration scripts may be in the following forms:
  - Python script
  - Executable file
  - System batch file
  - Inf file for use with secedit.exe

The python scripts require Python 2.7, Python 3.2 and the Python extensions for Windows. The python runtime and interpreter are available at http://www.python.org . The python extensions for Windows are available at http://python.net/crew/mhammond/win32/ . The executable files are either standard system utilities or custom programs developed as part of the validation content creation process.
Regardless of the configuration method chosen, users should verify the configuration of the test system matches the configuration defined in the spreadsheet.

Testing Process --
The testing process includes configuring the test system, scan with the product under test using the data stream, and ensure the results match the expected results. A default installation of test systems is an acceptable starting configuration for the SCAP 1.2 validation content because each data stream requires a specific configuration.

In general, the test procedure listed below should be followed.
  - Configure the test system according to the applicable configuration defined in the spreadsheet.
  - Import the data stream into the product under test.
  - Scan the test system.
  - Ensure the results match the expected results.
  - If there is not a match, troubleshoot the mis-match. 
      - Verify test system configuration
      - Verify the tool correctly processes the content
      - Run reference implementation tool and verify result matches expected result
      - Check for content errors

The content has been tested with reference implementation tools using the process previously listed. Vendor tools under test should yield the same result as the reference implementation tools.

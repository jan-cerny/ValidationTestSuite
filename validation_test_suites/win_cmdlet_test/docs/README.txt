Content analysis complete.

Content Status
Complete

Testing Status
Complete

Known Issues
Question about tests 4 and 119 and what the proper result should be for a test invoking a cmdlet that does not exist. Should it result in a fail or in an error?
- Unselected tests: 4, 119 - see question above
- Unselected tests: 6, 8, 10 - unable to get expected result
- Unselected tests: 31-40 - unable to identify a valid module id value

Scripts
None

Configuration Instructions
First open a powershell window with admin privileges
at the command line, create an alias based on the version of windows you are using (x86 or x64)
for x86:
new-alias installutil %Windir%\Microsoft.NET\Framework\v2.0.50727\installutil.exe
for x64:
new-alias installutil %Windir%\Microsoft.NET\Framework64\v2.0.50727\installutil.exe

Then run the following command:
installutil GetValTest.dll

Once this completes, verify that it shows up in the registered snap ins by running:

get-PSSnapin -reg *val*

You should see:
Name        : GetValTestCmdLets
PSVersion   : 2.0
Description : A cmdlet for use in NIST SCAP Validation Testing

To run the cmdlet from the command line perform the following steps.
add-PSSnapIn GetValTestCmdLets
get-valtest -testid 1

Cleanup Instructions 
None
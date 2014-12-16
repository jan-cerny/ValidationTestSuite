Content analysis complete.

Content Status
	Complete

Testing Status
	Complete

Known Issues
	Question about tests 4 and 119 and what the proper result should be for a test invoking a cmdlet that does not exist.
	Should it result in a fail or in an error?
	- Unselected tests: 4, 119 - see question above
	- Unselected tests: 6, 8, 10 - unable to get expected result
	- Unselected tests: 31-40 - unable to identify a valid module id value

	Unselected the following rules: xccdf_gov.nist.validation.winCmdlet_rule_13 and	xccdf_gov.nist.validation.winCmdlet_rule_18 - The OVAL specification
	does not clearly specify how to process the entity_check="none exist".
	(http://making-security-measurable.1364806.n2.nabble.com/OVAL-state-evaluation-with-entity-check-quot-none-exist-quot-tc7580011.html)

Scripts
	None

Configuration Instructions
	1. Copy GetValTest.dll to c:\Windows\System32\
	   (the GetValTest.dll is located in the ..\win_cmdlet_test\configuration_scripts\ folder)
	   
	2. Start Windows PowerShell running as Administrator
	   (click Start, point to Programs, point to Windows PowerShell, right-click Windows PowerShell, and then click Run as administrator)
	
	3. Create an alias based on the version of windows you are using (x86 or x64). At the Windows PowerShell prompt type:
		for x86:
			new-alias installutil C:\Windows\Microsoft.NET\Framework\v2.0.50727\installutil.exe

		for x64:
			new-alias installutil C:\Windows\Microsoft.NET\Framework64\v2.0.50727\installutil.exe
			
	4. At the Windows PowerShell prompt, type the following commands, and then press ENTER after each command:
		installutil .\GetValTest.dll
		Test-path $env:windir\System32\WindowsPowerShell\v1.0\profile.ps1
		
	5. If the results of the previous command are false, go to step 6. If the results are true, go to step 7.

	6. Type the following command, and then press ENTER:
		new-item -path $env:windir\System32\WindowsPowerShell\v1.0\profile.ps1 -itemtype file -force
	
	7. Type the following command, and then press ENTER:
		Notepad $env:windir\System32\WindowsPowerShell\v1.0\profile.ps1

	8. In the profile, type Add-PSSnapIn GetValTestCmdLets. If you are adding this command to an existing profile, add it on a new line at the end of the profile.

	9. On the menu bar, click File, and then click Exit.
	
	10.In Notepad, click Save.
	
	11.Type the following commands, and then press ENTER after each command:
		Set-ExecutionPolicy RemoteSigned
		. $env:windir\System32\WindowsPowerShell\v1.0\profile.ps1
	
	12.Verify that the cmdlet shows up in the registered snap-ins by running:
		get-PSSnapin -reg *val*
			The output should look like:
				Name        : GetValTestCmdLets
				PSVersion   : 2.0
				Description : A cmdlet for use in NIST SCAP Validation Testing

		get-valtest -testid 1
			The output should look like:
				Apple
				Bananna
		
Cleanup Instructions 
	1. Start Windows PowerShell running as Administrator
	
	2. At the Windows PowerShell prompt, type the following commands, and then press ENTER after each command:
		Remove-PSSnapin GetValTestCmdLets
		Notepad $env:windir\System32\WindowsPowerShell\v1.0\profile.ps1	
	   Delete the line: Add-PSSnapIn GetValTestCmdLets
	   
	3. On the menu bar, click File, and then click Exit.
	
	4. In Notepad, click Save.
	
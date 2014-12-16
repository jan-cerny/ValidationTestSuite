Content analysis
Complete

Testing Status
Complete

Known Issues
None

Scripts
lockout-policy_set.exe

Configuration Instructions
Configuration 1 - secedit.exe /configure /db test /cfg passwordpolicy_config_1.inf /overwrite /quiet
Configuration 2 - secedit.exe /configure /db test /cfg passwordpolicy_config_2.inf /overwrite /quiet
Configuration 3
	32-bit systems:
		lockout_policy_set32.exe  min_age:2332800 min_length:14 max_age:TIMEQ_FOREVER history_length:24
	64-bit systems:
		lockout_policy_set.exe min_age:2332800 min_length:14 max_age:TIMEQ_FOREVER history_length:24
	Windows XP systems:
		lockout_policy_setxp.exe  min_age:2332800 min_length:14 max_age:TIMEQ_FOREVER history_length:24

Cleanup Instructions 
secedit.exe /configure /db test /cfg Win7-BaseInstall.inf /overwrite /quiet
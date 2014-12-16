Content Status
Complete

Testing Status
Complete

Known Issues
None

Scripts
lockout_policy_set.exe
lockout_policy_set32.exe
lockout_policy_setxp.exe

Configuration Instructions
32-bit systems:
Configuration 1 - lockout_policy_set32.exe force_logoff:0 lockout_duration:-1 observation_window:-1 threshold:0
Configuration 2 - lockout_policy_set32.exe force_logoff:3600 lockout_duration:120 observation_window:120 threshold:10
Configuration 3 - lockout_policy_set32.exe force_logoff:TIMEQ_FOREVER lockout_duration:13 observation_window:13 threshold:50

64-bit systems:
Configuration 1 - lockout_policy_set.exe force_logoff:0 lockout_duration:-1 observation_window:-1 threshold:0
Configuration 2 - lockout_policy_set.exe force_logoff:3600 lockout_duration:120 observation_window:120 threshold:10
Configuration 3 - lockout_policy_set.exe force_logoff:TIMEQ_FOREVER lockout_duration:13 observation_window:13 threshold:50

Windows XP systems:
Configuration 1 - lockout_policy_setxp.exe force_logoff:0 lockout_duration:-1 observation_window:-1 threshold:0
Configuration 2 - lockout_policy_setxp.exe force_logoff:3600 lockout_duration:120 observation_window:120 threshold:10
Configuration 3 - lockout_policy_setxp.exe force_logoff:TIMEQ_FOREVER lockout_duration:13 observation_window:13 threshold:50


Cleanup Instructions 
secedit.exe /configure /db test /cfg Win7-BaseInstall.inf /overwrite /quiet
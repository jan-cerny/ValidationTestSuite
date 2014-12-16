Content Analysis Complete.

Content Status
Complete
 
Testing Status
Complete

Known Issues
None

Scripts
None

Configuration Instructions
Configuration 1 - secedit.exe /configure /db test /cfg auditeventpolicy_config_1.inf /overwrite /quiet
Configuration 2 - secedit.exe /configure /db test /cfg auditeventpolicy_config_2.inf /overwrite /quiet
Configuration 3 - secedit.exe /configure /db test /cfg auditeventpolicy_config_3.inf /overwrite /quiet
Configuration 4 - secedit.exe /configure /db test /cfg auditeventpolicy_config_4.inf /overwrite /quiet

Cleanup Instructions 
secedit.exe /configure /db test /cfg Win7-BaseInstall.inf /overwrite /quiet
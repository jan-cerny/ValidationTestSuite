Content analysis complete.  Test 24 fails, OVALDI appears not to retrieve permissions on HKEY_CURRENT_CONFIG.

Content Status
Complete 

Testing Status
Complete

Known Issues
OVALDI does not retrieve permission from HKEY_CIRRENT_CONFIG, test 24 not validated.

Scripts
win_regkeyeffectiverights_config1.py
win_regkeyeffectiverights_config2.py
win_regkeyeffectiverights_cleanup1.py

Configuration Instructions
Configuration 1 - Run win_regkeyeffectiverights_config1.py
Configuration 2 - Run win_regkeyeffectiverights_config2.py

Cleanup Instructions 
Run win_regkeyeffectiverights_cleanup1.py
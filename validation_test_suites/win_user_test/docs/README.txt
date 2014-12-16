Content analysis
Complete

Content Status
Complete

Testing Status
Complete

Known Issues
Tests 38-43 are potential issues since retrieval of last logon time does not occur.
Retrieval of last logon time in a domain environment is problematic in most cases.
The corresponding rules are not included in the benchmark.

Scripts
win_user_test_config1.py
win_user_test_config2.py
win_user_test_cleanup.py

Configuration Instructions
Manual Configuration: The computer name must be "TESTMACHINE" or "TESTMACHINE"[01-99]".
Configuration 1 - Run win_user_test_config1.py
Configuration 2 - Run win_user_test_config2.py

Cleanup Instructions 
Run win_user_test_cleanup.py
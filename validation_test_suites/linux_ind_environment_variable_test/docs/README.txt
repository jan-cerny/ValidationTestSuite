Content Status
Complete

Testing Status
Complete

Known Issues
None

Scripts
linux-ind_environment_variable_test-config1.sh

Configuration Instructions
Ensure that the "temp" environment variable exists and is set with a non-empty string.
Ensure that the "HISTSIZE" environment variable exists and is set 1000.

Run the script as root in the current shell context (using the "." or source)
otherwise you'll need to logout and login back for the environment settings to
be configured.
i.e.: 
#  . linux-ind_environment_variable_test-config1.sh
or
# source linux-ind_environment_variable_test-config1.sh

Cleanup Instructions 
None

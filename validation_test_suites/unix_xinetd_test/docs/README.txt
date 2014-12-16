STATUS
Testing complete. 

KNOWN ISSUES
none

OVERVIEW OF SCRIPTS
xinetd_config_script - this script first checks for the existence of the /etc/xinetd.d.
If it does not exist it exits.  Otherwise, it will changes the names of existing 
configuration files in /etc/xinetd.d to <file>.valbak.  Adding a "." to the file name
will cause xinetd to not consider it.  Then a copy of the validation services (echo,
ftp, and netstat) will be copied to /etc/xinetd.d.

xinetd_cleanup_script - this script first checks for the existence of the /etc/xinetd.d.
If it does not exist it exits.  Otherwise, it removes the validation services (echo, 
ftp, and netstat) that were added by the configuration script.  It then renames the existing
services so that it no longer includes ".valbak" and xinetd will consider them again.

CONFIGURE SYSTEM
1.  Make sure xinetd is installed on the system.
2.	Run chmod +x xinetd_config_script.sh
3.	./xinetd_config_script.sh

CLEAN UP SYSTEM
1.	Run chmod +x xinetd_cleanup_script.sh
2.	./xinetd_cleanup_script.sh


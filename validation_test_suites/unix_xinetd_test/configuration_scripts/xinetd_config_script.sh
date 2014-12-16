#!/bin/bash

#Make sure /etc/xinetd.d exists before proceeding
if [ ! -e "/etc/xinetd.d" ]
then
    echo "/etc/xinetd.d does not exist - does xinetd need to be installed?"
    exit
fi

#Backup existing files - xinetd ignores files with a "." in their name according to xinetd.conf man page which states:
#"Takes a directory name in the form of "includedir /etc/xinetd.d". Every file inside that directory, excluding 
#files with names containing a dot ('.') or ending with a tilde ('~'), will be parsed as xinetd configuration files..." 
FILES=/etc/xinetd.d/*
for f in $FILES
do
  mv $f "$f.valbak"
done

#Copy the validation configuration files to /etc/xinetd.d for testing
cp echo /etc/xinetd.d
cp ftp /etc/xinetd.d
cp netstat /etc/xinetd.d

dos2unix /etc/xinetd.d/echo
dos2unix /etc/xinetd.d/ftp
dos2unix /etc/xinetd.d/netstat

exit
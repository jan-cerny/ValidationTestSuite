#!/bin/bash

#Make sure /etc/xinetd.d exists before proceeding
if [ ! -e "/etc/xinetd.d" ]
then
    echo "/etc/xinetd.d does not exist - does xinetd need to be installed?"
    exit
fi

#Remove validation configuration files
rm -f /etc/xinetd.d/echo
rm -f /etc/xinetd.d/ftp
rm -f /etc/xinetd.d/netstat

#Restore files that were backed up
FILES=/etc/xinetd.d/*.valbak
for f in $FILES
do
  mv $f ${f%%".valbak"}
done

exit
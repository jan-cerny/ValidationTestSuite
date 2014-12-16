#!/bin/bash

#unset TEMP
if [ -n "${TEMP+x}" ]; then
	echo TEMP is set
else
	echo TEMP is not set
	echo "export TEMP=/tmp" >> /etc/profile
	source /etc/profile
fi

if [ -n "${TEMP+x}" ]; then
	echo TEMP was set correctly
else
	echo ERROR: TEMP was not set
fi

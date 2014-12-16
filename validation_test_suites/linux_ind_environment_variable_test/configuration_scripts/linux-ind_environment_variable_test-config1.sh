#!/bin/bash

#unset temp
if [ -n "${temp+x}" ]; then
	echo temp is set
else
	echo temp is not set
	echo "export temp=/tmp" >> /etc/profile
	source /etc/profile
fi

if [ -n "${temp+x}" ]; then
	echo temp was set correctly
else
	echo ERROR: temp was not set
fi

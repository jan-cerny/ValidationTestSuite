#!/bin/bash

if egrep -q "^export TEMP=\/tmp$" /etc/profile; then
	echo "The TEMP variable is defined in the /etc/profile"
	echo "I'll remove it..."
	sed -i".bak" '/^export TEMP=\/tmp$/d' /etc/profile
	unset TEMP
fi

if egrep -q "^export TEMP" /etc/bashrc; then
	echo "The TEMP variable is defined in the /etc/bashrc"
	echo "Nothing to do here..."
else
	echo "TEMP is not set in /etc/bashrc"
	echo "Configuring the environment variable"
	echo "export TEMP=/tmp" >> /etc/bashrc
	source /etc/bashrc
fi

if [ -n "${TEMP+x}" ]; then
	echo "TEMP was set correctly"
else
	echo "ERROR: TEMP was not set"
fi

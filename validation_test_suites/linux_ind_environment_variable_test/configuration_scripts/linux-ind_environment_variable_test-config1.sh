#!/bin/bash

if egrep -q "^export temp=\/tmp$" /etc/profile; then
	echo "The temp variable is defined in the /etc/profile"
	echo "I'll remove it..."
	sed -i".bak" '/^export temp=\/tmp$/d' /etc/profile
	unset temp
fi

if egrep -q "^export temp" /etc/bashrc; then
	echo "The temp variable is defined in the /etc/bashrc"
	echo "Nothing to do here..."
else
	echo "temp is not set in /etc/bashrc"
	echo "Configuring the environment variable"
	echo "export temp=/tmp" >> /etc/bashrc
	source /etc/bashrc
fi

if [ -n "${temp+x}" ]; then
	echo "temp was set correctly"
else
	echo "ERROR: temp was not set"
fi

if egrep -q "^export HISTSIZE" /etc/bashrc; then
	echo "The HISTSIZE variable is defined in the /etc/bashrc"
	echo "Nothing to do here..."
else
	echo "HISTSIZE is not set in /etc/bashrc"
	echo "Configuring the environment variable"
	echo "export HISTSIZE=1000" >> /etc/bashrc
	source /etc/bashrc
fi

if [ -n "${HISTSIZE+x}" ]; then
	echo "HISTSIZE was set correctly"
else
	echo "ERROR: HISTSIZE was not set"
fi

#!/usr/bin/env python

__author__ = 'dragos.prisaca'
__copyright__ = "Copyright 2012, G2, Inc."
__credits__ = ["Dragos Prisaca"]
__license__ = "TODO"
__version__ = "TODO"
__maintainer__ = 'dragos.prisaca'
__email__ = "TODO"
__status__ = "Alpha"

import os
import sys
from subprocess import *

name="RPM Info Test"
number=0
packageOne="testpackage1-2.3.4a-0.1"
packageTwo="testpackage2-2.3.4a-0"
packageOneRPM="testpackage1-2.3.4a-0.1.Noarch.rpm"
packageTwoRPM="testpackage2-2.3.4a-0.i386.rpm"
packageOneInstalled="no"
packageTwoInstalled="no"

def performConfig(workingDir=None):
	try:
		print("configuration {0} for {1}".format(number, name))
		print("configuring the {0} package".format(packageOne))
		print("should package {0} be installed? {1}".format(packageOne,packageOneInstalled))

		if packageOneInstalled=="yes":
			#give me all the installed packages
			output=getoutput("rpm -qa")
			#try to install packageOne using rpm command.
			if packageOne not in output:
				call(["rpm","-ivh",packageOneRPM])
			output=getoutput("rpm -qa")
			#if the package exists and should be there
			if packageOne not in output:
				print("ERROR: package not found, please install and retry!")
				sys.exit()
 				
		elif packageOneInstalled=="no":
			output=getoutput("rpm -qa")
			if packageOne in output:
				#remove packageOne
				call(["rpm","-ev",packageOne])
		else:
			print("Bad config, package installed error")
			sys.exit()

		print("configuring the {0} package".format(packageTwo))
		print("should package {0} be installed? {1}".format(packageTwo,packageTwoInstalled))		
		if packageTwoInstalled=="yes":
			#give me all the installed packages
			output=getoutput("rpm -qa")
			#try to install packageTwoS using rpm command
			if packageTwo not in output:
				call(["rpm","-ivh",packageTwoRPM])
			output=getoutput("rpm -qa")
			#if the package exists and should be there
			if packageTwo not in output:
				print("ERROR: package not found, please install and retry!")
				sys.exit()
		elif packageTwoInstalled=="no":
			output=getoutput("rpm -qa")
			if packageTwo in output:
				#remove packageTwo
				call(["rpm","-ev",packageTwo])
		else:
			print("Bad config, package installed error")
			sys.exit()


	except OSError as e:
		print("Execution failed:", e, file=sys.stderr)


if __name__ == "__main__":
	sys.exit(performConfig())

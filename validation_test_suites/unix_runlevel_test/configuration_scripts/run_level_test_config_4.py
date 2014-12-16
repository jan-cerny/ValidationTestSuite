import sys
from subprocess import *

name="Run Level Test"
number=4
packageOne="httpd"
packageTwo="mysqld"
packageTwoS="mysql-server"
packageOneInstalled="yes"
packageTwoInstalled="no"
packageOneOpts=['on', 'on', 'on', 'on', 'on', 'on', 'on']
packageTwoOpts=['na', 'na', 'na', 'na', 'na', 'na', 'na']


def performConfig(workingDir=None):
	try:
		print("configuration {0} for {1}".format(number, name))
		print("configuring the {0} package".format(packageOne))
		print("should package {0} be installed? {1}".format(packageOne,packageOneInstalled))
		

		if packageOneInstalled=="yes":
			#give me all the installed packages with runlevels
			output=getoutput("/sbin/chkconfig --list")
			#try to install packageOne using yum - it works if the OS is registered with RHN.
			if packageOne not in output:
				call(["yum","-y","install",packageOne])
			output=getoutput("/sbin/chkconfig --list")
			#if the package exists and should be there
			if packageOne in output:
				for level,opt in enumerate(packageOneOpts):
					print("setting run level "+str(level)+" for "+packageOne+" to "+opt)
				#set the appropriate run levels
					call(["/sbin/chkconfig","--level",str(level),packageOne,opt])
			else:
				print("package not found, please install and retry")
				sys.exit()
 				
		elif packageOneInstalled=="no":
			call(["yum","-y","remove",packageOne])
			#p1 = Popen(["find","/","-name",packageOne], stdout=PIPE)
			#p2 = Popen(["xargs", "rm"], stdin=p1.stdout, stdout=PIPE)
			#p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2exits.
			#output = p2.communicate()[0]
		
		else:
			print("Bad config, package installed error")
			sys.exit()

		
		if packageTwoInstalled=="yes":
			#give me all the installed packages with runlevels
			output=getoutput("/sbin/chkconfig --list")
			#try to install packageTwoS using yum - it works if the OS is registered with RHN.
			if packageTwo not in output:
				call(["yum","-y","install",packageTwoS])
			output=getoutput("/sbin/chkconfig --list")
			#if the package exists and should be there
			if packageTwo in output:
				for level,opt in enumerate(packageTwoOpts):
					print("setting run level "+str(level)+" for "+packageTwo+" to "+opt)
					#set the appropriate run levels
					call(["/sbin/chkconfig","--level",str(level),packageTwo,opt])
			else:
				print("package not found, please install and retry")
				sys.exit()
		elif packageTwoInstalled=="no":
			call(["yum","-y","remove",packageTwoS])
			#p1 = Popen(["find","/","-name",packageTwo], stdout=PIPE)
			#p2 = Popen(["xargs", "rm"], stdin=p1.stdout, stdout=PIPE)
			#p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2exits.
			#output = p2.communicate()[0]
		
		else:
			print("Bad config, package installed error")
			sys.exit()


	except OSError as e:
		print("Execution failed:", e, file=sys.stderr)



if __name__ == "__main__":
	sys.exit(performConfig())
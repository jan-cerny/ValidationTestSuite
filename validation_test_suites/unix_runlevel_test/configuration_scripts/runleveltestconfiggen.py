import sys
from subprocess import *

def create_config_shell_script(tup):

	try:
		things='''import sys
from subprocess import *

name="Run Level Test"
number={num}
packageOne="{packone}"
packageTwo="{packtwo}"
packageOneInstalled="{packonei}"
packageTwoInstalled="{packtwoi}"
packageOneOpts={packoneo}
packageTwoOpts={packtwoo}\n'''
		things=things.format(num=tup[0][0],packone=tup[0][1],packtwo=tup[1][1],packonei=tup[0][2],packtwoi=tup[1][2],packoneo=tup[0][3:],packtwoo=tup[1][3:])	

		other_things="""

def performConfig():
	try:
		print("configuration {0} for {1}".format(number, name))
		print("configuring the {0} package".format(packageOne))
		print("should package {0} be installed? {1}".format(packageOne,packageOneInstalled))
		

		if packageOneInstalled=="yes":
			#give me all the installed packages with runlevels
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
			p1 = Popen(["find","/","-name",packageOne], stdout=PIPE)
			p2 = Popen(["xargs", "rm"], stdin=p1.stdout, stdout=PIPE)
			p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2exits.
			output = p2.communicate()[0]
		
		else:
			print("Bad config, package installed error")
			sys.exit()

		
		if packageTwoInstalled=="yes":
			#give me all the installed packages with runlevels
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
			p1 = Popen(["find","/","-name",packageTwo], stdout=PIPE)
			p2 = Popen(["xargs", "rm"], stdin=p1.stdout, stdout=PIPE)
			p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2exits.
			output = p2.communicate()[0]
		
		else:
			print("Bad config, package installed error")
			sys.exit()


	except OSError as e:
		print("Execution failed:", e, file=sys.stderr)



if __name__ == "__main__":
	sys.exit(performConfig())"""

	

	except IndexError as e:
		print("hitting error: "+str(e))
		return "error"
	return things+other_things

"""*******************************MAIN***********************************"""
input_file=sys.argv[1]

#parse through the file
with open(input_file) as configs:

	#the config files are in a two row format, a header and a non header
	headers=[]
	nonheaders=[]
	#list to keep my configs


	for line in configs:
		#tab delimited conf file
		splits=line.split('\t')
		#if the header exists, its the beginning of a new config
		if splits[0].strip():
			headers.append(splits)
		else:	
			nonheaders.append(splits)

#make it easy to instantiate
zipped=zip(headers,nonheaders)


for i,zippy in enumerate(zipped):
	f=open("run_level_test_config_"+str(i+1)+".py", "w")
	#for each config, create a script that will configure the system as desired
	f.write(create_config_shell_script(zippy))
	
	f.close()



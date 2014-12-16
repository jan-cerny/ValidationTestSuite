import sys


def create_config_shell_script():
	return 2

inputFile=sys.argv[1]

configs={}
metaConfigs= open(inputFile)

for line in metaConfigs:
	splits=line.split("\t")
	ident=splits[1]+","+splits[3]
	if ident in configs:
		configs[ident].append(splits[2])
	else:
		configs[ident]=[splits[2]]

configCommands=[]

#create command text for each key value pair
for key,booleans in configs.items():
	splits=key.split(",")
	myString=splits[0]+" {0} "+splits[1]
	print(myString)
	newValues=[]
	for b in booleans:
		call_command=""
		if len(splits[0].split())==2:
			call_command="call(['/usr/sbin/"+splits[0].split()[0]+"','"+splits[0].split()[1]+"','"+b+"','"+splits[1].strip()+"'])\n"
		elif len(splits[0].split())==1:
			call_command="call(['/usr/sbin"+splits[0].split()[0]+"','"+b+"','"+splits[1].strip()+"'])\n"
		else:
			print("something went wrong")
			sys.exit()
		command=myString.format(b)
		newValues.append(call_command)
	
	
	configCommands.append('\t'.join(newValues))
	print(configCommands)

#clever i know
for i,things in enumerate(configCommands):
	print(i,things)
	f=open("selinux_boolean_test_config_"+str(i+1)+".py", "w")
	#for each config, create a script that will configure the system as desired
	f.write("from subprocess import* \n")
	f.write("def performConfig():\n\t")
	f.write(things)
	f.write("if __name__ == '__main__':\n\tsys.exit(performConfig()")
	f.close()

	

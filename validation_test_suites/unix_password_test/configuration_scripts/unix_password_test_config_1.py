#!/usr/bin/env python

import sys
from subprocess import *

username="passwordtest1"
home_dir="/home/passwordtest1"
gcos="test"
group_id="505"
login_shell="/bin/bash"
password="geek"
user_id="505"

def performConfig(workingDir=None):
    print("configuring Unix Password Test number 1")
    f=open("password_file",'w')
    #f.write("{0}:{1}:{2}:{3}:{4}:{5}:{6}:{7}".format(username,password,user_id,group_id,gcos,home_dir,login_shell))
    f.write(username+":"+password+":"+user_id+":"+group_id+":"+gcos+":"+home_dir+":"+login_shell+"\n")
    f.close()
    #user stuff
    call(["/usr/sbin/newusers","password_file"])

if __name__ == "__main__":
    performConfig()

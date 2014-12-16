#!/bin/bash
# Script name:   linux_partition_test_cleanup.sh
# Purpose:		 Remove configuration 1
# Last updated by Author: dragos.prisaca
# Current $Revision: na

#Functions
in_list() {
	# Function to determine if a loop device is in use
	local loop_dev="$1" # 1st argument
	shift
	local list_of_loop_devices=("$@")
	for device in $list_of_loop_devices
	do
		[[ "$device" == "$loop_dev" ]] && return 0 #device found
	done
	return 1 #device not found
}

#Main
#Global variable
Working_Directory="/scap_validation_content"
Test_Name="linux_partition_test"
File_Name="1GBfile.dat"
Mount_Point="/mnt/my_loop_device"

LOOPDEVICES=`losetup -a | awk '{ print $1 }'`
if [ -z "$LOOPDEVICES" ] # LOOPDEVICES is empty - none of them are used
then
	echo There are no loop devices in use.
else
	for i in {0..7}
	do
		LoopDevice="/dev/loop$i"
		if in_list "$LoopDevice:" "${LOOPDEVICES[@]}" 
		then
			echo "Device: $LoopDevice is in use. Continuing..."
			
			#is this device in use by my 1GBfile.dat ?
			output=`losetup $LoopDevice | awk '{ print $3 }'`
			if [ $output == "($Working_Directory/$Test_Name/$File_Name)" ]; then
				echo "	the device is used by 1GBfile.dat"
			
				#is the $LoopDevice mounted?
				if grep -qs "$LoopDevice" /proc/mounts; then
					umount "$LoopDevice" #unmount the device
				fi				
				losetup -d "$LoopDevice" #Detach the file or device associated with the specified loop device.
				[ -f "$Working_Directory/$Test_Name/$File_Name" ] && rm -rf "$Working_Directory/$Test_Name/$File_Name"
			fi
		else
			echo "$LoopDevice is not used. Nothing to do. Continuing..."
			#break #Abandon the loop when I found a device that's not in use
		fi
	done
fi

[ -f "$Working_Directory/$Test_Name/$File_Name" ] && rm -rf "$Working_Directory/$Test_Name/$File_Name"
[ -d "$Working_Directory/$Test_Name" ] && rm -rf "$Working_Directory/$Test_Name"

echo "Done."

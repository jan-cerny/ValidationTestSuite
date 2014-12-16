#!/bin/bash
# Script name:   linux_partition_test_config1.sh
# Purpose:		 Apply configuration 1 for Linux Partition Test
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
	#echo All the loop devices are not in used. I can use the /dev/loop0
	LoopDevice="/dev/loop0" #use /dev/loop0
else
	for i in {0..8}
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
				break #Abandon the loop
			fi
			
		else
			echo "$LoopDevice is available."
			break #Abandon the loop when I found a device that's not in use
		fi
	done
fi
echo "I'll use $LoopDevice"
if [ $LoopDevice != "/dev/loop8" ]
then
	# Create 1GBFile
	[ ! -d "$Working_Directory" ] && mkdir $Working_Directory
	[ ! -d "$Working_Directory/$Test_Name" ] && mkdir $Working_Directory/$Test_Name
	[ ! -f "$Working_Directory/$Test_Name/$File_Name" ] && echo "Creating $Working_Directory/$Test_Name/$File_Name. Please wait..." && dd if=/dev/zero of="$Working_Directory/$Test_Name/$File_Name" bs=4096 count=248291
	losetup "$LoopDevice" "$Working_Directory/$Test_Name/$File_Name"
	mkfs.ext3 -b 4096 "$LoopDevice"
	tune2fs "$LoopDevice" -U 11111111-2222-3333-4444-555555555555
	[ ! -d "$Mount_Point" ] && mkdir $Mount_Point
	mount "$LoopDevice" "$Mount_Point"
else
	echo "ERROR: There are no loop devices available!"
fi

exit
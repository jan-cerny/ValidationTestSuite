#!/bin/bash

# set the timezone to UTC
mv -f /etc/localtime /etc/localtime.bak
ln -s /usr/share/zoneinfo/UTC /etc/localtime

#create directories and files
mkdir /tmp/scap_validation_content
mkdir /tmp/scap_validation_content/unix_file
mkdir /tmp/scap_validation_content/unix_file/ne
mkdir /tmp/scap_validation_content/unix_file/e
chmod 777 /tmp/scap_validation_content/unix_file/e
chmod +t /tmp/scap_validation_content/unix_file/e
echo "This is 1.txt scap validation test file.">>/tmp/scap_validation_content/unix_file/e/1.txt
echo "This is 2.txt scap validation test file.">>/tmp/scap_validation_content/unix_file/e/2.txt
cp Skeleton.sh /tmp/scap_validation_content/unix_file/Skeleton.sh
cp Skeleton.sh /tmp/scap_validation_content/unix_file/e/Skeleton.sh
touch -a -t 201108011526.12 /tmp/scap_validation_content/unix_file/Skeleton.sh
touch -m -t 201108011439.31 /tmp/scap_validation_content/unix_file/Skeleton.sh
echo "This is Skeleton2.sh scap validation test file.">>/tmp/scap_validation_content/unix_file/e/Skeleton2.sh
echo "This is Skeleton3.sh scap validation test file.">>/tmp/scap_validation_content/unix_file/e/Skeleton3.sh
echo "This is a test file for the scap validation program.">/tmp/scap_validation_content/unix_file/e/abc.txt
#create testuser and scapvalidation group
groupadd -g 500 scapvalidation
useradd -g scapvalidation -u 5000 testuser
chown testuser:scapvalidation /tmp/scap_validation_content/unix_file/e/1.txt
chmod 777 /tmp/scap_validation_content/unix_file/e/1.txt
chmod a+s /tmp/scap_validation_content/unix_file/e/1.txt
chmod 77 /tmp/scap_validation_content/unix_file/e/Skeleton2.sh
#set extended attribute
setfattr -n user.testing -v "this is a test" /tmp/scap_validation_content/unix_file/e/Skeleton3.sh
setfacl -m g:scapvalidation:rx /tmp/scap_validation_content/unix_file/e/Skeleton3.sh
chmod 700 /tmp/scap_validation_content/unix_file/e/Skeleton3.sh

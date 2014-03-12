#!/bin/bash

if [ $# -lt 1 ]; then
	echo "not enough parameters"
	echo "code_name"
	exit -1
fi


mysql -u root -pQwerty21 -e "drop database $1"
rm -rf /home/hashcow/stratum_directories/$1
sudo rm -rf /var/www/MPOS_$1

sudo initctl stop twistd_$1
rm /etc/init/upstart/twistd_$1

#erase db
#erase stratum
#erase MPOS

#should remove cronjob!


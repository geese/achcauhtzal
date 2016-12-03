#!/bin/bash - 
#===============================================================================
#
#          FILE: run_report.sh
# 
#         USAGE: ./run_report.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Raymond Anderson (), raymondanderson1@mail.weber.edu
#  ORGANIZATION: 
#       CREATED: 11/23/2016 23:01
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

function help()
{
	echo "Usage run_report.sh [-f Beginning date] [-t end date]"
	echo "[-e email] [-u user] [-p password]"
	echo "All arguments are required"
	exit 1 
}

if [[ $1 == -help ]]
then 
	help
fi



if [[ $# -ne 10 ]]
then
	help
fi



while getopts ":f:t:e:u:p:" opt; do
	case $opt in 
	f) beginDate=$OPTARG
	;;
	t) endDate=$OPTARG
	;;
	e) email=$OPTARG
	;;
	u) user=$OPTARG
	;;
	p) password=$OPTARG
	;;
	\?) help
	;;
	esac 
done
echo $endDate
python3 create_report.py $beginDate $endDate

if [[ $? == 0 ]] 
then
ftp -inv 137.190.19.84 << EOF
user $user $password
get file1.txt retrieval.$$
bye 
EOF
	mail -s "Successfully transferred file (FTP Address)" "$email" << EMAIL
Successfully created a transaction report from BegDate to EndDate 
EMAIL

fi

if [[ $? == -1 ]]
then
mail -s "The create_report program exited with code -1" "$email" << EMAIL 
Bad Input parameters BegDate EndDate
EMAIL

fi




if [[ $? == -2 ]]
then 
	mail -s "The create_report program exit with code -2" "$email" << EMAIL
	No transaction available from BegDate to EndDate
EMAIL 
fi

exit 0

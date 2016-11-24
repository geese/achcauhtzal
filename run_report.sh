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
`python -c "import create_report.py; create_report.main($beginDate, $endDate)"` 

exit 0

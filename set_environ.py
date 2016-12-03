#!/usr/bin/env python
"""
Sets the following environment variables needed to connect to the database.  
    DB:     MySQL database name
    DB_ACT: MySQL database user name
    DB_PW:  MySQL database password
"""
import sys
import os


def getDatabase():
    return os.environ.get('DB', '')

def getUser():
    return os.environ.get('DB_ACT','')

def getPass():
    return os.environ.get('DB_PW', '')


# Main function
def main():
    """
    Set the environment variables for connecting to database.
    """
    #uncomment these to use credentials other than Gisela's
    os.environ["DB"]="W01216188"
    os.environ["DB_ACT"]="W01216188"
    os.environ["DB_PW"]="Raymondcs!"
    
    #os.environ["DB"]="W01267781"
    #os.environ["DB_ACT"]="W01267781"
    #os.environ["DB_PW"]="Giselacs!"
    
    return


if __name__ == '__main__':
    # Call Main
    main()

    exit(0)










#!/usr/bin/env python
"""
Takes two date format input parameters needed to query the database, converts them to datetime format for MySQL.
Args:
    beg_date:   format YYYYMMDD
    end_date    format YYYYMMDD
"""
import sys
import re

def convertToDateTime(beg_date, end_date):
    """
    Converts date range to datetime range for MySQL
    Args:
        beg_date:   format YYYYMMDD
        end_date    format YYYYMMDD
    Returns: 
        tuple of datetimes.  
        tuple[0] is format YYYY-MM-DD 00:00
        tuple[1] is format YYYY-MM-DD 23:59
    """
    return (beg_date[0:4]+'-'+beg_date[5:7]+'-'+beg_date[-2:]+' 00:00',
            end_date[0:4]+'-'+end_date[5:7]+'-'+end_date[-2:]+' 23:59')



def isValidDateInput(date):
    """
    Checks that date input matches format YYYYMMDD
    Args:
        date:  the date input (or supposed date)
    Returns:
        True if format is YYYYMMDD
        False if format is not YYYYMMDD, or the first digit is 0.
    """
    pattern = re.compile('[1-9]\d{7}')
    if pattern.match(date) == None:
        return False
    else:
        return True


# Main function
def main(beg_date, end_date):
    """
    Read two input date format parameters and send them to convertToDateTime() for conversion.
    Args:
        beg_date:   beginning date, format YYYYMMDD
        end_date:   end date, format YYYYMMDD
    """
    for date in (beg_date, end_date):
        if isValidDateInput(date) == False:
            exit(-1)
    return convertToDateTime(beg_date, end_date)


if __name__ == '__main__':
    # Call Main
    main(sys.argv[1], sys.argv[2])
    exit(0)










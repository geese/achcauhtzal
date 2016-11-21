#!/usr/bin/env python
"""
Takes two date format input parameters needed to query the database, converts them to datetime format for MySQL.
Args:
    beg_date:   format YYYYMMDD
    end_date    format YYYYMMDD
"""
import sys


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
    pass  


# Main function
def main(beg_date, end_date):
    """
    Read two input date format parameters and send them to convertToDateTime() for conversion.
    Args:
        beg_date:   beginning date, format YYYYMMDD
        end_date:   end date, format YYYYMMDD
    """
    convertToDateTime(beg_date, end_date)
    # TODO:  check for bad input and exit(-1)
    return


if __name__ == '__main__':
    # Call Main
    main(sys.argv[1], sys.argv[2])
    exit(0)










#!/usr/bin/env python3
"""
Takes two date format input parameters needed to query the tr_database, converts them to datetime format for MySQL.
Args:
    beg_date:   format YYYYMMDD
    end_date    format YYYYMMDD
"""
import sys
import re
import set_environ as s
import mysql.connector
from mysql.connector import Error, MySQLConnection


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
    return (beg_date[0:4]+'-'+beg_date[4:6]+'-'+beg_date[-2:]+' 00:00',
            end_date[0:4]+'-'+end_date[4:6]+'-'+end_date[-2:]+' 23:59')



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


def getTransactions(beg_date, end_date):
    """
    Connect to MySQL tr_database using environment variables
    """
    # set environment variables in order to be able to connect to database
    s.main() 
    
    dates = convertToDateTime(beg_date, end_date)
    print(dates)

    try:
        conn = MySQLConnection(user=s.getUser(), password=s.getPass(),host='lOcalhost',database=s.getDatabase())
        
        if conn.is_connected():
            print("Connected to", s.getDatabase())
        else:
            print("Connection Failed!")

        print("Getting transactions from {} to {}".format(dates[0], dates[1]))

        cursor = conn.cursor()
        
        exec = 'SELECT t.trans_id, trans_date, card_num, total, tl.prod_num, qty, amt, prod_desc FROM trans t JOIN trans_line tl ON t.trans_id = tl.trans_id JOIN products p ON tl.prod_num = p.prod_num WHERE trans_date between {} AND {}'.format('"'+dates[0]+'"','"'+dates[1]+'"')
       
        cursor.execute(exec)

        rows = cursor.fetchall()
        num_rows = cursor.rowcount
        
        if num_rows > 0:
            # hold the data for the first transaction
            tr_data = {'trans_id':rows[0][0], 'trans_date':re.sub('[\- :]','',str(rows[0][1])), 
                    'card_num':rows[0][2], 'total':rows[0][3]}
        else: # no transactions available for the input dates
            exit(-2)

        #initialize the first line that will be printed 
        printString = '{id:05}{date}{card}'.format(id=tr_data['trans_id'],
                date=tr_data['trans_date'],card=tr_data['card_num'])
            
        num_products = 0

        for row in rows:
            # it is not a new transaction, (not a new trans id) so add a product field to the printString
            if row[0] == tr_data['trans_id']: #not a new transaction
                printString += '{qty:02}{amt:06.0f}{desc:<10}'.format(qty=int(row[5]),amt=row[6]*100,desc=row[7])
                num_products += 1

            # it is a new transaction, (a new trans id) or it's the last row in the database results,
            # so print blank products if needed, and print the last transaction if this is the last row.
            # If not the last row, hold transaction data from the next transaction
            if row[0] != tr_data['trans_id'] or row == rows[-1]: 
                num_blanks = 3 - num_products
                for i in range(0, num_blanks):
                    printString += '{qty:02}{amt:06.0f}{desc:<10}'.format(qty=0,amt=0,desc='')
                printString += '{total:06.0f}'.format(total=tr_data['total']*100)
                print(printString)
                num_products = 0
                tr_data['trans_id'] = row[0]
                tr_data['trans_date'] = re.sub('[\- :]','',str(row[1]))
                tr_data['card_num'] = row[2]
                tr_data['total'] = row[3]
                printString = '{id:05}{date}{card}'.format(id=tr_data['trans_id'],
                        date=tr_data['trans_date'],card=tr_data['card_num'])
                printString += '{qty:02}{amt:06.0f}{desc:<10}'.format(qty=int(row[5]),amt=row[6]*100,desc=row[7])
                num_products += 1



    except Error as error:
        print(error)
    finally:
        conn.close()
        print("Connection closed")


# Main f/nction
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










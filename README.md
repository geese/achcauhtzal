# achcauhtzal

# create_report.py
# Takes two input parameters (beg_date, end_date).
# Queries the database to retrieve the transaction information needed.

# set_environ.py
# Sets the environment variables needed to connect to the database.

# run_report.sh
# Calls create_report.py
# If succesful compresses teh file using zip and transfers the file via FTP to the FTP server and emails the user.
# If unsuccesful the user is emailed the error.

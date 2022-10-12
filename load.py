import pandas as pd
import os
from datetime import datetime
import mysql.connector
from mysql.connector import errorcode

from config import db_host, db_name, db_user, db_password, date_format, debug
from insert import add_security, add_bhavcopy


def load_securities():
    print('loading securities')
    # import csv
    data = pd.read_csv(r'./securities/securities.csv')
    securities = pd.DataFrame(data)

    try:
        con = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_name)
        cursor = con.cursor()

        # for each row in securities df
        for index, s in securities.iterrows(): 
            debug and print(s)

            # collect data to be inserted
            data_security = (s[0], s[1], s[2], datetime.strptime(s[3], date_format).date(), float(s[4]), float(s[5]), s[6], s[7])
            debug and print(data_security)

            # insert new data
            cursor.execute(add_security, data_security)
        con.commit()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials provided!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("database does not exist!")
        else:
            print(err)
    else:
        con.close()

# load bhavcopy data into database
def load_bhavcopy():
    print('loading bhavcopies')
    directory = r'./bhavcopy'
    
    # for each bhavcopy in bhavcopy/
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            # import csv as dataframe
            data = pd.read_csv(f)
            bhavcopies = pd.DataFrame(data)

        try:
            con = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_name)
            cursor = con.cursor()

            # for each row in dataframe
            for index, b in bhavcopies.iterrows():
                debug and print(b)

                # collect data to be inserted
                data_bhavcopy = (b[0], str(b[1]), float(b[2]), float(b[3]), float(b[4]), float(b[5]), float(b[6]), float(b[7]), float(b[8]), int(b[9]), datetime.strptime(b[10], date_format).date(), b[11], b[12])
                debug and print(data_bhavcopy)

                # insert new row
                cursor.execute(add_bhavcopy, data_bhavcopy)
            con.commit()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Invalid credentials provided!")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("database does not exist!")
            else:
                print(err)
        else:
            con.close()
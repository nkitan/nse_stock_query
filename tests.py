from datetime import datetime
import mysql.connector
from mysql.connector import errorcode


from config import db_host, db_name, db_user, db_password, date_format
from insert import add_security, add_bhavcopy

def test_securities():
    print('testing securities')

    try:
        con = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_name)
        cursor = con.cursor()
        format = '%d-%b-%Y'
        data_security = ('20MICRONS','20 Microns Limited','EQ', datetime.strptime('06-OCT-2008', date_format).date(), 5, 1, 'tINE144J01027', 5)

        # Insert new security
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
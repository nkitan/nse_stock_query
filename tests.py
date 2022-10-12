from datetime import datetime
from load import *
import mysql.connector
from mysql.connector import errorcode


from config import db_host, db_name, db_user, db_password, date_format
from insert import add_security, add_bhavcopy

def test_load_securities():
    print('testing load_securities')

    try:
        load_securities()
    except Exception as err:
        print(err)

def test_load_bhavcopy():
    print('testing load_bhavcopy')

    try:
        load_bhavcopy()
    except Exception as err:
        print(err)


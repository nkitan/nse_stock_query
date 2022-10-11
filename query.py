import mysql.connector
from mysql.connector import errorcode
from tabulate import tabulate

from config import db_host, db_name, db_user, db_password

def run_query(query): 
    print('running query ' + str(query))
    try:
        con = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_name)
        cursor = con.cursor()
        cursor.execute(query)

        # get all records
        result = cursor.fetchall()

        if(len(result) == 0):
            print("Empty result set!")
            return

        print(tabulate(result, tablefmt='mysql'))

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials provided!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("database does not exist!")
        else:
            print(err)
    else:
        con.close()

def top_25_gainers():
    query = "SELECT *, ((bclose - bopen) / bopen ) AS Gains FROM Bhavcopy ORDER BY Gains DESC LIMIT 25;"
    run_query(query)

top_25_gainers()
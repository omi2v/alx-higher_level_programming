#!/usr/bin/python3


import MySQLdb
from sys import argv

'''

a script that lists all states
from the database
'''
if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost",
            port=3306,
            user=argv[0],
            password=argv[0],
            database=argv[0])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    db = cursor.fetchall()
    for i in db:
        print(i)
        cursor.close()
        db.close()

#!/usr/bin/python3
""" Defines a script to list items"""
import MySQLdb
""" importing important modules"""

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa")
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ;")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

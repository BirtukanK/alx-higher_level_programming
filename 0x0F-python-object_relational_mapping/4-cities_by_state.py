#!/usr/bin/python3
""" Defines printing of database items"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], port=3306, host="localhost")
    cur = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name \
            FROM cities \
            JOIN states ON states.id = cities.state_id \
            ORDER BY cities.id ASC"
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

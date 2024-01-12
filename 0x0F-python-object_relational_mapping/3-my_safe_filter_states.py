#!/usr/bin/python3
""" Defines a script to list items"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    try:
        query = "SELECT * FROM states \
            WHERE BINARY name = '{}'".format(sys.argv[4])
        cur.execute(query)
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    except MySQLdb.Error as e:
        exit(e)
    finally:
        cur.close()
        conn.close()

#!/usr/bin/python3
"""
Script to get states
"""
import MySQLdb
import sys


if __name__ == '__main__':

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306,
                                user=arg1, passwd=arg2, db=arg3,
                                charset="utf8")
    cur = conn.cursor()

    cur.execute("""SELECT * FROM states WHERE name like
                BINARY 'N%' ORDER BY id ASC""")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

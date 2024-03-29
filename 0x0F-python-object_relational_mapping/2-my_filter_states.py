#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
"""
import MySQLdb
import sys


if __name__ == '__main__':

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
    x = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=arg1, passwd=arg2,
                                db=arg3, charset="utf8")

    cur = conn.cursor()

    query = """SELECT * FROM states
            WHERE name LIKE BINARY '{}' ORDER BY id ASC""".format(x)
    cur.execute(query)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

#!/usr/bin/python3
"""lists all states with a name starting with N"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute("""
                   SELECT * FROM states
                   WHERE name LIKE BINARY 'N%'
                   ORDER BY id ASC
                   """)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()

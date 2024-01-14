#!/usr/bin/python3
"""states models
  taskes a value arguments and display values
   in state table
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]  # "your_username"
    db_password = sys.argv[2]  # "your_password"
    db_name = sys.argv[3]  # "your_database_name"
    port = 3306

    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                   ORDER BY states.id ASC".format(sys.argv[4]))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

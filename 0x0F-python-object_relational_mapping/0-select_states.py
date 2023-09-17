#!/usr/bin/python3

"""
    Fetch and print all state records from the database.
    """

import MySQLdb
import sys


def fetch_all_states():
    """
    Fetch and print all state records from the database.

    Usage:
    ./script.py <mysql_username> <mysql_password> <database_name>
    """
    try:
        # Extract MySQL username, password, and database name
        # from command line arguments
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

        # Connect to the MySQL server running on localhost at port 3306
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Create a cursor object
        cursor = db.cursor()

        # Create the SQL query to retrieve all states sorted by states.id
        sql_query = "SELECT * FROM states ORDER BY states.id ASC"

        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all rows as a list of tuples
        states = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        db.close()

        # Display the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    fetch_all_states()

#!/usr/bin/python3

"""
    Fetch and print all city records from the database.
    """

import MySQLdb
import sys


def fetch_all_cities():
    """
    Fetch and print all city records from the database.

    Usage:
    ./script.py <mysql_username> <mysql_password> <database_name>
    """
    # Check if all 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Extract the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Create a cursor object
        cursor = db.cursor()

        # Create the SQL query to retrieve all cities sorted by cities.id
        sql_query = (
            "SELECT * FROM cities "
            "ORDER BY cities.id ASC"
        )

        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all rows as a list of tuples
        cities = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        db.close()

        # Display the results
        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    fetch_all_cities()

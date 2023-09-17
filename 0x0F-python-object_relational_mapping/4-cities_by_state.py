#!/usr/bin/python3

"""
This script connects to a MySQL database,
retrieves cities from a 'cities' table, and displays the results.
It takes three command-line arguments: MySQL username,
MySQL password, and the name of the database to connect to.
"""

import MySQLdb
import sys

if __name__ == "__main__":
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

        # Execute the SQL query to fetch cities and order by cities.id
        cursor.execute("SELECT * FROM cities ORDER BY cities.id")

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

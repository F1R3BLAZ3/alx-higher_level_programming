#!/usr/bin/python3

"""
    Fetch and print city names for a given state from the database.
    """

import MySQLdb
import sys


def fetch_cities_for_state():
    """
    Fetch and print city names for a given state from the database.

    Usage:
    ./script.py <mysql_username> <mysql_password> <database_name> <state_name>
    """
    # Check if all 4 arguments are provided
    usage = (
        "Usage: {} <mysql_username> <mysql_password> "
        "<database_name> <state_name>"
    )
    if len(sys.argv) != 5:
        print(usage.format(sys.argv[0]))
        sys.exit(1)

    # Extract the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

        # Create a parameterized SQL query to retrieve city names
        sql_query = (
            "SELECT GROUP_CONCAT(cities.name "
            "ORDER BY cities.id ASC SEPARATOR ', ') "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s"
        )

        # Execute the SQL query with the state name as a parameter
        cursor.execute(sql_query, (state_name,))

        # Fetch the result as a tuple
        result = cursor.fetchone()

        # Close the cursor and database connection
        cursor.close()
        db.close()

        # Display the results
        if result and result[0]:
            print(result[0])

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    fetch_cities_for_state()

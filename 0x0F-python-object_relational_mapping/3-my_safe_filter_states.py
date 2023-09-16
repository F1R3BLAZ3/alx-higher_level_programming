#!/usr/bin/python3

"""
This script connects to a MySQL database, retrieves states based on a user-provided state name
from a 'states' table using a parameterized query to prevent SQL injection, and displays the results.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Extract the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Create a parameterized query with placeholders to prevent SQL injection
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY states.id"

    # Execute the SQL query with the state name as a parameter
    cursor.execute(sql_query, (state_name,))

    # Fetch all rows as a list of tuples
    states = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    db.close()

    # Display the results
    for state in states:
        print(state)

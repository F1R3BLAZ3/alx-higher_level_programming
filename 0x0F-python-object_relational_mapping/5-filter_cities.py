#!/usr/bin/python3

"""
    Query cities by state name from a MySQL database.
    """

import MySQLdb
import sys


def main():
    """
    Query cities by state name from a MySQL database.
    """
    # Check if all 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(sys.argv[0]))
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

        # Create the SQL query with user input (SQL injection free)
        sql_query = (
            "SELECT cities.id, cities.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id"
        )

        # Execute the SQL query with the state name as a parameter
        cursor.execute(sql_query, (state_name,))

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
    main()

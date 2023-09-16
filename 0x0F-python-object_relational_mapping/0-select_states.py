#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".
        format(sys.argv[0]))
        sys.exit(1)

    # Extract the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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

    # Execute the SQL query to fetch states
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    # Fetch all rows as a list of tuples
    states = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    db.close()

    # Display the results
    for state in states:
        print(state)

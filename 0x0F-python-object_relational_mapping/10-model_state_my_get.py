#!/usr/bin/python3

"""
    Main function for querying a state by name from the database.
    """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Main function for querying a state by name from the database.
    """
    # Check if all 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> "
              "<state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Create a SQLAlchemy engine to connect to the MySQL server
        engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                               .format(mysql_username, mysql_password,
                                       database_name))

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the State object with the provided state name
        # (SQL injection safe)
        result = session.query(State).filter(State.name == state_name).first()

        # Display the result or "Not found" if no matching state is found
        if result:
            print(result.id)
        else:
            print("Not found")

        # Close the session
        session.close()

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

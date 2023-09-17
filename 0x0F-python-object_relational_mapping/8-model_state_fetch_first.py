#!/usr/bin/python3

"""
    Main function for querying and
    displaying the first state from the database.
    """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """
    Main function for querying and
    displaying the first state from the database.
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
        # Create a SQLAlchemy engine to connect to the MySQL server
        engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                               .format(mysql_username,
                                       mysql_password, database_name))

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the first State object by ordering by id and using .first()
        first_state = session.query(State).order_by(State.id).first()

        # Display the result
        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")

        # Close the session
        session.close()

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
This script fetches all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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
        # Create a SQLAlchemy engine to connect to the MySQL server
        engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                               .format(mysql_username, mysql_password,
                                       database_name))

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query all City objects and sort them by id in ascending order
        cities = session.query(City).order_by(City.id).all()

        # Display the results
        for city in cities:
            print("{}: ({}) {}".format(city.state.name, city.id, city.name))

        # Close the session
        session.close()

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

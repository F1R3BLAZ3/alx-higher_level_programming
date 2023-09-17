#!/usr/bin/python3

"""
    State class representing the 'states' table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()


class State(Base):
    """
    State class representing the 'states' table.

    Attributes:
        id (int): Primary key for the state.
        name (str): Name of the state.
    """
    __tablename__ = 'states'

    # Columns definition
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Create a SQLAlchemy engine to connect to the MySQL server
    engine = create_engine(
        'mysql://<username>:<password>@localhost:3306/<database_name>'
        )

    # Import all classes that inherit from Base
    # This ensures that all table definitions are available
    # before creating them
    import your_other_classes  # Import other classes as needed

    # Create tables based on the class definitions
    Base.metadata.create_all(engine)

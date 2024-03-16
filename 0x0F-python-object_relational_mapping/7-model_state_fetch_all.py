#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Assuming model_state.py is in the same directory

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}')

    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    # A DBSession() instance establishes all conversations with the database
    session = DBSession()

    # Query all states
    states = session.query(State).order_by(State.id).all()

    # Print states
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

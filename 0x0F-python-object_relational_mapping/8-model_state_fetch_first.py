#!/usr/bin/python3
"""
A script that prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}')
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the first state object
    state = session.query(State).order_by(State.id).first()

    # Print the state if it exists
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()

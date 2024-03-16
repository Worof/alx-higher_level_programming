#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
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

    # Query for states containing 'a'
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    # Print matching states
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()

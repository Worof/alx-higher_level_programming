#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa.
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
    states_to_delete = session.query(State).filter(State.name.like('%a%'))

    # Delete the fetched states
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()

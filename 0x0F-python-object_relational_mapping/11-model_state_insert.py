#!/usr/bin/python3
"""
A script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
and prints the new state's id.
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

    # Create new State object
    new_state = State(name="Louisiana")

    # Add the new State to the session and commit
    session.add(new_state)
    session.commit()

    # Print the new State id
    print(new_state.id)

    # Close the session
    session.close()

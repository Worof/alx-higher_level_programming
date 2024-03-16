#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State  # Ensure this module has the required relationships
from relationship_city import City  # Ensure this module has the required relationships and backref to State

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}')
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all Cities and their State
    cities = session.query(City).order_by(City.id).all()

    # Print each City and its State
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()

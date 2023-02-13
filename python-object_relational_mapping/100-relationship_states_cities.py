#!/usr/bin/python3
"""script to create city and state object"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3], pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = session(bind=engine)
    session = session()

    new_city = City(name='San Francisco', state=new_state)
    new_state = State(name='California')
    session.add(new_state)
    session.add(new_city)
    session.commit()
    session.close()

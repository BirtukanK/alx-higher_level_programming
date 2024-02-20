#!/usr/bin/python3
""" Defines State class"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)
    flag = False
    for state in states:
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            flag = True
            break
    if flag is False:
        print("Not found")
#!/usr/bin/python3
"""Gets the state that has a in the name
using where
"""
import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc


def get_states_with_a(username, password, db, name):
    """get state that has the name
    args:
        username: str - Username in the db
        password: str - mysql password
        db: str - name of DB
        name: str - state name
    """
    # create the engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username,
                password, db),
            pool_pre_ping=True
            )
    # Create session
    Session = sessionmaker(bind=engine)

    # start a new session
    session = Session()

    state = session.query(State).filter_by(name=name).first()
    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    get_states_with_a(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4])

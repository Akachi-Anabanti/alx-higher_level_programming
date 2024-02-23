#!/usr/bin/python3
"""updates a new state
"""
import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc


def update_state(username, password, db):
    """updates a new state to the db
    args:
        username: str - Username in the db
        password: str - mysql password
        db: str - name of DB
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

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.add(state)
    session.commit()


if __name__ == "__main__":
    update_state(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
